import csv
import random

from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class representing details for the password manager
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor to create the initial save and yes object.
        :param args: None
        :param kwargs: None
        """

        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.save())      # when the user clicked save button
        self.yes_Button.clicked.connect(lambda: self.yes())       # when the user clicked yes  button

    def save(self):
        """
         Method to varify if name and user are valid
        """

        name = self.input_1.text()
        user = self.input_2.text()
        password = self.input_3.text()

        if ".com" in name and "@gmail.com" in user:
            with open("safe_file.csv", "a", newline='') as file:        # save the data on the cvs file
                write = csv.writer(file)
                write.writerow([name, user, password])

        else:
            self.input_3.setText("Invalid link or email")                # in case the email or link are not valid

    def yes(self):
        """
        Method to pick a random password from the text file
        :return: it returns nothing
        """
        with open("passwords.txt", "r") as file:
            keys = file.read()
            words = list(map(str, keys.split()))

            random_st = random.choice(words)

            self.input_3.setText(random_st)




























        #self.label.setText(f'Hello {name}')
        #self.input_2.setText(' ')








