#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();


private slots:
    void on_doubleSpinBox_valueChanged(double arg1);

    void on_pushButton_clicked();

    void on_comboBox_5_currentTextChanged(const QString &arg1);

    void on_comboBox_Rf0_currentTextChanged(const QString &arg1);

    void on_comboBox_dfe0CC0_currentIndexChanged(int index);

    void on_comboBox_Rf1_currentIndexChanged(int index);

    void on_comboBox_rf0ant0_currentTextChanged(const QString &arg1);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
