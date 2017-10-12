from PyQt5 import QtWidgets, uic, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
model = QtGui.QStandardItemModel()

for i in range(0, 4):

    item = QtGui.QStandardItem(str(i))
    column = QtGui.QStandardItem(str(i) + '2')

    model.setItem(i,0,item)
    model.setItem(i,1,column)

    #model.appendColumn([column])
    #column = QtGui.QStandardItem(str(i) + 'w')
    #model.insertColumn(1,[column])

tableview = QtWidgets.QTableView()
tableview.setModel(model)
layot = QtWidgets.QVBoxLayout()
layot.addWidget(tableview)
window.setLayout(layot)

window.show()
sys.exit(app.exec_())
