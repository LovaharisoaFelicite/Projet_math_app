from PyQt5.QtWidgets import QApplication
from ui.main_window import MathApp

app = QApplication([])
window = MathApp()
window.show()
app.exec_()
