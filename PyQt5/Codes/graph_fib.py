from PyQt5.QtWidgets import*
from form_python import Ui_Form


class page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)




app=QApplication([])
window=page()
window.show()
app.exec_()