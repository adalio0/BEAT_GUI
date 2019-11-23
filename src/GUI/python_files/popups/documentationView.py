# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'documentationView.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Documentation_Window(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(690, 486)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.documentView_layout = QtWidgets.QVBoxLayout()
        self.documentView_layout.setObjectName("documentView_layout")
        self.documentView_label = QtWidgets.QLabel(Dialog)
        self.documentView_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.documentView_label.setStyleSheet("background-color: rgb(182, 206, 227);\n"
"")
        self.documentView_label.setAlignment(QtCore.Qt.AlignCenter)
        self.documentView_label.setObjectName("documentView_label")
        self.documentView_layout.addWidget(self.documentView_label)
        self.documentView_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.documentView_lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.documentView_lineEdit.setObjectName("documentView_lineEdit")
        self.documentView_layout.addWidget(self.documentView_lineEdit)
        self.documentView_listWidget = QtWidgets.QListWidget(Dialog)
        self.documentView_listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.documentView_listWidget.setObjectName("documentView_listWidget")
        item = QtWidgets.QListWidgetItem()
        self.documentView_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.documentView_listWidget.addItem(item)
        self.documentView_layout.addWidget(self.documentView_listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_3.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_3.addWidget(self.deleteButton)
        self.documentView_layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.documentView_layout)
        self.dDocumentView_layout = QtWidgets.QVBoxLayout()
        self.dDocumentView_layout.setObjectName("dDocumentView_layout")
        self.dDocumentView_label = QtWidgets.QLabel(Dialog)
        self.dDocumentView_label.setStyleSheet("background-color: rgb(182, 206, 227);")
        self.dDocumentView_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dDocumentView_label.setObjectName("dDocumentView_label")
        self.dDocumentView_layout.addWidget(self.dDocumentView_label)
        self.dDocumentView_textEdit = QtWidgets.QTextEdit(Dialog)
        self.dDocumentView_textEdit.setLineWidth(1)
        self.dDocumentView_textEdit.setObjectName("dDocumentView_textEdit")
        self.dDocumentView_layout.addWidget(self.dDocumentView_textEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.editButton = QtWidgets.QPushButton(Dialog)
        self.editButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_4.addWidget(self.editButton)
        self.dDocumentView_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.dDocumentView_layout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.documentView_label.setText(_translate("Dialog", "Document View"))
        self.documentView_lineEdit.setPlaceholderText(_translate("Dialog", "Search.."))
        __sortingEnabled = self.documentView_listWidget.isSortingEnabled()
        self.documentView_listWidget.setSortingEnabled(False)
        item = self.documentView_listWidget.item(0)
        item.setText(_translate("Dialog", "BEAT Documentation"))
        item = self.documentView_listWidget.item(1)
        item.setText(_translate("Dialog", "Plugin Structure"))
        self.documentView_listWidget.setSortingEnabled(__sortingEnabled)
        self.addButton.setText(_translate("Dialog", "Add"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.dDocumentView_label.setText(_translate("Dialog", "Detailed Document View"))
        self.saveButton.setText(_translate("Dialog", "Save"))
        self.editButton.setText(_translate("Dialog", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Documentation_Window()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
