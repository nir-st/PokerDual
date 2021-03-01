import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow


app = QApplication(sys.argv)

demo = MainWindow(app)
demo.show()

sys.exit(app.exec_())
