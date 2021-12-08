#ifndef RF_H
#define RF_H

#include <QWidget>

namespace Ui {
class rf;
}

class rf : public QWidget
{
    Q_OBJECT

public:
    explicit rf(QWidget *parent = nullptr);
    ~rf();

private:
    Ui::rf *ui;
};

#endif // RF_H
