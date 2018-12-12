#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
 
# Create an PyQT4 application object.
a = QApplication(sys.argv)       
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
 
# Show a message box
result = QMessageBox.question(w, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
QMessageBox.information(w, "Message", "An information messagebox @ pythonspot.com ")
 
if result == QMessageBox.Yes:
    print 'Yes.'
else:
    print 'No.'        
 
 
# Show window
w.show() 
 
sys.exit(a.exec_())
