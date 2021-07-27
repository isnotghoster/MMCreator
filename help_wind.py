# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/help_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hw(object):
    def setupUi(self, hw):
        hw.setObjectName("hw")
        hw.resize(367, 679)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI/../Ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hw.setWindowIcon(icon)
        hw.setStyleSheet("background: #121212\n"
"")
        self.layoutWidget = QtWidgets.QWidget(hw)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 351, 671))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setStyleSheet("color: #ffffff")
        self.tabWidget.setObjectName("tabWidget")
        self.CM = QtWidgets.QWidget()
        self.CM.setObjectName("CM")
        self.gridLayout = QtWidgets.QGridLayout(self.CM)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.CM)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffffff")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.CM, "")
        self.wip = QtWidgets.QWidget()
        self.wip.setObjectName("wip")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wip)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.wip)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tabWidget.addTab(self.wip, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.back = QtWidgets.QPushButton(self.layoutWidget)
        self.back.setStyleSheet("color: #ffffff;\n"
"background: #414141;\n"
"border-radius: 5px;\n"
"height: 25px")
        self.back.setObjectName("back")
        self.gridLayout_2.addWidget(self.back, 1, 0, 1, 1)

        self.retranslateUi(hw)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(hw)

    def retranslateUi(self, hw):
        _translate = QtCore.QCoreApplication.translate
        hw.setWindowTitle(_translate("hw", "Form"))
        self.label.setText(_translate("hw", "\"Name Class:\"-глобальное название моба,\n"
"оно будет использоваться в плагине.\n"
"\n"
"\"Type:\"-тип моба,то есть как будет он\n"
"выглядеть в игре.\n"
"\n"
"\"Display:\"-название моба которое будет\n"
" отображатся в игре.\n"
"\n"
"\"Health:\"-Здоровь моба в ед..\n"
"\n"
"\"Damage:\"-Урон моба в ед..\n"
"\n"
"\"Faction:\"-Фракция моба,то есть как он\n"
"будет себя вести.\n"
"\n"
"\"Mount:\"-На ком будет сидеть моб.\n"
"\n"
"\"Equipment:\"-Список брони и оружия,\n"
"которое будет на мобе."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CM), _translate("hw", "Кастомный моб"))
        self.label_3.setText(_translate("hw", "WIP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wip), _translate("hw", "Wip"))
        self.back.setText(_translate("hw", "Обратно"))