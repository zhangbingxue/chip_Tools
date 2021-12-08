#ifndef PAINT_H
#define PAINT_H

#include <QWidget>

namespace Ui {
class paint;
}

class paint : public QWidget
{
    Q_OBJECT

public:
    explicit paint(QWidget *parent = nullptr);
    ~paint();

private:
    Ui::paint *ui;
};

#endif // PAINT_H
