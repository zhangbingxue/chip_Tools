#include "connect.h"
#include "ui_connect.h"

connect::connect(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::connect)
{
    ui->setupUi(this);
}

connect::~connect()
{
    delete ui;
}
