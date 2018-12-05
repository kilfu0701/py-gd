# A tiny package for Google Drive

## Install
```sh
pip install py-gd
```

## Simple use & setmp

### Step 1:
Get your `credentials.json` from https://developers.google.com/drive/api/v3/quickstart/python

### Step 2:
```sh
python -c 'import py_gd; py_gd.GoogleDrive(cred="credentials.json", token="token.json")'
```

### Step 3:
It will open a webpage for authentication, and will generate `token.json` after authenticated.

## Packages usage

### Create folder
```python
from py_gd import GoogleDrive, Scope

gd = GoogleDrive(cred='credentials.json', token='token.json', scopes=Scope.ALL)
folder_id = gd.create_folder('NewFolder')
print('folder created. id = {}'.format(folder_id))
```
- About Scopes: [https://developers.google.com/drive/api/v3/about-auth](https://developers.google.com/drive/api/v3/about-auth)
- Here's py-gd [Scope enums](https://github.com/kilfu0701/py-gd/blob/master/py_gd/gd_enum.py#L4)

### Get folder id
```python
folder_id = gd.get_folder_id('NewFolder')
```

### Get file id
```python
from py_gd import MimeType

file_id = gd.get_file_id('my_file.csv', mime=MimeType.SPREADSHEET)
```
- About mimetype [https://developers.google.com/drive/api/v3/about-aut](https://developers.google.com/drive/api/v3/about-aut)
- Here's py-gd [MimeType enums](https://github.com/kilfu0701/py-gd/blob/master/py_gd/gd_enum.py#L17)

### Upload file
```python
src = '/local/dir/file.txt'
dest = 'file.txt'

gd.upload_file(src, dest)

# you can specify a folder
gd.upload_file(src, dest, folder='MyFolder')
```


## License

MIT

