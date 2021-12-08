#include "paint.h"
#include "ui_paint.h"

paint::paint(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::paint)
{
    ui->setupUi(this);
}

paint::~paint()
{
    delete ui;
}
