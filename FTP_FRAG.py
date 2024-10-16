import ftplib

def FRAG_FTP():
    try:
        host = ''
        username = ''
        password = ''

        # Path to the file to upload (replace with your file path)
        file_to_upload = ''

        # The name to save the file as on the FTP server
        remote_file_name = ''

        # Directory on the FTP server where the file should be uploaded
        remote_directory = ''  # Change to the desired folder name
        # Establish FTP connection
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        print(f"Connected to {host}")

        # Change to the desired directory on the FTP server
        ftp.cwd(remote_directory)
        print(f"Changed to directory: {remote_directory}")

        # Open the file in binary mode
        with open(file_to_upload, 'rb') as file:
            # Use STOR command to upload the file to the specified directory
            ftp.storbinary(f'STOR {remote_file_name}', file)

        print(f"File '{file_to_upload}' uploaded successfully as '{remote_file_name}' in '{remote_directory}' directory")

        # Close the connection
        ftp.quit()

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

if __name__=="__main__":
    # FTP server details
    ftp_host = ''
    ftp_user = ''
    ftp_pass = ''

    # Path to the file to upload (replace with your file path)
    file_to_upload = ''

    # The name to save the file as on the FTP server
    remote_file_name = ''

    # Directory on the FTP server where the file should be uploaded
    remote_directory = ''  # Change to the desired folder name

    # Call the function to upload the file to the specified folder
    FRAG_FTP()
