#include "channel.h"
#include "ui_channel.h"

channel::channel(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::channel)
{
    ui->setupUi(this);
}

channel::~channel()
{
    delete ui;
}
