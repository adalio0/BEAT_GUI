# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProjectWind.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class NewProject(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(785, 443)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.saveNewProject = QtWidgets.QPushButton(Form)
        self.saveNewProject.setObjectName("saveNewProject")
        self.gridLayout.addWidget(self.saveNewProject, 7, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setStyleSheet("background-color: rgb(182, 206, 227);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.cancelNewProject = QtWidgets.QPushButton(Form)
        self.cancelNewProject.setObjectName("cancelNewProject")
        self.gridLayout.addWidget(self.cancelNewProject, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.browseNewProject = QtWidgets.QPushButton(Form)
        self.browseNewProject.setObjectName("browseNewProject")
        self.gridLayout.addWidget(self.browseNewProject, 3, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.gridLayout.addWidget(self.treeWidget, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Project Name"))
        self.saveNewProject.setText(_translate("Form", "Create"))
        self.label.setText(_translate("Form", "                                                                                                    Create A New Project"))
        self.label_5.setText(_translate("Form", "Binary File Properties"))
        self.cancelNewProject.setText(_translate("Form", "Cancel"))
        self.label_4.setText(_translate("Form", "Binary File Path"))
        self.label_3.setText(_translate("Form", "Project Description"))
        self.browseNewProject.setText(_translate("Form", "Browse"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Value"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "OS"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "Binary Type"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "Machine"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("Form", "Class"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("Form", "Bits"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("Form", "Language"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("Form", "New Item"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("Form", "Canary"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("Form", "Crypto"))
        self.treeWidget.topLevelItem(9).setText(0, _translate("Form", "Nx"))
        self.treeWidget.topLevelItem(10).setText(0, _translate("Form", "Pic"))
        self.treeWidget.topLevelItem(11).setText(0, _translate("Form", "Relocs"))
        self.treeWidget.topLevelItem(12).setText(0, _translate("Form", "Relro"))
        self.treeWidget.topLevelItem(13).setText(0, _translate("Form", "Stripped"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

