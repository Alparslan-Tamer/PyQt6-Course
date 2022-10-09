# Form implementation generated from reading ui file '11-QRadioButton_with_Designer.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(231, 183)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:yellow\n"
"}\n"
"\n"
"QLabel{\n"
"color:green\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_first = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton_first.setFont(font)
        self.radioButton_first.setObjectName("radioButton_first")
        self.radioButton_first.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_first)
        self.radioButton_bus = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton_bus.setFont(font)
        self.radioButton_bus.setObjectName("radioButton_bus")
        self.radioButton_bus.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_bus)
        self.radioButton_eco = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton_eco.setFont(font)
        self.radioButton_eco.setObjectName("radioButton_eco")
        self.radioButton_eco.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_eco)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout_2.addWidget(self.label_result)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label_result.setText(f"You have selected: {radio_btn.text()}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Flight Type"))
        self.radioButton_first.setText(_translate("Dialog", "First Class           $150"))
        self.radioButton_bus.setText(_translate("Dialog", "Business Class   $120"))
        self.radioButton_eco.setText(_translate("Dialog", "Economic Class  $100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
