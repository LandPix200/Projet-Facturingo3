# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 595)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/F1-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 3)
        self.table_clt = QtWidgets.QTableWidget(self.centralwidget)
        self.table_clt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgba(90, 173, 187, 54);\n"
"gridline-color: rgb(52, 101, 164);")
        self.table_clt.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.table_clt.setAlternatingRowColors(True)
        self.table_clt.setShowGrid(True)
        self.table_clt.setGridStyle(QtCore.Qt.SolidLine)
        self.table_clt.setWordWrap(False)
        self.table_clt.setRowCount(9999)
        self.table_clt.setObjectName("table_clt")
        self.table_clt.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_clt.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_clt.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_clt.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_clt.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_clt.setHorizontalHeaderItem(4, item)
        self.table_clt.horizontalHeader().setDefaultSectionSize(250)
        self.table_clt.horizontalHeader().setStretchLastSection(True)
        self.table_clt.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.table_clt, 3, 0, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 4, 1, 1)
        self.btn_remove_clt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_remove_clt.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_remove_clt.setFont(font)
        self.btn_remove_clt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_remove_clt.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_remove_clt.setObjectName("btn_remove_clt")
        self.gridLayout.addWidget(self.btn_remove_clt, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 4, 2, 1, 1)
        self.btn_modif_clt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_modif_clt.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_modif_clt.setFont(font)
        self.btn_modif_clt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_modif_clt.setStyleSheet("background-color: rgba(65, 191, 64, 197);")
        self.btn_modif_clt.setObjectName("btn_modif_clt")
        self.gridLayout.addWidget(self.btn_modif_clt, 5, 1, 1, 1)
        self.line_search = QtWidgets.QLineEdit(self.centralwidget)
        self.line_search.setMinimumSize(QtCore.QSize(300, 35))
        self.line_search.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.line_search.setAlignment(QtCore.Qt.AlignCenter)
        self.line_search.setObjectName("line_search")
        self.gridLayout.addWidget(self.line_search, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clients"))
        self.table_clt.setSortingEnabled(True)
        item = self.table_clt.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Identifiant"))
        item = self.table_clt.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom et Prénom"))
        item = self.table_clt.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N° de téléphone"))
        item = self.table_clt.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date de naissance"))
        item = self.table_clt.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Adresse mail"))
        self.btn_remove_clt.setText(_translate("MainWindow", "Enlever un client"))
        self.label.setText(_translate("MainWindow", "Base de donnée des clients"))
        self.btn_modif_clt.setText(_translate("MainWindow", "Modifier un client"))
        self.line_search.setPlaceholderText(_translate("MainWindow", "Rechercher un client"))

