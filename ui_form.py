# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(613, 303)
        Widget.setMinimumSize(QSize(600, 300))
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 611, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.user_label = QLabel(self.verticalLayoutWidget)
        self.user_label.setObjectName(u"user_label")

        self.verticalLayout.addWidget(self.user_label)

        self.user_entry = QLineEdit(self.verticalLayoutWidget)
        self.user_entry.setObjectName(u"user_entry")
        self.user_entry.setMinimumSize(QSize(250, 30))
        self.user_entry.setMaximumSize(QSize(300, 40))

        self.verticalLayout.addWidget(self.user_entry)

        self.vSpacer_bw_user_pass = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.vSpacer_bw_user_pass)

        self.password_label = QLabel(self.verticalLayoutWidget)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_entry = QLineEdit(self.verticalLayoutWidget)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setMinimumSize(QSize(250, 30))
        self.password_entry.setMaximumSize(QSize(300, 40))
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.password_entry)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_button = QPushButton(self.verticalLayoutWidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(100, 30))
        self.login_button.setMaximumSize(QSize(150, 30))
        self.login_button.setCheckable(False)

        self.horizontalLayout.addWidget(self.login_button)

        self.create_acc_button = QPushButton(self.verticalLayoutWidget)
        self.create_acc_button.setObjectName(u"create_acc_button")
        self.create_acc_button.setMinimumSize(QSize(100, 30))
        self.create_acc_button.setMaximumSize(QSize(150, 30))

        self.horizontalLayout.addWidget(self.create_acc_button)

        self.hSpacer_after_login_create = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSpacer_after_login_create)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vSpacer_below_buttons = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.vSpacer_below_buttons)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.user_label.setText(QCoreApplication.translate("Widget", u"Username", None))
        self.user_entry.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter your Username", None))
        self.password_label.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.password_entry.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter your Password", None))
        self.login_button.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.create_acc_button.setText(QCoreApplication.translate("Widget", u"Create Account", None))
    # retranslateUi

