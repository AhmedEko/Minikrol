from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from home import Ui_MainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #page2 qwidget hover effects

        #connect exit_btn to exit_app
        self.ui.exit_btn.clicked.connect(self.exit_app)
    

    def exit_app(self):
        #check if user wants to exit via a message box
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            #terminate the app
            sys.exit()
        else:
            #do nothing
            pass
        

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())