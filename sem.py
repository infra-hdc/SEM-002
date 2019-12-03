#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic, QtWebKitWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("dialog.ui")
#window.btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())
