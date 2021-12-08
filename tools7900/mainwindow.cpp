#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}



void MainWindow::on_doubleSpinBox_valueChanged(double arg1)
{

}


void MainWindow::on_pushButton_clicked()
{

}


void MainWindow::on_comboBox_5_currentTextChanged(const QString &arg1)
{

}


void MainWindow::on_comboBox_Rf0_currentTextChanged(const QString &arg1)
{

}


void MainWindow::on_comboBox_dfe0CC0_currentIndexChanged(int index)
{

}


void MainWindow::on_comboBox_Rf1_currentIndexChanged(int index)
{

}


void MainWindow::on_comboBox_rf0ant0_currentTextChanged(const QString &arg1)
{

}

