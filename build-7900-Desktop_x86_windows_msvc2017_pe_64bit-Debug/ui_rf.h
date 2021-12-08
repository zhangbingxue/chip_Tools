/********************************************************************************
** Form generated from reading UI file 'rf.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_RF_H
#define UI_RF_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_rf
{
public:
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout;
    QPushButton *pushButton_ant0;
    QPushButton *pushButton_ant1;
    QPushButton *pushButton_ant2;
    QPushButton *pushButton_ant3;

    void setupUi(QWidget *rf)
    {
        if (rf->objectName().isEmpty())
            rf->setObjectName(QString::fromUtf8("rf"));
        rf->resize(175, 299);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(rf->sizePolicy().hasHeightForWidth());
        rf->setSizePolicy(sizePolicy);
        verticalLayout_2 = new QVBoxLayout(rf);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        groupBox = new QGroupBox(rf);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 216, 171);"));
        verticalLayout = new QVBoxLayout(groupBox);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        pushButton_ant0 = new QPushButton(groupBox);
        pushButton_ant0->setObjectName(QString::fromUtf8("pushButton_ant0"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(pushButton_ant0->sizePolicy().hasHeightForWidth());
        pushButton_ant0->setSizePolicy(sizePolicy1);
        pushButton_ant0->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        verticalLayout->addWidget(pushButton_ant0);

        pushButton_ant1 = new QPushButton(groupBox);
        pushButton_ant1->setObjectName(QString::fromUtf8("pushButton_ant1"));
        sizePolicy1.setHeightForWidth(pushButton_ant1->sizePolicy().hasHeightForWidth());
        pushButton_ant1->setSizePolicy(sizePolicy1);
        pushButton_ant1->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        verticalLayout->addWidget(pushButton_ant1);

        pushButton_ant2 = new QPushButton(groupBox);
        pushButton_ant2->setObjectName(QString::fromUtf8("pushButton_ant2"));
        sizePolicy1.setHeightForWidth(pushButton_ant2->sizePolicy().hasHeightForWidth());
        pushButton_ant2->setSizePolicy(sizePolicy1);
        pushButton_ant2->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        verticalLayout->addWidget(pushButton_ant2);

        pushButton_ant3 = new QPushButton(groupBox);
        pushButton_ant3->setObjectName(QString::fromUtf8("pushButton_ant3"));
        sizePolicy1.setHeightForWidth(pushButton_ant3->sizePolicy().hasHeightForWidth());
        pushButton_ant3->setSizePolicy(sizePolicy1);
        pushButton_ant3->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        verticalLayout->addWidget(pushButton_ant3);


        verticalLayout_2->addWidget(groupBox);


        retranslateUi(rf);

        QMetaObject::connectSlotsByName(rf);
    } // setupUi

    void retranslateUi(QWidget *rf)
    {
        rf->setWindowTitle(QCoreApplication::translate("rf", "Form", nullptr));
        groupBox->setTitle(QString());
        pushButton_ant0->setText(QCoreApplication::translate("rf", "ANT 0", nullptr));
        pushButton_ant1->setText(QCoreApplication::translate("rf", "ANT 1", nullptr));
        pushButton_ant2->setText(QCoreApplication::translate("rf", "ANT 2", nullptr));
        pushButton_ant3->setText(QCoreApplication::translate("rf", "ANT 3", nullptr));
    } // retranslateUi

};

namespace Ui {
    class rf: public Ui_rf {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_RF_H
