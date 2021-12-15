#include "eyediagram.h"
#include "ui_eyediagram.h"

eyediagram::eyediagram(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::eyediagram)
{
    ui->setupUi(this);
}

eyediagram::~eyediagram()
{
    delete ui;
}
