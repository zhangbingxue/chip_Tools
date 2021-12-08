#include "rf.h"
#include "ui_rf.h"

rf::rf(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::rf)
{
    ui->setupUi(this);
}

rf::~rf()
{
    delete ui;
}
