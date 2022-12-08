#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import nav

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

class Ui_Waiterbot_1(object):
    def setupUi(self, Waiterbot_1):
        Waiterbot_1.setObjectName("Waiterbot_1")
        Waiterbot_1.resize(442, 480)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 221, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(4, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.dockWidgetContents)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(220, 0, 221, 461))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(4, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 3, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 0, 1, 1)
        Waiterbot_1.setWidget(self.dockWidgetContents)
        self.pushButton.clicked.connect(self.t5)
        self.pushButton_2.clicked.connect(self.t3)
        self.pushButton_3.clicked.connect(self.t1)
        self.pushButton_4.clicked.connect(self.t6)
        self.pushButton_5.clicked.connect(self.t4)
        self.pushButton_6.clicked.connect(self.t2)
        self.pushButton_7.clicked.connect(self.t7)
        self.pushButton_8.clicked.connect(self.t8)


        self.retranslateUi(Waiterbot_1)
        QtCore.QMetaObject.connectSlotsByName(Waiterbot_1)

    def retranslateUi(self, Waiterbot_1):
        _translate = QtCore.QCoreApplication.translate
        Waiterbot_1.setWindowTitle(_translate("Waiterbot_1", "Waiterbot_1"))
        self.pushButton.setText(_translate("Waiterbot_1", "Table 5"))
        self.pushButton_3.setText(_translate("Waiterbot_1", "Table 1"))
        self.pushButton_2.setText(_translate("Waiterbot_1", "Table 3"))
        self.pushButton_7.setText(_translate("Waiterbot_1", "Table 7"))
        self.pushButton_8.setText(_translate("Waiterbot_1", "kitchen"))
        self.pushButton_4.setText(_translate("Waiterbot_1", "Table 6"))
        self.pushButton_5.setText(_translate("Waiterbot_1", "Table 4"))
        self.pushButton_6.setText(_translate("Waiterbot_1", "Table 2"))

    def t1(self):
        nav.GOTO("table1")
        print("1")
    def t2(self):
        nav.GOTO("table2")
    def t3(self):
        nav.GOTO("table3")
    def t4(self):
        nav.GOTO("table4")
    def t5(self):
        nav.GOTO("table5")
    def t6(self):
        nav.GOTO("table6")
    def t7(self):
        nav.GOTO("table7")
    def t8(self):
        nav.GOTO("kitchen")
    
if __name__ == "__main__":
    rospy.init_node("gui",anonymous=False)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Waiterbot_1 = QtWidgets.QDockWidget()
    ui = Ui_Waiterbot_1()
    ui.setupUi(Waiterbot_1)
    Waiterbot_1.show()
    sys.exit(app.exec_())

