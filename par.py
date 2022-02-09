from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelDateStart = QtWidgets.QLabel(self.centralwidget)
        self.labelDateStart.setGeometry(QtCore.QRect(60, 60, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDateStart.setFont(font)
        self.labelDateStart.setObjectName("labelDateStart")
        self.labelDateEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelDateEnd.setGeometry(QtCore.QRect(460, 60, 361, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDateEnd.setFont(font)
        self.labelDateEnd.setObjectName("labelDateEnd")
        self.labelPar = QtWidgets.QLabel(self.centralwidget)
        self.labelPar.setGeometry(QtCore.QRect(60, 120, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPar.setFont(font)
        self.labelPar.setObjectName("labelPar")
        self.labelLengthPP = QtWidgets.QLabel(self.centralwidget)
        self.labelLengthPP.setGeometry(QtCore.QRect(460, 120, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLengthPP.setFont(font)
        self.labelLengthPP.setObjectName("labelLengthPP")
        self.labelTempStart = QtWidgets.QLabel(self.centralwidget)
        self.labelTempStart.setGeometry(QtCore.QRect(60, 180, 361, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTempStart.setFont(font)
        self.labelTempStart.setObjectName("labelTempStart")
        self.labelTempEnd = QtWidgets.QLabel(self.centralwidget)
        self.labelTempEnd.setGeometry(QtCore.QRect(460, 180, 311, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTempEnd.setFont(font)
        self.labelTempEnd.setObjectName("labelTempEnd")
        self.pushButtonInput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInput.setGeometry(QtCore.QRect(350, 280, 100, 30))
        self.pushButtonInput.setObjectName("pushButtonInput")
        self.lineEditDateStart = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDateStart.setGeometry(QtCore.QRect(60, 100, 171, 22))
        self.lineEditDateStart.setObjectName("lineEditDateStart")
        self.lineEditPar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPar.setGeometry(QtCore.QRect(60, 160, 171, 22))
        self.lineEditPar.setObjectName("lineEditPar")
        self.lineEditTempStart = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTempStart.setGeometry(QtCore.QRect(60, 220, 171, 22))
        self.lineEditTempStart.setObjectName("lineEditTempStart")
        self.lineEditDateEnd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDateEnd.setGeometry(QtCore.QRect(460, 100, 171, 22))
        self.lineEditDateEnd.setObjectName("lineEditDateEnd")
        self.lineEditLengthPP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLengthPP.setGeometry(QtCore.QRect(460, 160, 171, 22))
        self.lineEditLengthPP.setObjectName("lineEditLengthPP")
        self.lineEditTempEnd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTempEnd.setGeometry(QtCore.QRect(460, 220, 171, 22))
        self.lineEditTempEnd.setObjectName("lineEditTempEnd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuInput = QtWidgets.QMenu(self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuPlots = QtWidgets.QMenu(self.menubar)
        self.menuPlots.setObjectName("menuPlots")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuPlots.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ПЦО. Температура и пар"))
        self.labelDateStart.setText(_translate("MainWindow", "Дата начала закачки пара (гггг-мм-дд)"))
        self.labelDateEnd.setText(_translate("MainWindow", "Дата конца закачки пара (гггг-мм-дд)"))
        self.labelPar.setText(_translate("MainWindow", "Пар, т"))
        self.labelLengthPP.setText(_translate("MainWindow", "Длина ПП"))
        self.labelTempStart.setText(_translate("MainWindow", "Температура начальная"))
        self.labelTempEnd.setText(_translate("MainWindow", "Температура на выходе"))
        self.pushButtonInput.setText(_translate("MainWindow", "Ввод"))
        self.menuInput.setTitle(_translate("MainWindow", "Ввод данных"))
        self.menuPlots.setTitle(_translate("MainWindow", "Графики"))
        self.action.setText(_translate("MainWindow", "хуй"))

    def add_functions(self):
        self.pushButtonInput.clicked.connect(lambda: self.save_data(self.lineEditDateStart.text(),
                                                                    self.lineEditDateEnd.text(),
                                                                    self.lineEditPar.text(),
                                                                    self.lineEditLengthPP.text(),
                                                                    self.lineEditTempStart.text(),
                                                                    self.lineEditTempEnd.text()))
        
    def save_data(self, date_start, date_end, par, length_pp, temp_start, temp_end):
        data = {
            'Дата начала закачки пара':date_start,
            'Дата конца закачки пара':date_end,
            'Пар, т':par,
            'Длина ПП':length_pp,
            'Температура начальная':temp_start,
            'Температура на выходе':temp_end
        }
        df = pd.DataFrame(data=data, index=[0])
        df['Дата начала закачки пара'] = pd.to_datetime(df['Дата начала закачки пара'])
        df['Дата конца закачки пара'] = pd.to_datetime(df['Дата конца закачки пара'])
        df[['Пар, т', 'Длина ПП']] = df[['Пар, т', 'Длина ПП']].astype('int64')
        df[['Температура начальная', 'Температура на выходе']] = df[['Температура начальная', 'Температура на выходе']].astype('float')
        df['Кол-во дней закачки'] = (df['Дата конца закачки пара'] - df['Дата начала закачки пара']).dt.days
        df['Тон пара в день'] = (df['Пар, т'] / df['Кол-во дней закачки']).round(3)
        df['Температура в день'] = ((df['Температура на выходе'] - df['Температура начальная']) / df['Кол-во дней закачки']).round(3)
        new_columns_list = ['Дата начала закачки пара', 'Дата конца закачки пара',
                    'Кол-во дней закачки', 'Пар, т', 'Длина ПП', 'Тон пара в день',
                    'Температура начальная', 'Температура на выходе', 'Температура в день']

        df = df[new_columns_list]

        full_df = pd.DataFrame()
        final_data = pd.DataFrame()

        days_count = int(df['Кол-во дней закачки'])
        list_days = [i for i in range (0, days_count+1)]
        full_df = pd.DataFrame({'День':list_days})

        temp_diff = float(df['Температура в день'])
        temp_start = float(df['Температура начальная'])
        par_diff = float(df['Тон пара в день'])
        par_start = 0
        
        for index_df, row_df in full_df.iterrows():
            if index_df == 0:
                full_df.loc[0, 'Температура'] = temp_start
                full_df.loc[0, 'Пар'] = par_start
            else:
                full_df.loc[index_df, 'Температура'] = float(full_df.loc[index_df - 1, 'Температура']) + temp_diff
                full_df.loc[index_df, 'Пар'] = float(full_df.loc[index_df - 1, 'Пар']) + par_diff
        
        final_data = pd.concat([final_data, full_df])

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 7), dpi=100)
        ax1.plot(final_data['День'], final_data['Температура'])
        ax1.set(xlabel='День', ylabel='Температура', title='Изменение температуры по дням')
        ax1.grid()

        ax2.plot(final_data['День'], final_data['Пар'])
        ax2.set(xlabel='День', ylabel='Пар', title='Изменение пара по дням')
        ax2.grid()
        plt.show()

        print(final_data)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
