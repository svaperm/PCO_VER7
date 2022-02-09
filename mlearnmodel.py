import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.uic import loadUi
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

class DataDialog(QDialog):
    def __init__(self):
        super(DataDialog,self).__init__()
        loadUi('m_learn.ui',self)
        self.browse.clicked.connect(self.browsefiles)
        self.teachModel.clicked.connect(self.teachmodel)
        self.saveModel.hide()
        self.cancelModel.hide()
    # выбор файла из проводника
    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self,'Open File',r'C:\Users\Computer\Desktop\PCO_Model','Лист Microsoft Excel (*.xlsx)')
        self.fileName.setText(fname[0])
    # переобучение модели
    def learning(self,file,model,x_list, y_list):
        # -- вот этот кусок стоит модифицировать на случай проблем с данными
        data = pd.read_excel(file, 1)
        X = data[x_list].values
        y = data[y_list].values
        # --
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        reg = pickle.load(open(model,'rb'))
        # !!Возможно только переобучение с начала невозможно добавить данные!!
        reg.fit(X_train,y_train)
        y_predict = reg.predict(X_test)
        mae = mean_absolute_error(y_test, y_predict)
        mse = mean_squared_error(y_test, y_predict)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_predict)
        str='Metrics:\n MAE: {}\n MSE: {}\nRMSE: {}\nR-Squared: {}'.format(mae, mse, rmse, r2)
        self.metrics.setText(str)
        self.saveModel.clicked.connect(lambda: self.save(reg,model))
        self.saveModel.show()
        self.cancelModel.clicked.connect(self.cancel)
        self.cancelModel.show()

    # кнопка переобучения модели
    def teachmodel(self):
        file=self.fileName.text()
        if file == "":
            self.metrics.setText('Выберите данные для обучения')
        else : 
            if self.selectModel.currentIndex() == 0:
                x_columns = ['Глубина, м', 'Барометрия, закачка, МПа', 'Термометрия, закачка, МПа', 'Термометрия, статика, МПа','Расходометрия, об/мин', 'Перфорация']
                y_columns = ['Степень сухости пара, %', 'Удельная энтальпия, кДж/кг']
                self.learning(file,'model1.pkl',x_columns,y_columns)
            else:
                self.metrics.setText('Нету модели :с')   
    # сохранить
    def save(self,model,file):
        pickle.dump(model,open(file,'wb'))
        self.saveModel.clicked.disconnect()
        self.saveModel.hide()
    # отмена
    def cancel(self):
        str='Metrics:\n MAE: \n MSE: \nRMSE: \nR-Squared: '
        self.metrics.setText(str)
        self.cancelModel.hide()


app=QApplication(sys.argv)
mainwindow=DataDialog()
widget=QtWidgets.QStackedWidget()
widget.setFixedHeight(300)
widget.setFixedWidth(600)
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())