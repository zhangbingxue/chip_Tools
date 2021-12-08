from tools7900.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon,QPixmap
from module_Drawning import Module_Drawning

# from module_serialSetting import SerialSetting
# from module_sftp import Sftp_Client

class module_mainwindow(QMainWindow):
    def __init__(self):
        super(module_mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dfe_flag = True #用来防止重置时候，触发combox_currentIndexChanged内置信号导致异常
        self.dfe_cc_combox = ['N','1','2','3','4','5','6','7','8','9','10','11','12','13'] #初始化时候各个cc可选的载波号
        self.dfe_msps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #初始化时候各个通道内的Msps总和都为0
        self.ant_dfe = []
        self.connectFlag = '未连接'
        self.__initUi()

    def __initUi(self):
        # 增加左上角logo图标
        self.setWindowIcon(QIcon(':/ICT.png'))
        self.initDfeSingal()
        self.initAntSingal()
        self.paintA = Module_Drawning()
        self.paintA.ccModule = True
        self.ui.verticalLayout.addWidget(self.paintA)
        self.paintB = Module_Drawning()
        self.paintB.antModule = True
        self.ui.verticalLayout_2.addWidget(self.paintB)
        self.ui.treeWidget.expandAll()  # 设置展开所有树
        statusLabel = QLabel('测试平台： ')
        statusLabel.setStyleSheet("font: 75 10pt '黑体';")
        statusLabel_1 = QLabel()
        statusLabel_1.setObjectName('showStatus')
        statusLabel_1.setText(self.connectFlag)
        statusLabel_1.setStyleSheet("font: 75 10pt '黑体';background-color: rgb(255, 134, 162);")
        self.ui.statusbar.addWidget(statusLabel)
        self.ui.statusbar.addWidget(statusLabel_1)
        pix = QPixmap(':/DFE.png')
        self.ui.label_sys.setPixmap(pix)

    def on_treeWidget_itemClicked(self, item):
        if item.text(0) == '芯片架构':
            self.ui.stackedWidget.setCurrentIndex(2)
        if item.text(0) == 'DFE':
            self.ui.stackedWidget.setCurrentIndex(0)

    def updata_DfeMsps(self):
        draw_point=[]
        for i in range(10):
            dfe_msps_cc = [0, 0, 0]
            for j in range(3):
                item = self.findChild(QComboBox,f'comboBox_dfe{i}CC{j}') #根据combox的名称进行遍历
                if item.currentText() != 'N':
                    itemcc = self.findChild(QDoubleSpinBox, f'doubleSpinBox_C{item.currentText()}')
                    # itemcc.setEnabled(False)
                    dfe_msps_cc[j] = float(itemcc.text())
                    draw_point.append([i,j,int(item.currentText())]) #遍历需要连接的按钮
            self.dfe_msps[i] = sum(dfe_msps_cc) #计算同个DFE通道内CC——msps的总和
            if self.dfe_msps[i]  > 122.88:
                QMessageBox.information(self,'配置提示',f'DFE通道【{i}】MSPS总和超过122.88 ！请进行调整')

        for i in range(10):
            item = self.findChild(QLabel, f'label_Mspsdfe{i}')
            item.setText("{:.2f}".format(self.dfe_msps[i]))

        self.paintA.list = draw_point #改变对象的画图属性
        self.paintA.repaint() #重新绘制cc和dfe_cc之间的连线

    #将所有的dfecc绑定槽函数change_dfe_combox
    def initDfeSingal(self):
        self.combox_dfe_cc = {} #存放所有的dfe_cc_combox对象
        for i in range(10):
            for j in range(3):
                item = self.findChild(QComboBox,f'comboBox_dfe{i}CC{j}') #根据combox的名称进行遍历
                item.currentIndexChanged[int].connect(self.change_dfe_combox) #将信号和槽连接
                self.combox_dfe_cc[item]=True #生成对应的键值对

    #遍历所有的dfecc，删除已被选择的comboxindex
    def change_dfe_combox(self,msg):
        if self.dfe_flag:
            self.updata_DfeMsps()
            dfe_cc_box = self.sender() #获取发送信号的控件对象
            self.combox_dfe_cc[dfe_cc_box] = False
            dfe_cc_box.setEnabled(False)
            for item in self.combox_dfe_cc:
                if self.combox_dfe_cc[item]:
                    item.removeItem(msg)

    def initAntSingal(self):
        for i in range(2):
            for j in range(4):
                item = self.findChild(QComboBox,f'comboBox_rf{i}ant{j}') #根据combox的名称进行遍历
                item.currentTextChanged[str].connect(self.antToDfechannel)

    @pyqtSlot(str)
    def antToDfechannel(self,msg):
        tmp_list = []
        tmp_list1 = []
        if msg in self.ant_dfe:
            self.sender().setCurrentText('N')
            QMessageBox.information(self, '提示', f'DFE通道【{msg}】已配置天线')
            return
        for i in range(2):
            for j in range(4):
                item = self.findChild(QComboBox,f'comboBox_rf{i}ant{j}') #根据combox的名称进行遍历
                if item.currentText() != 'N':
                    tmp_list.append(item.currentText())
                    tmp_list1.append([i,j,item.currentText()])
        self.ant_dfe = tmp_list
        self.paintB.list = tmp_list1 #改变对象的画图属性
        self.paintB.repaint() #重新绘制ant和dfe之间的连线

    @pyqtSlot(int)
    def on_comboBox_Rf0_currentIndexChanged(self,msg):
        self.ui.comboBox_rf0ant2.setVisible(True)
        self.ui.comboBox_rf0ant3.setVisible(True)
        for j in range(4):
            item = self.findChild(QComboBox, f'comboBox_rf0ant{j}')
            item.setCurrentText('N')
        if msg == 1:
            self.ui.comboBox_rf0ant2.setVisible(False)
            self.ui.comboBox_rf0ant3.setVisible(False)
        if msg == 0:
            self.ui.comboBox_rf0ant2.setVisible(True)
            self.ui.comboBox_rf0ant3.setVisible(True)

    @pyqtSlot(int)
    def on_comboBox_Rf1_currentIndexChanged(self,msg):
        self.ui.frame_5.setVisible(True)
        self.ui.comboBox_rf1ant2.setVisible(True)
        self.ui.comboBox_rf1ant3.setVisible(True)
        for j in range(4):
            item = self.findChild(QComboBox, f'comboBox_rf1ant{j}')
            item.setCurrentText('N')
        if msg == 2:
            self.ui.frame_5.setVisible(False)
        if msg == 1:
            self.ui.comboBox_rf1ant2.setVisible(False)
            self.ui.comboBox_rf1ant3.setVisible(False)
        if msg == 0:
            self.ui.comboBox_rf1ant2.setVisible(True)
            self.ui.comboBox_rf1ant3.setVisible(True)

    @pyqtSlot()
    def on_pushButton_reset_clicked(self):
        self.dfe_flag = False
        for i in range(10):
            for j in range(3):#遍历dfe各个子通道box，回复可用状态，并清除其中的下拉选项，再重置默认下拉选项
                item = self.findChild(QComboBox,f'comboBox_dfe{i}CC{j}')
                item.setEnabled(True)
                item.clear()
                item.addItems(self.dfe_cc_combox)
                self.combox_dfe_cc[item] = True
        for i in range(2):
            for j in range(4):
                item = self.findChild(QComboBox,f'comboBox_rf{i}ant{j}')
                item.setCurrentText('N')
        self.dfe_flag = True
        self.dfe_msps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.updata_DfeMsps()


    # 软件版权信息
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        QMessageBox.about(self, "版权信息",
                          """Copyright 2021 @创芯慧联 zhangbingxue"""
                          )
