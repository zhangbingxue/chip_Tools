#ifndef CONNECT_H
#define CONNECT_H

#include <QDialog>

namespace Ui {
class connect;
}

class connect : public QDialog
{
    Q_OBJECT

public:
    explicit connect(QWidget *parent = nullptr);
    ~connect();

private:
    Ui::connect *ui;
};

#endif // CONNECT_H
