import dropbox
class TransferData :
    def __init__(self,access_token):
        self.access_token=access_token

    def UploadFiles(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.AwiDT9IIyApIdYpt9bkKjzia2C9o4fIk9BNsqEL4patElbnYDBDX1_OrdcKyDtjk1ZPI26cXe2IoFTNCFwu46ZDATFsQ-En0G-o0e_g_OFJjvXRPGV7VhSyGdpj6IIX-8GfgURo"
    transferData=TransferData(access_token)

    file_from=input("enter the file paths to transfer: ")
    file_to=input("enter the full path to upload to dropbox: ")

    transferData.UploadFiles(file_from,file_to)
    print("file has been moved")

main()
