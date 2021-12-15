#include "sshconsole.h"
#include "ui_sshconsole.h"

sshconsole::sshconsole(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::sshconsole)
{
    ui->setupUi(this);
}

sshconsole::~sshconsole()
{
    delete ui;
}

void sshconsole::on_lineEdit_returnPressed()
{

}

