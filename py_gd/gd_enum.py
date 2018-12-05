from enum import Enum

# https://developers.google.com/drive/api/v3/about-auth
class Scope(Enum):
    ALL               = 'https://www.googleapis.com/auth/drive'
    READONLY          = 'https://www.googleapis.com/auth/drive.readonly'
    APPFOLDER         = 'https://www.googleapis.com/auth/drive.appfolder'
    FILE              = 'https://www.googleapis.com/auth/drive.file'
    INSTALL           = 'https://www.googleapis.com/auth/drive.install'
    METADATA          = 'https://www.googleapis.com/auth/drive.metadata'
    METADATA_READONLY = 'https://www.googleapis.com/auth/drive.metadata.readonly'
    SCRIPTS           = 'https://www.googleapis.com/auth/drive.scripts'
    APPS_READONLY     = 'https://www.googleapis.com/auth/drive.apps.readonly'


# https://developers.google.com/drive/api/v3/about-auth
class MimeType(Enum):
    AUDIO        = 'application/vnd.google-apps.audio'
    DOCUMENT     = 'application/vnd.google-apps.document'
    DRAWING      = 'application/vnd.google-apps.drawing'
    FILE         = 'application/vnd.google-apps.file'
    FOLDER       = 'application/vnd.google-apps.folder'
    FORM         = 'application/vnd.google-apps.form'
    FUSIONTABLE  = 'application/vnd.google-apps.fusiontable'
    MAP          = 'application/vnd.google-apps.map'
    PHOTO        = 'application/vnd.google-apps.photo'
    PRESENTATION = 'application/vnd.google-apps.presentation'
    SCRIPT       = 'application/vnd.google-apps.script'
    SITE         = 'application/vnd.google-apps.site'
    SPREADSHEET  = 'application/vnd.google-apps.spreadsheet'
    UNKNOWN      = 'application/vnd.google-apps.unknown'
    VIDEO        = 'application/vnd.google-apps.video'
    DRIVE_SDK    = 'application/vnd.google-apps.drive-sdk'
