import sys
import serial.tools.list_ports
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from uipoject.portSetting_ui import Ui_serialSetting
from image import image
import qdarkstyle

class SerialSetting(QDialog,Ui_serialSetting):
    saveSigal = pyqtSignal(tuple,dict)  # 自定义一个传输dict信号管道
    def __init__(self,parent=None):
        super(SerialSetting, self).__init__(parent)
        self.ui = Ui_serialSetting()
        self.ui.setupUi(self)
        self.initUi()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initUi(self):
        # 增加左上角logo图标
        self.setWindowIcon(QIcon(':/ICT.png'))
        self.setAttribute(QtCore.Qt.WA_QuitOnClose, False)  # 设置伴随主窗口关闭
        self.ui.buttonBox.accepted.connect(self.serialCfgMsg)
        self.get_serials_name()# 初始化获取系统设备串口连接情况

    #获取界面组件内容并发送信号
    def serialCfgMsg(self):
        kwarg = {}
        port_name = self.ui.comBx_PortName.currentText()
        baud = int(self.ui.comBx_BaudRate.currentText())
        kwarg['parities'] = self.ui.comBx_Parities.currentText()
        kwarg['bytesize'] = int(self.ui.comBx_ByteSize.currentText())
        kwarg['stopbits'] = int(self.ui.comBx_StopBits.currentText())
        if port_name == '':
            QMessageBox.information(self,'提示','未配置有效端口号')
            return
        args = (port_name,baud)
        self.saveSigal.emit(args,kwarg)

    # 获取当前设备连接的COM列表
    def get_serials_name(self):
        ports_get = list(serial.tools.list_ports.comports())
        port_list = []
        if len(ports_get) == 0:
            QMessageBox.information(self,'提示',"错误提示,找不到串口\n")
            return
        for i in range(0, len(ports_get)):
            port = (ports_get[i])
            port_list.append(port[0])
        port_list.sort()
        self.ui.comBx_PortName.addItems(port_list)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    serialUi = SerialSetting()
    serialUi.show()
    sys.exit(myapp.exec_())