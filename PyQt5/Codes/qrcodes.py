from PyQt5.QtWidgets import*
from qr_python import Ui_Form


class code(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)




app=QApplication([])
window=code()
window.show()
app.exec_()