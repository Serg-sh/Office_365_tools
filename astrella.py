import local_utils
import sp_utils

tenant_O365 = 'https://rgorgua.sharepoint.com/'
username_O365 = 'c2hwYWtAYXN0cmVsbGEuY29tLnVh'
password_O365 = 'MzNHamhuY2J1Zmhm'
site_O365_path = 'https://rgorgua.sharepoint.com/sites/astrella/'
shared_dir_path = 'Shared Documents/ИТ Служба/BackUps/Astrella/1C_UTP/'
local_dir_path = '//10.123.11.10/DB_backups/astrella/'
# remote_dir_path = ''

local_utils.net_copy()

sp_utils.copy_to_sp(tenant=tenant_O365,
                    username=username_O365,
                    password=password_O365,
                    site_o365=site_O365_path,
                    shared_folder=shared_dir_path,
                    local_folder=local_dir_path)
