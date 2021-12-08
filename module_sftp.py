# import threading
# from time import sleep
import logging
from paramiko import Transport,SFTPClient
class Sftp_Client():
    def __init__(self,ip='192.168.2.53',username='root',pwd='BlTf128'):
        self.ip = ip
        self.user = username
        self.passwd = pwd
        try:
            self.sf = Transport((ip, 22))
            self.sf.connect(username=self.user, password=self.passwd)
            self.sftp = SFTPClient.from_transport(self.sf)
        except Exception as e:
            logging.error(e)

    def getFile(self,localPath='./data/1.yaml',remotePath='/lib/fireware'):
        self.sftp.get(remotePath,localPath)

    def putFile(self,localPath='./data/eyedata.xlsx',remotePath='/lib/firmware/eyedata.xlsx'):
        self.sftp.put(localPath,remotePath)

    def close(self):
        self.sf.close()