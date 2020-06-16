import base64
import os
import sys
import time
import traceback

from datetime import datetime
from shareplum import Office365
from shareplum import Site
from shareplum.site import Version


# \venv\lib\site-packages\shareplum\folder.py" Need change field timeout in __init__ to None

# tenant_O365 = 'https://rgorgua.sharepoint.com/'
# username_O365 = 'c2hwYWtAYXN0cmVsbGEuY29tLnVh'
# password_O365 = 'MzNHamhuY2J1Zmhm'
# site_O365_path = 'https://rgorgua.sharepoint.com/sites/astrella/'
# shared_dir_path = 'Shared Documents/ИТ Служба/BackUps/Astrella/1C_UTP/'
# local_dir_path = '//10.123.11.10/DB_backups/astrella/'

def o365_login(tenant, username, password, site_o365, shared_folder):
    authcookie = Office365(tenant,
                           username=base64.b64decode(username).decode('utf-8'),
                           password=base64.b64decode(password).decode('utf-8')).GetCookies()
    site = Site(site_o365, version=Version.v365, authcookie=authcookie)
    folder_shared_o365 = site.Folder(shared_folder)
    print(time_now(), f'    Login to O365 to {site_o365} is successful!')
    return folder_shared_o365


def copy_to_sp(tenant: str, username: str, password: str, site_o365: str, shared_folder: str, local_folder: str):
    try:
        folder_shared_o365 = o365_login(tenant, username, password, site_o365, shared_folder)

        files_local = [f for f in os.listdir(local_folder)]

        for file in sorted(files_local, key=lambda f: os.path.getatime(os.path.join(local_folder, f)), reverse=True)[
                    :2]:
            file_abs_path = os.path.join(local_folder, file)
            print(time_now(), f'    File: {file_abs_path}')
            print(time_now(), f'    Created: {time.ctime(os.path.getatime(file_abs_path))}')
            print(time_now(), f'    File size: {os.path.getsize(file_abs_path) // 1024 // 1024} Mb')

            with open(file_abs_path, 'rb') as f:
                data = f.read()
                folder_shared_o365.upload_file(data, file)
                print(time_now(), f'    File: {file} copied successfully.')
    except Exception as e:
        print(time_now(), '    Script is end with error!!!.'.upper())
        print(time_now(), f'    {e}')
        print(time_now(), f'    {traceback.format_exc()}')
        sys.exit()
    else:
        print((time_now()), f'    Copy to folder {site_o365 + shared_folder} completed successfully.')


def time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M')

# e = base64.b64encode(b'33Gjhncbufhf')
# print(e)
#
# d = base64.b64decode('MzNHamhuY2J1Zmhm')
#
# print(d.decode('utf-8'))
