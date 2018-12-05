import os
import sys

py_gd_module = os.path.abspath('../')
sys.path.insert(0, py_gd_module)

try:
    import py_gd
    print('py_gd version:', py_gd.__version__)
except:
    exit('Error! Cannot import py_gd package.')


from py_gd import GoogleDrive, Scope

gd = GoogleDrive(cred='credentials.json', token='token.json', scopes=Scope.ALL)
