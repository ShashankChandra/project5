import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFON-ZjXy0qYmtk4NnHeF6BfvDKqP-Jfy7rn2XczOj_Nmz7e3pQS_DYtRbfDReL2FIdxEVaT6j5bos_17IbtvIvH_93k1rilRfjuKzv95SthEF3eIKqs3GYM_uTn_CimAQELE9DL7vg'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()