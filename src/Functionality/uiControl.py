#! /usr/bin/env python3.

import os
import sys
import subprocess
import xml.etree.ElementTree as ET

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.GUI.python_files.BATT5_GUI import Ui_BATT5
from src.GUI.python_files.popups.errors import ErrFile, Errx86, ErrRadare
from src.GUI.python_files.popups.newProjectWind import NewProject
from src.GUI.python_files.popups.xmlEditor import XMLEditor
from src.GUI.python_files.popups.analysisResultView import Analysis_Window
from src.GUI.python_files.popups.documentationView import Documentation_Window

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.window = Ui_BATT5()
        self.window.setupUi(self)

# Menu Bar
        # Clicking on New.. menu bar calls showNewProject method
        self.window.actionNew_Project.triggered.connect(self.showNewProject)

        # Clicking on Open menu bar calls showFileExplorer method
        self.window.actionOpen.triggered.connect(self.showFileExplorerSimple)

        # Clicking on Save as menu bar calls..
        self.window.actionSave_as.triggered.connect(self.showFileExplorerSimple)


        # Clicking on Save Analysis menu bar calls showAnalysisWindow method
        self.window.actionSave_Analysis.triggered.connect(self.showAnalysisWindow)

        # Clicking on Windows menu bar calls..

        # Clicking on Help menu bar calls showDocumentWindow method
        self.window.actionDocumentation.triggered.connect(self.showDocumentationWindow)

# Detailed Plugin Management
        # Clicking on Plugin Structure browse button calls showFileExplorer method
        self.window.dpmPluginStructure_button.clicked.connect(self.showFileExplorer)

        # Clicking on Plugin Predefined browse button calls showFileExplorer method (xmlEditor for now)
        self.window.dpmPluginPredefined_button.clicked.connect(self.xmlEditor)

    # Opens up an xml (file) editor TODO: If we open this window it creates a bug where we can't select a file in the
    # TODO:                                 main window need to figure out a fix.
    def xmlEditor(self):
        self.window = XMLEditor()
        self.window.show()

        cur_path = os.getcwd()
        file = os.path.join(cur_path, '..', 'Configurations', 'country_data.xml')
        tree = ET.parse(file)
        root = tree.getroot()

        # print(root.tag)

    # Shows NewProject window
    def showNewProject(self):
        self.window =QtWidgets.QWidget()
        self.ui = NewProject()
        self.ui.setupUi(self.window)
        self.window.show()

    # Shows Analysis Result window
    def showAnalysisWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Analysis_Window()
        self.ui.setupUi(self.window)
        self.window.show()


    # Shows Documentation window
    def showDocumentationWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Documentation_Window()
        self.ui.setupUi(self.window)
        self.window.show()


    # Open up file explorer to select a file
    def showFileExplorer(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        self.window.dpmPluginStructure_lineEdit.setText(name)

    # Open up file explorer, does not pass any data
    def showFileExplorerSimple(self):
        _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')

    # Shows ErrFile window
    def showErrFile(self):
        self.window = ErrFile()
        self.window.show()

    # Shows Errx86 window
    def showErrx86(self):
        self.window = Errx86()
        self.window.show()

    # Shows ErrBFile window
    def showErrBFile(self):
        self.window = ErrRadare()
        self.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
