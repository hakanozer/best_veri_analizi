from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)
        self.resize(506, 304)
        self.btnLogin.clicked.connect(self.login)   

    def login(self):
        username = self.plainTextEdit.toPlainText()
        password = self.plainTextEdit_2.toPlainText()
        # alert ile kullanıcı adı ve şifreyi göster
        print(f"Kullanıcı Adı: {username}, Şifre: {password}")
        if username == "admin" and password == "admin":
            print("Giriş başarılı")
        else:
            print("Giriş başarısız")
                

app = QApplication([])
window = App()
window.show()
app.exec_()