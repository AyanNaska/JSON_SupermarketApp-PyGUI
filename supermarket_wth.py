import sys
import json
from PySide6 import QtCore, QtGui, QtWidgets

# Function to read the JSON file and return the parsed data
def read_json_file():
    with open("supermarket_database.json", "r") as file: 
        data = json.load(file)
    return data

# Function to get the item details for a specific floor
def get_floor_items(floor_name):
    data = read_json_file()
    for floor in data["supermarket"]["floors"]:
        if floor["floor_name"].lower() == floor_name.lower():
            items_list = []
            for item in floor["items"]:
                item_info = f"Item: {item['item_name']}\nPrice: ${item['price']}\nQuantity: {item['quantity']}\n{'-' * 20}"
                items_list.append(item_info)
            return "\n".join(items_list)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 586)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background_Frames = QtWidgets.QFrame(parent=self.centralwidget)
        self.Background_Frames.setGeometry(QtCore.QRect(0, 0, 891, 641))
        self.Background_Frames.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Background_Frames.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Background_Frames.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Background_Frames.setObjectName("Background_Frames")
        self.Floor_Buttons = QtWidgets.QFrame(parent=self.Background_Frames)
        self.Floor_Buttons.setGeometry(QtCore.QRect(9, 9, 301, 541))
        self.Floor_Buttons.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid rgb(0,0,0);")
        self.Floor_Buttons.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Floor_Buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Floor_Buttons.setObjectName("Floor_Buttons")
        self.pushButton = QtWidgets.QPushButton(parent=self.Floor_Buttons)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 231, 51))
        self.pushButton.setStyleSheet("QPushButton\n"
                              "{\n"
                              "background-color: rgb(245, 245, 245);\n"
                              "}\n"
                              "QPushButton:hover\n"
                              "{\n"
                              "background-color: rgb(235, 235, 235);\n"
                              "}\n"
                              "QPushButton:pressed\n"
                              "{\n"
                              "background-color: rgb(220, 220, 220);\n"
                              "}\n"
                              "")
        self.pushButton.setObjectName("1st Floor")
        self.pushButton.clicked.connect(self.display_food_floor)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.Floor_Buttons)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 300, 231, 51))
        self.pushButton_2.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(245, 245, 245);\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "background-color: rgb(235, 235, 235);\n"
                                        "}\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "background-color: rgb(220, 220, 220);\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.display_cloths_floor)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.Floor_Buttons)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 380, 231, 51))
        self.pushButton_3.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(245, 245, 245);\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "background-color: rgb(235, 235, 235);\n"
                                        "}\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "background-color: rgb(220, 220, 220);\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.display_accessories_floor)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.Floor_Buttons)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 460, 231, 51))
        self.pushButton_4.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(245, 245, 245);\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "background-color: rgb(235, 235, 235);\n"
                                        "}\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "background-color: rgb(220, 220, 220);\n"
                                        "}\n"
                                        "")
        self.pushButton_4.setObjectName("4th Floor")
        self.pushButton_4.clicked.connect(self.display_entertainment_floor)

        self.label1 = QtWidgets.QLabel(parent=self.Floor_Buttons)
        self.label1.setGeometry(QtCore.QRect(50, 30, 191, 151))
        self.label1.setStyleSheet("image: url(1st.jpg);")
        self.label1.setObjectName("label1")
        self.label1.hide();
        self.label2 = QtWidgets.QLabel(parent=self.Floor_Buttons)
        self.label2.setGeometry(QtCore.QRect(50, 30, 191, 151))
        self.label2.setStyleSheet("image: url(2nd.jpg);")
        self.label2.setObjectName("label2")
        self.label2.hide();
        self.label3 = QtWidgets.QLabel(parent=self.Floor_Buttons)
        self.label3.setGeometry(QtCore.QRect(50, 30, 191, 151))
        self.label3.setStyleSheet("image: url(3rd.jpg);")
        self.label3.setObjectName("label3")
        self.label3.hide();
        self.label3_2 = QtWidgets.QLabel(parent=self.Floor_Buttons)
        self.label3_2.setGeometry(QtCore.QRect(50, 30, 191, 151))
        self.label3_2.setStyleSheet("image: url(4th.jpg);")
        self.label3_2.setObjectName("label3_2")
        self.label3_2.hide();
        self.textEdit = QtWidgets.QTextEdit(parent=self.Background_Frames)
        self.textEdit.setGeometry(QtCore.QRect(340, 140, 521, 411))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid rgb(0,0,0);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.Background_Frames)
        self.label.setGeometry(QtCore.QRect(500, 30, 241, 71))
        self.label.setStyleSheet("image: url(ADI.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "I FLOOR (FOOD)"))
        self.pushButton_2.setText(_translate("MainWindow", "II FLOOR (CLOTHS)"))
        self.pushButton_3.setText(_translate("MainWindow", "III FLOOR (ACCESSORIES)"))
        self.pushButton_4.setText(_translate("MainWindow", "IV FLOOR (ENTERTAINMENT)"))

### Functions to display item details for each floor
    def display_food_floor(self):
        items = get_floor_items("Food")
        self.label1.show();
        self.label2.hide();
        self.label3.hide();
        self.label3_2.hide();
        self.textEdit.setPlainText(items) # print as it is

    def display_cloths_floor(self):
        items = get_floor_items("Cloths")
        self.label1.hide();
        self.label2.show();
        self.label3.hide();
        self.label3_2.hide();
        self.textEdit.setPlainText(items)

    def display_accessories_floor(self):
        items = get_floor_items("Accessories")
        self.label1.hide();
        self.label2.hide();
        self.label3.show();
        self.label3_2.hide();
        self.textEdit.setPlainText(items)

    def display_entertainment_floor(self):
        items = get_floor_items("Entertainment")
        self.label1.hide();
        self.label2.hide();
        self.label3.hide();
        self.label3_2.show();
        self.textEdit.setPlainText(items)
################################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
