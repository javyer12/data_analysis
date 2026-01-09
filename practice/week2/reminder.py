
 
# reminder_time = input("Enter the reminder time (HH/MM):")
# message= input("Enter your message: ")

# print("Reminder set....")

# while True:
#     current_time = datetime.now().strftime('%H:%M')
#     print("Current time", current_time)
#     if current_time == reminder_time:
#         print("⏰REMINDER.....")
#         print(message)
#         break 

#     time.sleep(30)
import time
from datetime import datetime
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My form")

        # Create widgets
        self.current_time_label = QtWidgets.QLabel(f"Current Time: {datetime.now().strftime('%H:%M')}")
        self.text1 = QtWidgets.QLabel("<font color=gray size=5>Write the Hour to remind</font>")
        self.edit1 = QLineEdit("Write the hour here..")
        self.text2 = QtWidgets.QLabel("<font color=gray size=5>Write your message..</font>")
        self.edit2 = QLineEdit("Write the message there..")

        self.button = QPushButton("Submit")
        # Create layout and add widgets
        
        layout = QVBoxLayout()
        layout.addWidget(self.current_time_label)
        layout.addWidget(self.text1)
        layout.addWidget(self.edit1)
        layout.addWidget(self.text2)
        layout.addWidget(self.edit2)
        layout.addWidget(self.button)


        self.setLayout(layout)
        self.button.clicked.connect(self.Reminder)

    def greetings(self):
            print(f"Hello {self.edit1.text()} and {self.edit2.text()}")

    def Reminder(self):
        current_time = datetime.now().strftime('%H:%M')
        while True:
            if current_time == self.edit1:
                print("⏰REMINDER.....")
                print(self.edit2)
            else:
                print(current_time)
                sys.exit()
            break 

            time.sleep(30)
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("<font color=red size=50>Hello World</font>",
#                                      alignment=QtCore.Qt.AlignCenter)

#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)

#         self.button.clicked.connect(self.magic)

#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())


    # app = QtWidgets.QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    # sys.exit(app.exec())

# -----------Faltantes----------------
# Falta crear el widget de recordatorio
# modificar la funcion Reminder
