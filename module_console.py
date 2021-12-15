import sys
import threading

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
from image import image
from tools7900.sshconsole import Ui_sshconsole
from module_connect import SshClient

class Module_console(QWidget):
    """console客户端"""
    infoMsgPrint = pyqtSignal(str)
    def __init__(self,ip='192.168.2.53',port=22,username='root',pwd='BlTf128'):
        super(Module_console, self).__init__()
        self.ui = Ui_sshconsole()
        self.ui.setupUi(self)
        self.ip = ip
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__initui()
        self.__initSsh()

    def __initui(self):
        # 增加左上角logo图标
        self.setWindowIcon(QIcon(':/ICT.png'))
        self.infoMsgPrint.connect(self.information_print)

    def __initSsh(self):
        """初始化ssh连接，生成实例"""
        self.ssh = SshClient(username=self.username,ip=self.ip,pwd=self.pwd,port=self.port)
        thr1 = threading.Thread(target=self.output)
        thr1.setDaemon(True)
        thr1.start()

    @pyqtSlot()
    def on_lineEdit_returnPressed(self):
        """当lineEdit发送回车信号时的槽函数"""
        sshmsg = self.ui.lineEdit.text()
        self.ssh.send_msg1(sshmsg)
        self.ui.lineEdit.clear()

    def output(self):
        """循环获取shell客户端读取的字符串"""
        while True:
            try:
                res = self.ssh.shell.recv(512)
                res1 = str(res,encoding='utf-8')
                self.infoMsgPrint.emit(res1)
            except Exception as e:
                pass

    def information_print(self, mypstr):
        """输出信息到plaintext控件上"""
        try:
            self.ui.plainTextEdit.appendPlainText(mypstr)
        except Exception as e:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Module_console()
    win.show()
    sys.exit(app.exec_())