# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\changeBorehole.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changeBorehole(object):
    def setupUi(self, changeBorehole):
        changeBorehole.setObjectName("changeBorehole")
        changeBorehole.resize(300, 362)
        self.centralwidget = QtWidgets.QWidget(changeBorehole)
        self.centralwidget.setObjectName("centralwidget")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(10, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(10, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(10, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(10, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(10, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(30, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_change = QtWidgets.QPushButton(self.centralwidget)
        self.btn_change.setGeometry(QtCore.QRect(160, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_change.setFont(font)
        self.btn_change.setObjectName("btn_change")
        self.combo_depZone = QtWidgets.QComboBox(self.centralwidget)
        self.combo_depZone.setGeometry(QtCore.QRect(160, 227, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_depZone.setFont(font)
        self.combo_depZone.setObjectName("combo_depZone")
        self.line_lengthSteamPipe = QtWidgets.QLineEdit(self.centralwidget)
        self.line_lengthSteamPipe.setGeometry(QtCore.QRect(160, 186, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_lengthSteamPipe.setFont(font)
        self.line_lengthSteamPipe.setObjectName("line_lengthSteamPipe")
        self.line_bhDepthPaker = QtWidgets.QLineEdit(self.centralwidget)
        self.line_bhDepthPaker.setGeometry(QtCore.QRect(160, 137, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_bhDepthPaker.setFont(font)
        self.line_bhDepthPaker.setObjectName("line_bhDepthPaker")
        self.line_bhDepth = QtWidgets.QLineEdit(self.centralwidget)
        self.line_bhDepth.setGeometry(QtCore.QRect(160, 95, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_bhDepth.setFont(font)
        self.line_bhDepth.setObjectName("line_bhDepth")
        self.line_name = QtWidgets.QLineEdit(self.centralwidget)
        self.line_name.setGeometry(QtCore.QRect(160, 56, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_name.setFont(font)
        self.line_name.setObjectName("line_name")
        self.combo_numberBorehole = QtWidgets.QComboBox(self.centralwidget)
        self.combo_numberBorehole.setGeometry(QtCore.QRect(160, 17, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_numberBorehole.setFont(font)
        self.combo_numberBorehole.setObjectName("combo_numberBorehole")
        changeBorehole.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(changeBorehole)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        changeBorehole.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(changeBorehole)
        self.statusbar.setObjectName("statusbar")
        changeBorehole.setStatusBar(self.statusbar)

        self.retranslateUi(changeBorehole)
        QtCore.QMetaObject.connectSlotsByName(changeBorehole)

    def retranslateUi(self, changeBorehole):
        _translate = QtCore.QCoreApplication.translate
        changeBorehole.setWindowTitle(_translate("changeBorehole", "Изменить скважину"))
        self.label_29.setText(_translate("changeBorehole", "Номер скважины"))
        self.label_30.setText(_translate("changeBorehole", "Название"))
        self.label_31.setText(_translate("changeBorehole", "Глубина, м"))
        self.label_32.setText(_translate("changeBorehole", "Глубина до пакера, м"))
        self.label_33.setText(_translate("changeBorehole", "Длина паропровода"))
        self.label_34.setText(_translate("changeBorehole", "Зона залежи"))
        self.btn_cancel.setText(_translate("changeBorehole", "Отмена"))
        self.btn_change.setText(_translate("changeBorehole", "Изменить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changeBorehole = QtWidgets.QMainWindow()
    ui = Ui_changeBorehole()
    ui.setupUi(changeBorehole)
    changeBorehole.show()
    sys.exit(app.exec_())
