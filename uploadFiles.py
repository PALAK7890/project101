import dropbox
import os


class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,files_to,files_from,local_path,dropbox_path,relative_path,WriteMode):
        dbx = dropbox.Dropbox(self.access_token)
        
        for root,dirs, files in os.walk(files_from):
            relative_path=os.path .realpath(local_path,files_from)
            dropbox_path=os.path.join(files_to,relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))

    
def main():
    access_token = 'sl.Bof9nlMmhvrn6pHmZ8f4i68ciqnBTk-X2E9IlYrSdjdSsfkqNFcUiy1SzLUpm8DTFCqGo4Twf4ez43nKMoF4IuMKsWHN0t7VFjMeNSzmEL8oCH1JpWzo5m_iXt_opcxVr2w_1e8FO6nW'
    transferData = TransferData(access_token)


    file_from = input('enter the path to file to be uploaded: ')
    file_to = input('enter the path where the file should be upload :')


   
    transferData.upload_file(file_from, file_to)


if __name__ == '__main__':
    main()
