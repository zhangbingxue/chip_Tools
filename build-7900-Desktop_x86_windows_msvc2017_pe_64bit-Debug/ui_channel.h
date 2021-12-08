/********************************************************************************
** Form generated from reading UI file 'channel.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CHANNEL_H
#define UI_CHANNEL_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_channel
{
public:
    QHBoxLayout *horizontalLayout_4;
    QFrame *frame_2;
    QFrame *frame;
    QLabel *label;
    QComboBox *comboBox_dfeCC1;
    QComboBox *comboBox_dfeCC2;
    QFrame *frame_3;
    QLabel *label_3;
    QComboBox *comboBox_dfeCC2_2;
    QComboBox *comboBox_dfeCC1_2;
    QComboBox *comboBox_dfeCC0_2;
    QPushButton *pushButton;
    QComboBox *comboBox_dfeCC0;

    void setupUi(QWidget *channel)
    {
        if (channel->objectName().isEmpty())
            channel->setObjectName(QString::fromUtf8("channel"));
        channel->resize(301, 183);
        horizontalLayout_4 = new QHBoxLayout(channel);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        frame_2 = new QFrame(channel);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
        frame_2->setSizePolicy(sizePolicy);
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        frame = new QFrame(frame_2);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(30, 10, 131, 61));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy1);
        frame->setStyleSheet(QString::fromUtf8("background-color: rgb(105, 166, 184);"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        label = new QLabel(frame);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 10, 91, 16));
        comboBox_dfeCC1 = new QComboBox(frame_2);
        comboBox_dfeCC1->addItem(QString());
        comboBox_dfeCC1->addItem(QString());
        comboBox_dfeCC1->setObjectName(QString::fromUtf8("comboBox_dfeCC1"));
        comboBox_dfeCC1->setGeometry(QRect(0, 30, 31, 20));
        QSizePolicy sizePolicy2(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(comboBox_dfeCC1->sizePolicy().hasHeightForWidth());
        comboBox_dfeCC1->setSizePolicy(sizePolicy2);
        comboBox_dfeCC2 = new QComboBox(frame_2);
        comboBox_dfeCC2->addItem(QString());
        comboBox_dfeCC2->addItem(QString());
        comboBox_dfeCC2->setObjectName(QString::fromUtf8("comboBox_dfeCC2"));
        comboBox_dfeCC2->setGeometry(QRect(0, 50, 31, 20));
        sizePolicy2.setHeightForWidth(comboBox_dfeCC2->sizePolicy().hasHeightForWidth());
        comboBox_dfeCC2->setSizePolicy(sizePolicy2);
        frame_3 = new QFrame(frame_2);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setGeometry(QRect(30, 80, 131, 61));
        sizePolicy1.setHeightForWidth(frame_3->sizePolicy().hasHeightForWidth());
        frame_3->setSizePolicy(sizePolicy1);
        frame_3->setStyleSheet(QString::fromUtf8("background-color: rgb(105, 166, 184);"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        label_3 = new QLabel(frame_3);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(10, 10, 91, 16));
        comboBox_dfeCC2_2 = new QComboBox(frame_2);
        comboBox_dfeCC2_2->addItem(QString());
        comboBox_dfeCC2_2->addItem(QString());
        comboBox_dfeCC2_2->setObjectName(QString::fromUtf8("comboBox_dfeCC2_2"));
        comboBox_dfeCC2_2->setGeometry(QRect(0, 120, 31, 20));
        sizePolicy2.setHeightForWidth(comboBox_dfeCC2_2->sizePolicy().hasHeightForWidth());
        comboBox_dfeCC2_2->setSizePolicy(sizePolicy2);
        comboBox_dfeCC1_2 = new QComboBox(frame_2);
        comboBox_dfeCC1_2->addItem(QString());
        comboBox_dfeCC1_2->addItem(QString());
        comboBox_dfeCC1_2->setObjectName(QString::fromUtf8("comboBox_dfeCC1_2"));
        comboBox_dfeCC1_2->setGeometry(QRect(0, 100, 31, 20));
        sizePolicy2.setHeightForWidth(comboBox_dfeCC1_2->sizePolicy().hasHeightForWidth());
        comboBox_dfeCC1_2->setSizePolicy(sizePolicy2);
        comboBox_dfeCC0_2 = new QComboBox(frame_2);
        comboBox_dfeCC0_2->addItem(QString());
        comboBox_dfeCC0_2->addItem(QString());
        comboBox_dfeCC0_2->setObjectName(QString::fromUtf8("comboBox_dfeCC0_2"));
        comboBox_dfeCC0_2->setGeometry(QRect(0, 80, 31, 20));
        sizePolicy2.setHeightForWidth(comboBox_dfeCC0_2->sizePolicy().hasHeightForWidth());
        comboBox_dfeCC0_2->setSizePolicy(sizePolicy2);
        pushButton = new QPushButton(frame_2);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(190, 60, 21, 23));
        comboBox_dfeCC0 = new QComboBox(frame_2);
        comboBox_dfeCC0->addItem(QString());
        comboBox_dfeCC0->setObjectName(QString::fromUtf8("comboBox_dfeCC0"));
        comboBox_dfeCC0->setGeometry(QRect(0, 10, 31, 20));
        sizePolicy2.setHeightForWidth(comboBox_dfeCC0->sizePolicy().hasHeightForWidth());
        comboBox_dfeCC0->setSizePolicy(sizePolicy2);

        horizontalLayout_4->addWidget(frame_2);


        retranslateUi(channel);

        QMetaObject::connectSlotsByName(channel);
    } // setupUi

    void retranslateUi(QWidget *channel)
    {
        channel->setWindowTitle(QCoreApplication::translate("channel", "Form", nullptr));
        label->setText(QCoreApplication::translate("channel", "CH0", nullptr));
        comboBox_dfeCC1->setItemText(0, QCoreApplication::translate("channel", "unuse", nullptr));
        comboBox_dfeCC1->setItemText(1, QCoreApplication::translate("channel", "used", nullptr));

        comboBox_dfeCC2->setItemText(0, QCoreApplication::translate("channel", "unuse", nullptr));
        comboBox_dfeCC2->setItemText(1, QCoreApplication::translate("channel", "used", nullptr));

        label_3->setText(QCoreApplication::translate("channel", "CH1", nullptr));
        comboBox_dfeCC2_2->setItemText(0, QCoreApplication::translate("channel", "unuse", nullptr));
        comboBox_dfeCC2_2->setItemText(1, QCoreApplication::translate("channel", "used", nullptr));

        comboBox_dfeCC1_2->setItemText(0, QCoreApplication::translate("channel", "unuse", nullptr));
        comboBox_dfeCC1_2->setItemText(1, QCoreApplication::translate("channel", "used", nullptr));

        comboBox_dfeCC0_2->setItemText(0, QCoreApplication::translate("channel", "unuse", nullptr));
        comboBox_dfeCC0_2->setItemText(1, QCoreApplication::translate("channel", "used", nullptr));

        pushButton->setText(QCoreApplication::translate("channel", "+", nullptr));
        comboBox_dfeCC0->setItemText(0, QCoreApplication::translate("channel", "unused", nullptr));

    } // retranslateUi

};

namespace Ui {
    class channel: public Ui_channel {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CHANNEL_H
