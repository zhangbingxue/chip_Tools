#ifndef SERDESLOOP_H
#define SERDESLOOP_H

#include <QWidget>

namespace Ui {
class serdesloop;
}

class serdesloop : public QWidget
{
    Q_OBJECT

public:
    explicit serdesloop(QWidget *parent = nullptr);
    ~serdesloop();

private:
    Ui::serdesloop *ui;
};

#endif // SERDESLOOP_H
