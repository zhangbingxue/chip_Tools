import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication
from paramiko import Transport, SFTPClient, SSHClient, AutoAddPolicy

from tools7900.connect import Ui_connect
class Module_connect(QDialog):
    """连接配置对话框"""
    def __init__(self):
        super(Module_connect, self).__init__()
        self.ui = Ui_connect()
        self.ui.setupUi(self)
        self.__initUi()

    def __initUi(self):
        """初始化UI组件"""
        # 增加左上角logo图标
        self.setWindowIcon(QIcon(':/ICT.png'))
        self.ui.lineEdit.setInputMask("000.000.000.000;")


class SshClient():
    """生成ssh客户端"""
    def __init__(self, ip,port=22,username='root', pwd='BlTf128'):
        self._ip = ip
        self._port = port
        self._username = username
        self._pwd = pwd
        self.ssh = None
        self._sftp = None
        self.connect()

    def connect(self):
        """建立ssh，sftp连接"""
        self.ssh = SSHClient()
        key = AutoAddPolicy()
        self.ssh.set_missing_host_key_policy(key)
        self.ssh.connect(self._ip, self._port,self._username, self._pwd, timeout=1.5)
        trans = Transport((self._ip, self._port))
        trans.connect(username=self._username, password=self._pwd)
        self._sftp = SFTPClient.from_transport(trans)
        self.shell = self.ssh.invoke_shell()

    def send_msg(self, msg):
        """通过ssh客户端发送消息"""
        sdin, stdout, stderr = self.ssh.exec_command(msg)
        for i in stdout:
            return i

    def send_msg1(self, msg):
        """交互式ssh客户端发送字符串"""
        self.shell.send(msg + '\n')

    def get_file(self, localPath='./data/1.yaml', remotePath='/lib/fireware'):
        """通过sftp从远程路径拷贝到本地路径"""
        if self._sftp is None:
            return
        self._sftp.get(remotePath, localPath)

    def put_file(self, localPath='./data/eyedata.xlsx', remotePath='/lib/firmware/eyedata.xlsx'):
        """通过sftp从本地路径拷贝到远程路径"""
        if self._sftp is None:
            return
        self._sftp.put(localPath, remotePath)

    def close(self):
        """关闭ssh以及sftp连接"""
        if self.ssh is not None:
            self._sftp.close()
            self.ssh.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Module_connect()
    win.show()
    sys.exit(app.exec_())
