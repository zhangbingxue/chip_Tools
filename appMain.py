import sys
from module_busy import GifSplashScreen  # 初始化界面
from module_mainwindow import module_mainwindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = GifSplashScreen()  # 实例化初始化界面
    splash.show()  # 初始化界面显示
    splash.showMessage('初始化中', Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
    # from module_eyePic import eyeDiagram  # matplot组件加载时间较长2s左右，放在这里提示加载情况
    mainform = module_mainwindow()
    splash.showMessage('组件加载完成', Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
    mainform.show()
    splash.finish(mainform)
    sys.exit(app.exec_())