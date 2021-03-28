import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.At38MEuadeGAU1I1Ppye907DjYEr0UB6-9vX-IKR-U1f7R-9kcHhBapNiihtzSEFBmwmDEx9F3_tip0gBNoptqjc5g8UtoP51VjvuHWWfk0wcfsPIPrGsUSgJFMv4PVRyUkYYIM'
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to upload: ")
    transferData.upload_file(file_from,file_to)
    print("file has been move !!!")

main()