#ifndef SSHCONSOLE_H
#define SSHCONSOLE_H

#include <QWidget>

namespace Ui {
class sshconsole;
}

class sshconsole : public QWidget
{
    Q_OBJECT

public:
    explicit sshconsole(QWidget *parent = nullptr);
    ~sshconsole();

private slots:
    void on_lineEdit_returnPressed();

private:
    Ui::sshconsole *ui;
};

#endif // SSHCONSOLE_H
