"""
docs:
  scope       = https://developers.google.com/drive/api/v3/about-auth
  mimeType    = https://developers.google.com/drive/api/v3/mime-types
  file search = https://developers.google.com/drive/api/v3/search-parameters
"""
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

from .gd_enum import Scope, MimeType

__all__ = ['GoogleDrive']

class GoogleDrive(object):
    def __init__(self, token=None, cred=None, scopes=Scope.READONLY):
        if not isinstance(scopes, list):
            scopes = [scopes]

        scopes = [s.value if isinstance(s, Scope) else s for s in scopes]

        store = file.Storage(token)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(cred, scopes)
            creds = tools.run_flow(flow, store)

        self.service = build('drive', 'v3', http=creds.authorize(Http()))

    def upload_file(self, src, dest, folder=None, overwrite=True, mime=MimeType.SPREADSHEET):
        folder_id = self.create_folder(folder) if folder else None

        if isinstance(mime, MimeType):
            mime = mime.value

        file_metadata = {
            'name': dest,
            'mimeType': mime,
        }

        media = MediaFileUpload(
            src,
            mimetype='text/csv',
            resumable=True)

        kwargs = {
            'body': file_metadata,
            'media_body': media,
            'fields': 'id',
        }

        file_id = self.get_file_id(dest)

        if file_id:
            kwargs['fileId'] = file_id
            kwargs['addParents'] = folder_id
            self.service.files().update(**kwargs).execute()
        else:
            f = self.service.files().create(**kwargs).execute()
            self.service.files().update(fileId=f.get('id'), addParents=folder_id).execute()

    def get_file_id(self, filename, mime=MimeType.SPREADSHEET):
        if isinstance(mime, MimeType):
            mime = mime.value

        query = "name='{}' and mimeType='{}' and trashed = false".format(filename, mime)
        results = self.service.files().list(q=query).execute()
        items = results.get('files')
        return items[0]['id'] if items else None

    def get_folder_id(self, folder_name):
        query = "name='{}' and mimeType='{}'".format(folder_name, MimeType.FOLDER.value)
        results = self.service.files().list(q=query).execute()
        items = results.get('files')
        return items[0]['id'] if items else None

    def create_folder(self, folder_name):
        folder_id = self.get_folder_id(folder_name)
        if folder_id:
            return folder_id

        file_metadata = {
            'name': folder_name,
            'mimeType': MimeType.FOLDER.value
        }
        f = self.service.files().create(
            body=file_metadata,
            fields='id'
        ).execute()
        return f.get('id')

    # XXX: remove if not use
    def _test_list_files(self):
        # Call the Drive v3 API
        results = self.service.files().list(
            pageSize=10,
            fields="nextPageToken, files(id, name)"
        ).execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

def main():
    gd = GoogleDrive()

if __name__ == '__main__':
    main()
