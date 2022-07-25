from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io
import os

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/Users/user/Documents/make-cribs/makecribs-db3a28935e7b.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

folder_id = '1GWArUb9GIuI8OdS6dd9CFl8PODe3zjv8'
name = 'file.docx'
file_path = '/Users/user/Documents/make-cribs/file.docx'
file_metadata = {
                'name': name,
                'parents': [folder_id]
            }
media = MediaFileUpload(file_path, resumable=True)
r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
pp.pprint(r)

results = service.files().list(pageSize=10,
                               fields="nextPageToken, files(id, name, mimeType)").execute()

file_id = r['id']
request = service.files().get_media(fileId=file_id)
filename = os.getcwd() + '/result/file.docx'
fh = io.FileIO(filename, 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
