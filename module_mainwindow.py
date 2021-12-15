import logging
from datetime import datetime
from time import sleep

# from image import image
import qtawesome
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QMenu, QAction, QComboBox, QDoubleSpinBox, QLabel
from module_eyePic import eyeDiagram
from module_Drawning import Module_Drawning
from module_connect import Module_connect
from module_connect import SshClient
from tools7900.mainwindow import Ui_MainWindow


class module_mainwindow(QMainWindow):
    def __init__(self):
        super(module_mainwindow, self).__init__()
        self.combox_dfe_cc = {}  # 存放所有的dfe_cc_combox对象
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()  # 最大化显示
        self.dfe_flag = True  # 用来防止重置时候，触发combox_currentIndexChanged内置信号导致异常
        self.dfe_cc_combox = ['N', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                              '13']  # 初始化时候各个cc可选的载波号
        self.dfe_msps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 初始化时候各个通道内的Msps总和都为0
        self.ant_dfe = []
        self.__initUi()
        self.ip = ''  # 芯片的ip地址
        self.sshclient = None
        self.flag_connect = False  # 连接状态标志

    def __initUi(self):
        """初始化界面控件以及信号和槽连接"""
        # 增加左上角logo图标
        self.setWindowIcon(QIcon(':/ICT.png'))
        self.initDfeSingal()  # 初始化信号和槽连接
        self.initAntSingal()
        self.paintA = Module_Drawning()  # 实例化绘图widget,DFE和cc之间的连线
        self.paintA.ccModule = True
        self.ui.verticalLayout.addWidget(self.paintA)
        self.paintB = Module_Drawning()  # 实例化绘图widget,DFE和ANT之间的连线
        self.paintB.antModule = True
        self.ui.verticalLayout_2.addWidget(self.paintB)
        self.ui.treeWidget.expandAll()  # 设置展开所有树
        self.ui.statusbar.addPermanentWidget(self.ui.progressBar_dfe, 1)  # statusbar添加固定控件progressbar
        pix = QPixmap(':/DFE.png')
        self.ui.label_sys.setPixmap(pix)
        self.ui.progressBar_dfe.setVisible(False)  # 初始化时设置不可见
        self.ui.tableWidget.setSpan(0, 0, 1, 2)  # 合并单元格
        self.ui.tableWidget_3.setSpan(0, 0, 1, 2)
        self.ui.tableWidget.setCellWidget(1, 1, self.ui.lineEdit_width)  # 单元格添加控件
        self.ui.tableWidget.setCellWidget(2, 1, self.ui.comboBox_compress)
        self.ui.tableWidget_3.setCellWidget(1, 1, self.ui.comboBox_jesd)
        self.ui.tableWidget_3.setCellWidget(2, 1, self.ui.comboBox_Rf0)
        self.ui.tableWidget_3.setCellWidget(3, 1, self.ui.comboBox_Rf1)
        self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # 打开右键菜单的策略
        self.ui.treeWidget.customContextMenuRequested.connect(self.treeWidgetItem_menu)  # 绑定事件
        self.connectDialog = Module_connect()
        self.connectDialog.ui.buttonBox.accepted.connect(self.set_connect)

    def set_connect(self):
        """更改ip属性,建立ssh客户端连接"""
        self.ip = self.connectDialog.ui.lineEdit.text()
        try:
            self.sshclient = None
            self.sshclient = SshClient(self.ip)  # 创建SSH客户端
            self.flag_connect = True
            QMessageBox.information(self, '提示', '连接成功')
            logging.info('连接成功')
        except Exception as E:
            QMessageBox.information(self, '提示', f'连接异常：{E}')
            logging.error(f"{E}")

    @pyqtSlot()
    def on_btnEyeBuild_clicked(self):
        """眼图生成槽函数"""
        if self.flag_connect and self.sshclient is not None:
            b_type = self.ui.comboBox_type.currentIndex()
            c_lane = self.ui.comboBox_lane.currentIndex()
            fileName = f"eyedata_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
            eyeBuildMsg = f"idbg -a serdes_eye -b {str(b_type)} -c {str(c_lane)} -f {fileName}"
            try:
                msg = self.sshclient.send_msg(eyeBuildMsg)
                logging.info(msg)
                self.sshclient.get_file(localPath=f'./data/{fileName}', remotePath=f'/lib/firmware/eyedata.xlsx')
                self.ui.statusbar.showMessage(f"{datetime.now().strftime('%Y/%m/%d-%H:%M:%S')}:眼图已下载-{fileName}")
                eyeDiagram(fileName=f'./data/{fileName}')
            except Exception as e:
                QMessageBox.information(self, '错误提示', f'{e}')
                logging.error(f"{e}")
        else:
            QMessageBox.information(self,'提示','请配置连接')

    @pyqtSlot()
    def on_actionconnect_triggered(self):
        """弹出ip配置界面"""
        self.connectDialog.exec_()

    def treeWidgetItem_menu(self, pos):
        """定义点击treewidget中item生成菜单界面"""
        item = self.ui.treeWidget.itemAt(pos)
        if item != None and item.text(0) == '配置':
            rightmenu = QMenu()
            action1 = QAction(qtawesome.icon('fa.play', color="green"), '下发配置', rightmenu)
            action1.triggered.connect(self.dfe_config_upload)
            action2 = QAction(qtawesome.icon('fa.refresh', color="red"), '重新配置', rightmenu)
            action2.triggered.connect(self.dfe_config_reset)  # 菜单子按钮连接重配
            rightmenu.addAction(action1)
            rightmenu.addAction(action2)
            rightmenu.exec_(QCursor.pos())

    def dfe_config_upload(self):
        """DFE界面所有参数下发"""
        self.ui.progressBar_dfe.setVisible(True)
        self.ui.progressBar_dfe.setValue(20)
        sleep(0.5)
        self.ui.progressBar_dfe.setValue(60)
        sleep(0.5)
        self.ui.progressBar_dfe.setValue(80)
        sleep(0.5)
        self.ui.progressBar_dfe.setVisible(False)
        self.ui.statusbar.showMessage(f"{datetime.now().strftime('%Y/%m/%d-%H:%M:%S')}:  DFE配置下发成功")

    def dfe_config_reset(self):
        """DFE界面参数恢复成默认"""
        self.dfe_flag = False
        for i in range(10):
            for j in range(3):  # 遍历dfe各个子通道box，回复可用状态，并清除其中的下拉选项，再重置默认下拉选项
                item = self.findChild(QComboBox, f'comboBox_dfe{i}CC{j}')
                item.setEnabled(True)
                item.clear()
                item.addItems(self.dfe_cc_combox)
                self.combox_dfe_cc[item] = True
        for i in range(2):
            for j in range(4):
                item = self.findChild(QComboBox, f'comboBox_rf{i}ant{j}')
                item.setCurrentText('N')
        self.dfe_flag = True
        self.dfe_msps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.updata_DfeMsps()

    def on_treeWidget_itemClicked(self, item):
        """树控件点击信号绑定stackwidget的index"""
        if item.text(0) == '芯片架构':
            self.ui.stackedWidget.setCurrentIndex(2)
        if item.text(0) == '配置':
            self.ui.stackedWidget.setCurrentIndex(0)
        if item.text(0) == '测试分析':
            self.ui.stackedWidget.setCurrentIndex(3)

    def updata_DfeMsps(self):
        """1,获取当前不是显示N的combox控件，获取对应的doublespin数值，
        同一通道相加判断是否超过122.88
           2,进行绘图控件repaint操作"""
        draw_point = []
        for i in range(10):
            dfe_msps_cc = [0, 0, 0]
            for j in range(3):
                item = self.findChild(QComboBox, f'comboBox_dfe{i}CC{j}')  # 根据combox的名称进行遍历
                if item.currentText() != 'N':
                    itemcc = self.findChild(QDoubleSpinBox, f'doubleSpinBox_C{item.currentText()}')
                    # itemcc.setEnabled(False)
                    dfe_msps_cc[j] = float(itemcc.text())
                    draw_point.append([i, j, int(item.currentText())])  # 遍历需要连接的按钮
            self.dfe_msps[i] = sum(dfe_msps_cc)  # 计算同个DFE通道内CC——msps的总和
            if self.dfe_msps[i] > 122.88:
                QMessageBox.information(self, '配置提示', f'DFE通道【{i}】MSPS总和超过122.88 ！请进行调整')

        for i in range(10):
            item = self.findChild(QLabel, f'label_Mspsdfe{i}')
            item.setText("{:.2f}".format(self.dfe_msps[i]))

        self.paintA.list = draw_point  # 改变对象的画图属性
        self.paintA.repaint()  # 重新绘制cc和dfe_cc之间的连线


    def initDfeSingal(self):
        """将所有的dfecc绑定槽函数change_dfe_combox"""
        for i in range(10):
            for j in range(3):
                item = self.findChild(QComboBox, f'comboBox_dfe{i}CC{j}')  # 根据combox的名称进行遍历
                item.currentIndexChanged[int].connect(self.change_dfe_combox)  # 将信号和槽连接
                self.combox_dfe_cc[item] = True  # 生成对应的键值对


    def change_dfe_combox(self, msg):
        """遍历所有的dfecc，删除已被选择的comboxindex"""
        if self.dfe_flag:
            self.updata_DfeMsps()
            dfe_cc_box = self.sender()  # 获取发送信号的控件对象
            self.combox_dfe_cc[dfe_cc_box] = False
            dfe_cc_box.setEnabled(False)
            for item in self.combox_dfe_cc:
                if self.combox_dfe_cc[item]:
                    item.removeItem(msg)

    def initAntSingal(self):
        """将天线ant的combox信号连接到槽函数antToDfechannel"""
        for i in range(2):
            for j in range(4):
                item = self.findChild(QComboBox, f'comboBox_rf{i}ant{j}')  # 根据combox的名称进行遍历
                item.currentTextChanged[str].connect(self.antToDfechannel)

    @pyqtSlot(str)
    def antToDfechannel(self, msg):
        """1，判断dfe通道是否已经配置
        2，遍历rf天线combox当前数值，进行绘图控件repaint操作"""
        tmp_list = []
        tmp_list1 = []
        if msg in self.ant_dfe:
            self.sender().setCurrentText('N')
            QMessageBox.information(self, '提示', f'DFE通道【{msg}】已配置天线')
            return
        for i in range(2):
            for j in range(4):
                item = self.findChild(QComboBox, f'comboBox_rf{i}ant{j}')  # 根据combox的名称进行遍历
                if item.currentText() != 'N':
                    tmp_list.append(item.currentText())
                    tmp_list1.append([i, j, item.currentText()])
        self.ant_dfe = tmp_list
        self.paintB.list = tmp_list1  # 改变对象的画图属性
        self.paintB.repaint()  # 重新绘制ant和dfe之间的连线

    @pyqtSlot(int)
    def on_comboBox_Rf0_currentIndexChanged(self, msg):
        """RF 0天线配置combox 槽函数操作
        1，根据天线配置进行控件隐藏
        2，控件默认恢复显示N"""
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
    def on_comboBox_Rf1_currentIndexChanged(self, msg):
        """RF 1天线配置combox 槽函数操作
        1，根据天线配置进行控件隐藏
        2，控件默认显示N操作"""
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
    def on_actionAbout_triggered(self):
        """弹窗显示软件版权信息"""
        QMessageBox.about(self, "版权信息",
                          """Copyright 2021 @创芯慧联 zhangbingxue"""
                          )
