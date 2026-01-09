from ftplib import FTP

host="asdfghj"
user="qwertyuiop"
password="qwertyuiop"

with FTP(host) as ftp:
    ftp.login(user=user, password=password)
    print(ftp.getwelcome())

    with open('test.txt','wb') as f:
        ftp.retrbinary("RETR"+"mytest.txt",f.write,1024)
    ftp.quit()
    