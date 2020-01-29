#-*- coding:utf-8 -*-

import os, sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, QSize, QDir, Qt
from BookTable_ver2_0.utils import *
import getpass

class Openfile_window():
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.pathRoot = QDir.rootPath()
        self.mainwindow.model = QFileSystemModel()
        self.mainwindow.model.setRootPath(self.mainwindow.pathRoot)
        self.mainwindow.indexRoot = self.mainwindow.model.index(self.mainwindow.model.rootPath())
        self.mainwindow.treeView.setModel(self.mainwindow.model)
        self.mainwindow.treeView.setRootIndex(self.mainwindow.indexRoot)

        self.mainwindow.treeView.clicked['QModelIndex'].connect(self.get_file_path)
        self.mainwindow.submit_button.clicked.connect(self.set_file_path)

    def get_file_path(self, index):
        indexItem = self.mainwindow.model.index(index.row(), 0, index.parent())

        self.mainwindow.file_name = self.mainwindow.model.fileName(indexItem)
        self.mainwindow.file_dir = self.mainwindow.model.filePath(indexItem)

        self.mainwindow.dirPlainText.setPlainText(self.mainwindow.file_dir)

    def set_file_path(self): # trick.
        if self.mainwindow.file_name == '':
            return 0
        self.mainwindow.main_stack.setCurrentIndex(0)

        # Open file
        self.mainwindow.excel = pd.read_excel(self.mainwindow.file_dir.replace('/', '\\'))

        # update main window
        self.mainwindow.update_main_tables()
