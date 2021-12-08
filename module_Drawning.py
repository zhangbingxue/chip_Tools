import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import (QPainter, QPen,QPolygon)
from tools7900.paint import Ui_paint

class Module_Drawning(QWidget):
    def __init__(self):
        super(Module_Drawning, self).__init__()
        self.ui = Ui_paint()
        self.ui.setupUi(self)
        self.list = []
        self.ccModule = False
        self.antModule = False

    ##  ==================event处理函数=================================
    def paintEvent(self, event):  # 在窗口上绘图
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        # 设置画笔
        pen = QPen()
        pen.setWidth(3)  # 线宽
        ## Qt::NoPen,Qt::SolidLine, Qt::DashLine, Qt::DotLine,Qt::DashDotLine,Qt::DashDotDotLine,Qt::CustomDashLine
        pen.setStyle(Qt.SolidLine)  # 线的类型，实线、虚线等
        ## Qt::FlatCap, Qt::SquareCap,Qt::RoundCap
        pen.setCapStyle(Qt.RoundCap)  # 线端点样式
        ## Qt::MiterJoin,Qt::BevelJoin,Qt::RoundJoin,Qt::SvgMiterJoin
        pen.setJoinStyle(Qt.RoundJoin)  # 线的连接点样式
        W = self.width()  # 绘图区宽度
        H = self.height()  # 绘图区高度
        if self.list == '':
            return
        if self.ccModule:
            pen.setColor(Qt.darkGray)  # 划线颜色
            painter.setPen(pen)
            for i in self.list:
                points = [QPoint(0, (9.5+i[2])*H / 36.5),
                          QPoint(40, (9.5+i[2])*H / 36.5),
                          QPoint(W-40, (0.5+i[0]*3+i[1]) *H / 36.5),
                          QPoint(W, (0.5+i[0]*3+i[1])* H/36.5)]
                painter.drawPolyline(QPolygon(points))
        if self.antModule:
            pen.setColor(Qt.darkGray)  # 划线颜色
            painter.setPen(pen)
            for i in self.list:
                if i[0] == 0:
                    points = [QPoint(0, H / 12),
                              QPoint(40, H / 12),
                              QPoint(W-40,  i[1]*20+190),
                              QPoint(W,i[1]*20+190)]
                if i[0] == 1:
                    points = [QPoint(0, H / 12),
                              QPoint(40, H / 12),
                              QPoint(W - 40, i[1] * 20 + 460),
                              QPoint(W, i[1] * 20 + 460)]
                painter.drawPolyline(QPolygon(points))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Module_Drawning()
    win.show()
    sys.exit(app.exec_())
