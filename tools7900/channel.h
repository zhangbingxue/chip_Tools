#ifndef CHANNEL_H
#define CHANNEL_H

#include <QWidget>

namespace Ui {
class channel;
}

class channel : public QWidget
{
    Q_OBJECT

public:
    explicit channel(QWidget *parent = nullptr);
    ~channel();

private:
    Ui::channel *ui;
};

#endif // CHANNEL_H
