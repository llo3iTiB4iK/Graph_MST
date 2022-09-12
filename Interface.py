from Graph import*
from PyQt5 import QtCore, QtGui, QtWidgets

class Interface(object):
    def setupUi(self, MainWindow): # налаштовує головне вікно
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
            "border-color: rgb(0, 0, 0);")
# полотно в головному вікні
        self.__centralwidget = QtWidgets.QWidget(MainWindow)
# кнопка виходу з програми
        self.__EXITbutton=QtWidgets.QPushButton(self.__centralwidget)
        self.__EXITbutton.setGeometry(QtCore.QRect(675, 525, 100, 50))
        self.__EXITbutton.setStyleSheet("background-color: rgb(0, 0, 0);\n" "color:rgb(255, 255, 255);\n" "font-size: 22px;")
        self.__EXITbutton.clicked.connect(MainWindow.close)
# напис "Ініціалізація зваженого звязного неорієнтованого графа таблицею ваг:"
        self.__label0 = QtWidgets.QLabel(self.__centralwidget)
        self.__label0.setGeometry(QtCore.QRect(50, 0, 721, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.__label0.setFont(font)
        self.__label0.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                  "color: rgb(170, 255, 255);")
        self.__label0.setAlignment(QtCore.Qt.AlignCenter)
# напис "Кількість вершин графа = "
        self.__label_1 = QtWidgets.QLabel(self.__centralwidget)
        self.__label_1.setGeometry(QtCore.QRect(130, 60, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.__label_1.setFont(font)
        self.__label_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                   "color: rgb(255, 255, 255);")
        self.__label_1.setAlignment(QtCore.Qt.AlignCenter)
# поле вводу кількості вершин графа
        self.__choose_V = QtWidgets.QLineEdit(self.__centralwidget)
        self.__choose_V.setGeometry(QtCore.QRect(430, 60, 100, 31))
        font.setPointSize(14)
        self.__choose_V.setFont(font)
        self.__choose_V.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.__choose_V.setAlignment(QtCore.Qt.AlignCenter)
# кнопка підтвердження кількості вершин графа
        self.__OKbutton = QtWidgets.QPushButton(self.__centralwidget)
        self.__OKbutton.setGeometry(QtCore.QRect(600, 60, 71, 31))
        self.__OKbutton.setStyleSheet("background-color: rgb(222, 253, 255);")
        self.__OKbutton.clicked.connect(lambda: self.__Confirm_n())
# матриця з однорядкових полів вводу
        self.__WM = []  # створення матриці полів вводу розміру 20х20
        for i in range(20):
            tmp = []
            for j in range(20):
                self.__element = QtWidgets.QLineEdit(self.__centralwidget)
                self.__element.setAlignment(QtCore.Qt.AlignCenter)
                self.__element.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.__element.setVisible(False)
                if i>=j:
                    self.__element.setEnabled(False)
                tmp += [self.__element]
            self.__WM += [tmp]
# кнопка підтвердження вводу матриці ваг
        self.__OKbutton2 = QtWidgets.QPushButton(self.__centralwidget)
        self.__OKbutton2.setGeometry(QtCore.QRect(650, 300, 71, 50))
        self.__OKbutton2.setStyleSheet("background-color: rgb(222, 253, 255);")
        self.__OKbutton2.setVisible(False)
        self.__OKbutton2.setEnabled(False)
        self.__OKbutton2.clicked.connect(lambda: self.__Confirm_Matrix())
# випадаючий список з вибором алгоритма
        self.__ALGORITHM_CHOOSE = QtWidgets.QComboBox(self.__centralwidget)
        self.__ALGORITHM_CHOOSE.setGeometry(QtCore.QRect(150, 60, 401, 31))
        self.__ALGORITHM_CHOOSE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.__ALGORITHM_CHOOSE.addItem("(оберіть алгоритм)")
        self.__ALGORITHM_CHOOSE.addItem("Алгоритм Прима")
        self.__ALGORITHM_CHOOSE.addItem("Алгоритм Краскала")
        self.__ALGORITHM_CHOOSE.addItem("Алгоритм Борувки")
        self.__ALGORITHM_CHOOSE.setEnabled(False)
        self.__ALGORITHM_CHOOSE.setVisible(False)
# кнопка підтвердження вибору алгоритма
        self.__OKbutton3 = QtWidgets.QPushButton(self.__centralwidget)
        self.__OKbutton3.setGeometry(QtCore.QRect(600, 60, 71, 31))
        self.__OKbutton3.setStyleSheet("background-color: rgb(222, 253, 255);")
        self.__OKbutton3.setEnabled(False)
        self.__OKbutton3.setVisible(False)
#кнопка виводу у файл
        self.__OUTPUTbutton=QtWidgets.QPushButton(self.__centralwidget)
        self.__OUTPUTbutton.setGeometry(QtCore.QRect(675, 225, 100, 50))
        self.__OUTPUTbutton.setStyleSheet("background-color: rgb(222, 253, 255);")
        self.__OUTPUTbutton.setEnabled(False)
        self.__OUTPUTbutton.setVisible(False)
#кнопка показу аналітичних даних алгоритму
        self.__analytic_data_button=QtWidgets.QPushButton(self.__centralwidget)
        self.__analytic_data_button.setGeometry(QtCore.QRect(675, 325, 100, 50))
        self.__analytic_data_button.setStyleSheet("background-color: rgb(222, 253, 255);")
        self.__analytic_data_button.setEnabled(False)
        self.__analytic_data_button.setVisible(False)
#кнопка показу загальної ваги дерева
        self.general_weight=QtWidgets.QPushButton(self.__centralwidget)
        self.general_weight.setGeometry(QtCore.QRect(675,425,100,50))
        self.general_weight.setStyleSheet("background-color: rgb(222, 253, 255);")
        self.general_weight.setText("Вага MST")
        self.general_weight.setVisible(False)

        MainWindow.setCentralWidget(self.__centralwidget) # встановлюємо centralwidget головним полотном
        self.__retranslateUi(MainWindow)

    def __retranslateUi(self, MainWindow): #встановлює тексти нашим віджетам
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Знаходження MST графа"))
        self.__EXITbutton.setText(_translate("MainWindow", "ВИХІД"))
        self.__label0.setText(_translate("MainWindow", "Ініціалізація зваженого звязного неорієнтованого графа таблицею ваг:"))
        self.__label_1.setText(_translate("MainWindow", "Кількість вершин графа = "))
        self.__OKbutton.setText(_translate("MainWindow", "OK"))
        self.__OKbutton2.setText(_translate("MainWindow", "OK"))
        self.__OKbutton3.setText(_translate("MainWindow", "OK"))
        self.__OUTPUTbutton.setText(_translate("MainWindow", "Вивести у файл"))
        self.__analytic_data_button.setText(_translate("MainWindow", "Аналітичні дані"))

    def __Confirm_n(self): #функція підтвердження розмірності графа та виклику подальших дій
        try:
            number=int(self.__choose_V.text()) #отримуємо з поля вводу кількість вершин
        except ValueError: #якщо в полі вводу дані, які не можна перетворити в ціле число
            self.__wrong_input("Введені некоректні дані") #виводимо відповідну помилку
            return
        if number<1:
            self.__wrong_input("Неможливо створити граф з такою кількістю вершин")
            return
        elif number==1:
            self.__wrong_input("Граф з однієї точки не є коректним")
            return
        self.__graph = Graph(number)
        self.__choose_V.setEnabled(False)
        if number<=20:
            self.__OKbutton.setText("Очистити") #функція підтвердження кількості вершин при повторному натисканні буде обнуляти матрицю ваг
            self.__Draw_Matr()
            self.__matrix_fill_info()
            self.__OKbutton2.setVisible(True)
            self.__OKbutton2.setEnabled(True)
        else: #якщо число вершин більше за 20
            self.__OKbutton.setEnabled(False)
            self.__matrix_fill_info()
            self.__graph.rand_gener() #випадково генеруємо матрицю ваг для нашого графа
            self.__START()

    def __wrong_input(self, text:str):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle("Помилка(...)")
        msg.exec_()

    def __matrix_fill_info(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if self.__graph.V<=20:
            msg.setText("Заповніть матрицю ваг графа")
            msg.setInformativeText(
                "Число на перетині рядка і стовпчика позначає вагу ребра між відповідними вершинами, inf-несуміжні вершини.\n"
                "Оскільки граф неорієнтований, його матриця ваг відобразиться симетрично відносно головної діагоналі. Петлі не є доступними і під час виконання програми будуть ігноруватися.")
            msg.setWindowTitle("Перед продовженням...")
        else:
            msg.setText("Для кількості вершин n>20 граф буде згенеровано випадковим чином, матриця ваг буде виведена у файл in.txt.")
            msg.setWindowTitle("Довідка")
        msg.exec_()

    def __Draw_Matr(self): #малювання шаблона матриці ваг та назначення для її клітинок значень за замовчуванням
        width_of_cell = int(600 // self.__graph.V)
        height_of_cell = int(450 // self.__graph.V)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(height_of_cell // 3) #адаптуємо розмір шрифту до розміру клітинки
#розміщаємо у вікні та робим видимими елементи матриці полів вводу
        for i in range(self.__graph.V):
            for j in range(self.__graph.V):
                self.__WM[i][j].setGeometry(10 + j * width_of_cell, 110 + i * height_of_cell, width_of_cell, height_of_cell)
                self.__WM[i][j].setFont(font)
                self.__WM[i][j].setVisible(True)
#встновлюємо значення елементів матриці за замовчуванням
                if i == j:
                    self.__WM[i][j].setText("0")
                else:
                    self.__WM[i][j].setText("inf")

    def __Confirm_Matrix(self): #підтвердження матриці
        for i in range(self.__graph.V):
            for j in range(i, self.__graph.V):
                try:    #пробуємо перетворити вміст клітинки в float
                    if i!=j:
                        self.__graph.WeightMatr[i].append(float(self.__WM[i][j].text()))
                        self.__graph.WeightMatr[j].append(float(self.__WM[i][j].text()))
                        if self.__graph.WeightMatr[i][j]!=float('inf'):
                            self.__graph.edge_list.append((i, j))
                    else:
                        self.__graph.WeightMatr[i].append(float(self.__WM[i][j].text()))
                except ValueError:
                    self.__incorrect_input_error(i + 1, j + 1, "Введене число не можна перетворити в число з плаваючою крапкою!")
                    self.__graph.graph_clear()
                    return
                self.__WM[j][i].setText(self.__WM[i][j].text()) #віддзеркалюємо матрицю полів вводу
        if not(self.__graph.is_connected()):  # перевірка цього графа на зв'язність
            self.__not_connected_error()
            self.__graph.graph_clear()
            return
        for i in range(self.__graph.V):
            for j in range(self.__graph.V):
                self.__WM[i][j].setEnabled(False) #робимо матрицю полів вводу незмінюваною
        self.__START()

    def __incorrect_input_error(self, row, column, text): #помилка некоректного ведення в клітинку (row,column) матриці полів вводу
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Некоректне введення даних в клітинку (" + str(row) + ',' + str(column) + ')')
        msg.setInformativeText(text)
        msg.setWindowTitle("Помилка(...)")
        msg.exec_()

    def __not_connected_error(self): #помилка незв'язності введеного графа
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Даний граф не є зв'язним")
        msg.setInformativeText("Не всі вершини у графі є досяжними...")
        msg.setWindowTitle("Помилка(...)")
        msg.exec_()

    def __START(self):
        self.__graph_file_output()  # виводимо матрицю ваг нашого графа у файл "in.txt"
        if self.__graph.V<=20:
            self.__graph.Visualise() #малюємо наш граф
        self.__Window_Update() #оновлюємо вигляд нашого вікна
        self.__OKbutton3.clicked.connect(lambda: self.__algorithm())

    def __Window_Update(self):
        self.__label0.setText("Яким алгоритмом будемо знаходити MST?") #змінюємо текст напису зверху
#видаляємо всі непотрібні надалі елементи
        self.__label_1.deleteLater()
        self.__choose_V.deleteLater()
        self.__OKbutton.deleteLater()
        self.__OKbutton2.deleteLater()
#робимо вибір алгоритму доступним
        self.__ALGORITHM_CHOOSE.setEnabled(True)
        self.__ALGORITHM_CHOOSE.setVisible(True)
#робимо кнопку підтвердження вибору алгоритму доступною
        self.__OKbutton3.setEnabled(True)
        self.__OKbutton3.setVisible(True)

    def __algorithm(self):
        msg = QtWidgets.QMessageBox()
        if self.__ALGORITHM_CHOOSE.currentIndex()!=0:
            self.__graph.MST_find(self.__ALGORITHM_CHOOSE.currentIndex()) #передаємо в функцію знаходження MST потрібний аргумент-алгоритм
            self.__ALGORITHM_CHOOSE.setEnabled(False) #робимо вибір алгоритма недоступним
            self.__OKbutton3.setEnabled(False) #робимо кнопку підтвердження вибору алгоритму недоступною
            if self.__graph.V<=20: #якщо кількість вершин менша 20, виводимо на екран матрицю ваг найкоротшого остовного дерева
                for i in range(self.__graph.V):
                    for j in range(self.__graph.V):
                        self.__WM[i][j].setText(str(self.__graph.MST_Matr[i][j]))
# вмикаємо кнопку виводу у файл і привязуємо до її сигналу операцію виводу у файл
            self.__OUTPUTbutton.setVisible(True)
            self.__OUTPUTbutton.setEnabled(True)
            self.__OUTPUTbutton.clicked.connect(self.__MST_file_output)
# вмикаємо кнопку показу аналітичних даних роботи алгоритму
            self.__analytic_data_button.setVisible(True)
            self.__analytic_data_button.setEnabled(True)
            self.__analytic_data_button.clicked.connect(lambda: self.__analytic_data(self.__ALGORITHM_CHOOSE.currentIndex()))

            self.general_weight.setVisible(True)
            self.general_weight.clicked.connect(lambda: self.weight_show())

# виводимо коритувачеві повідомлення з поясненням
            msg.setIcon(QtWidgets.QMessageBox.Question)
            if self.__graph.V<=20:
                msg.setText("Перед вами початковий граф, його найкоротше остовне дерево (червоні ребра) та матриця ваг цього остова.\n"
                            "Також ви можете вивести матрицю ваг MST та поточний малюнок у файл, а також переглянути статистичні дані роботи алгоритму.")
            else:
                msg.setText("Найкоротше остовне дерево графа знайдено, для перегляду виведіть його у файл")
            msg.setWindowTitle("Довідка")
            msg.exec_()
        else:
#якщо користувач не обрав алгоритм - виводимо йому повідомлення, що треба вибрати алгоритм
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Оберіть алгоритм")
            msg.setWindowTitle("...")
            msg.exec_()

    def __graph_file_output(self): #вивід матриці ваг початкового графа у файл "in.txt"
        with open('in.txt','w') as file:
            for i in range(len(self.__graph.WeightMatr)):
                tmp=" ".join(map(str, self.__graph.WeightMatr[i]))
                file.write(tmp)
                if i != len(self.__graph.WeightMatr) - 1:
                    file.write('\n')
# виводимо повідомлення про успішний вивід
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Матриця ваг графа успішно виведена у файл in.txt (в кореневому каталозі програми).")
        msg.setWindowTitle(" ")
        msg.exec_()

    def __MST_file_output(self): # вивід у файл "out.txt" матриці ваг MST
        with open('out.txt','w') as file:
            for i in range(len(self.__graph.MST_Matr)):
                tmp=" ".join(map(str, self.__graph.MST_Matr[i]))
                file.write(tmp)
                if i != len(self.__graph.MST_Matr) - 1:
                    file.write('\n')
        if self.__graph.V<=20:
            plt.savefig("MST.png") #виводимо у файл "MST.png" наш малюнок - граф та MST
# виводимо повідомлення про успішний вивід та деактивуємо кнопку виводу
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if self.__graph.V<=20:
            msg.setText("Матриця ваг MST успішно виведена у файл out.txt, результуючий граф у файл MST.png (в кореневому каталозі програми).")
        else:
            msg.setText("Матриця ваг MST успішно виведена у файл out.txt (в кореневому каталозі програми).")
        msg.setWindowTitle("Готово")
        msg.exec_()
        self.__OUTPUTbutton.setEnabled(False)

    def __analytic_data(self,num): #показ аналітичних даних алгоритму
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if num==1:
            msg.setText("Алгоритм Прима\nКількість ітерацій = " + str(self.__graph.iterations))
        elif num==2:
            msg.setText("Алгоритм Краскала\nКількість ітерацій = " + str(self.__graph.iterations))
        else:
            msg.setText("Алгоритм Борувки\nКількість ітерацій = " + str(self.__graph.iterations))
        msg.setWindowTitle("Статистичні дані")
        msg.exec_()

    def weight_show(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Вага найкоротшого остовного дерева = "+str(int(self.__graph.MST_weight)))
        msg.setWindowTitle("Вага MST")
        msg.exec_()