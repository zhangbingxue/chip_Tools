#ifndef EYEDIAGRAM_H
#define EYEDIAGRAM_H

#include <QWidget>

namespace Ui {
class eyediagram;
}

class eyediagram : public QWidget
{
    Q_OBJECT

public:
    explicit eyediagram(QWidget *parent = nullptr);
    ~eyediagram();

private:
    Ui::eyediagram *ui;
};

#endif // EYEDIAGRAM_H
