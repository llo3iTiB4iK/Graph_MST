from Interface import*

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) #додаток
    MainWindow = QtWidgets.QMainWindow() #головне вікно додатка
    IF = Interface() #створюємо свій об'єкт-інтерфейс
    IF.setupUi(MainWindow) #налаштовуємо наше вікно
    MainWindow.show() #показуємо вікно
    sys.exit(app.exec_()) #завжди коректний вихід