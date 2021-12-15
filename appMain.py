import os
import sys
from module_busy import GifSplashScreen  # 初始化界面
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from yaml import load, FullLoader
import logging.config

def setup_logging(default_path="./config/logging.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    """设置软件log输出格式以及log等级"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = load(f.read(), Loader=FullLoader)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == '__main__':
    setup_logging()  # 设置logging配置
    app = QApplication(sys.argv)
    splash = GifSplashScreen()  # 实例化初始化界面
    splash.show()  # 初始化界面显示
    splash.showMessage('初始化中', Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
    from module_mainwindow import module_mainwindow
    mainform = module_mainwindow()
    splash.showMessage('组件加载完成', Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
    mainform.show()
    splash.finish(mainform)
    sys.exit(app.exec_())