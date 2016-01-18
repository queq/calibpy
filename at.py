import sys

from PyQt4 import QtGui, uic


app = QtGui.QApplication(sys.argv)
widget = uic.loadUi('at.ui')
widget.show()
sys.exit(app.exec_())
