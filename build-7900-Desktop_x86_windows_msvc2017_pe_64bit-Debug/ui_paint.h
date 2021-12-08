/********************************************************************************
** Form generated from reading UI file 'paint.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PAINT_H
#define UI_PAINT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_paint
{
public:

    void setupUi(QWidget *paint)
    {
        if (paint->objectName().isEmpty())
            paint->setObjectName(QString::fromUtf8("paint"));
        paint->resize(328, 692);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(paint->sizePolicy().hasHeightForWidth());
        paint->setSizePolicy(sizePolicy);

        retranslateUi(paint);

        QMetaObject::connectSlotsByName(paint);
    } // setupUi

    void retranslateUi(QWidget *paint)
    {
        paint->setWindowTitle(QCoreApplication::translate("paint", "Form", nullptr));
    } // retranslateUi

};

namespace Ui {
    class paint: public Ui_paint {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PAINT_H
