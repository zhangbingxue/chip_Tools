#include "serdesloop.h"
#include "ui_serdesloop.h"

serdesloop::serdesloop(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::serdesloop)
{
    ui->setupUi(this);
}

serdesloop::~serdesloop()
{
    delete ui;
}
