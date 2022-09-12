import networkx as nx
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self,v,WM=None): #конструктор класу граф
        self.V=v #кількість ребер
        if WM==None:
            self.WeightMatr=[[] for i in range(self.V)] #матриця ваг графа
        else:
            self.WeightMatr=WM
        self.MST_Matr=[[float('inf') for i in range(self.V)] for i in range(self.V)] #матриця ваг MST графа
        for i in range(self.V):
            self.MST_Matr[i][i]=float(0) #на головній діагоналі лежать перетини двох однакових вершин
        self.edge_list=[] #для оптимізації роботи алгоритмів створюємо список ребер
        self.iterations=0  #ітерації циклу в алгоритмі знаходження MST
        self.MST_weight=0

    def rand_gener(self): #функція випадкового генерування матриці ваг такої, щоб результуючий граф був зв'язним
        while True:
            for i in range(self.V):
                for j in range(i,self.V):
                    if i==j: #якщо одна і та сама вершина
                        self.WeightMatr[i].append(float(0))
                    else:
                        if random.randint(0,1)==1: #генеруємо значення 0-1, де 0-несуміжні ребра, 1-суміжні; якщо суміжні:
                            weight=float(random.randint(-1000,1000)/10)
                            self.edge_list.append((i,j))
                        else: #якщо ребра несуміжні
                            weight=float('inf')
        #додаємо у матрицю ваг це ребро
                        self.WeightMatr[i].append(weight)
                        self.WeightMatr[j].append(weight)
            if self.is_connected(): #якщо граф зв'язний
                return #закінчуємо генерацію
            else:
                self.graph_clear()

    def is_connected(self): #перевірка графа на зв'язність
# формуємо список суміжності G графа для оптимізації подальшої роботи алгоритму
        G=[[] for i in range(self.V)]
        for (u,v) in self.edge_list:
            G[u].append(v)
            G[v].append(u)
        used = [False] * self.V
        used_num = 1  # кількість використаних вершин
        S = [0]
        used[0] = True
#алгоритм пошуку в глибину
        while (S != []):
            v = S[-1]
            moved_deeper = False
            for i in G[v]:
                if (used[i] == False):
                    moved_deeper = True
                    S.append(i)
                    used[i] = True
                    used_num += 1
                    break
            if moved_deeper == False:
                S.pop()
#якщо при пошуку вглиб були використані всі вершини, то граф є зв'язний
        if used_num == self.V:
            return True
        else:
            return False

    def MST_find(self,ALG): #знаходження MST і показ його на екрані
        if ALG == 1:
            self.__Prim()
        elif ALG == 2:
            self.__Kruskal()
        elif ALG == 3:
            self.__Boruvka()
        if self.V<=20:
            self.__MST_show()

    def __Prim(self):
        visited = [False] * self.V #список маркерів відвідано-не відвідано для кожної вершини
        visited[0] = True
        visited_number = 1  # число відвіданих вершин
        edges=sorted(self.edge_list, key=lambda edge: self.WeightMatr[edge[0]][edge[1]])
        while visited_number < self.V:
            x = 0  # номер вершини-початку ребра яке будемо додавати до MST
            y = 0  # номер вершини-кінця ребра яке будемо додавати до MST
            for (u,v) in edges:
                self.iterations += 1
                if visited[u] and not visited[v]:
                    x = u  # початок найлегшого ребра - початок поточного ребра
                    y = v  # кінець найлегшого ребра - кінець поточного ребра
                    edges.remove((u, v))
                    break
                elif visited[v] and not visited[u]:
                    x = v  # початок найлегшого ребра - початок поточного ребра
                    y = u  # кінець найлегшого ребра - кінець поточного ребра
                    edges.remove((u, v))
                    break
            self.MST_Matr[x][y] = self.MST_Matr[y][x] = self.WeightMatr[x][y]  # додаємо ребро в MST
            self.MST_weight+=self.WeightMatr[x][y]
            visited[y]=True
            visited_number+=1
#якщо кількість вершин графа не більша за 20, то показуємо покрокове знаходження MST
            if self.V <= 20:
                self.__MST_show()

    def __Kruskal(self):
        setMatrix = [] #список компонент зв'язності
        edges = sorted(self.edge_list, key=lambda edge: self.WeightMatr[edge[0]][edge[1]])
        for i in range(self.V):
            setMatrix.append([i])  #спочатку кожна вершина є компонентою
        for (u,v) in edges:
            e0 = -1  # номер компоненти в якій лежить початок мінімального ребра
            e1 = -1  # номер компоненти в якій лежить кінець мінімального ребра
            for i in range(len(setMatrix)):
                self.iterations+=1
                if u in setMatrix[i]:
                    e0 = i
                if v in setMatrix[i]:
                    e1 = i
                if e0!=-1 and e1!=-1:
                    break
            if e0!=e1:  # якщо початок і кінець ребра в різних компонентах, об'єднуємо ці компоненти:
                setMatrix[e0] += setMatrix[e1]
                del setMatrix[e1]
                self.MST_Matr[u][v] = self.MST_Matr[v][u] = self.WeightMatr[u][v]  # додаємо ребро в MST
                self.MST_weight+=self.WeightMatr[u][v]
# якщо кількість вершин графа не більша за 20, то показуємо покрокове знаходження MST
                if self.V <= 20:
                    self.__MST_show()
                if len(setMatrix)==1: #якщо в нас одна компонента, ми знайшли MST
                    return

    def __Boruvka(self):
        setMatrix = []  # список компонент зв'язності
        for i in range(len(self.WeightMatr)):
            setMatrix.append([i])  # спочатку кожна вершина є компонентою
        edges=sorted(self.edge_list, key=lambda edge: self.WeightMatr[edge[0]][edge[1]])
        while len(setMatrix)>1:
            for component in setMatrix: #для кожної компоненти знаходимо мінімальне інцидентне їй ребро
                start=-1  #початок найлегшого ребра між цією компонентою і будь-якою іншою
                end=-1  #кінець найлегшого ребра між цією компонентою і будь-якою іншою
                for (u,v) in edges:
                    self.iterations += 1
                    if u in component and v not in component:
                        start=u
                        end=v
                        edges.remove((u,v))
                        break
                    elif v in component and u not in component:
                        start=v
                        end=u
                        edges.remove((u, v))
                        break
                e0 = -1  # номер компоненти в якій лежить початок мінімального ребра
                e1 = -1  # номер компоненти в якій лежить кінець мінімального ребра
                for i in range(len(setMatrix)):
                    if start in setMatrix[i]:
                        e0 = i
                    if end in setMatrix[i]:
                        e1 = i
                    if e0 != -1 and e1 != -1:
                        break
                if e0 != e1:  # якщо початок і кінець ребра в різних компонентах, об'єднуємо ці компоненти:
                    setMatrix[e0] += setMatrix[e1]
                    del setMatrix[e1]
                    self.MST_Matr[start][end] = self.MST_Matr[end][start] = self.WeightMatr[start][end]  # додаємо ребро в MST
                    self.MST_weight+=self.WeightMatr[start][end]
# якщо кількість вершин графа не більша за 20, то показуємо покрокове знаходження MST
                    if self.V <= 20:
                        self.__MST_show()

    def Visualise(self): #показ графа
        self.__g = nx.Graph()  #створення спецального об'єкта-графа, що використовуватиметься для візуаліації
# ініціалізуємо спеціальний об'єкт граф
        for i in range(self.V):
            self.__g.add_node(i + 1)
        for (i,j) in self.edge_list:
            if self.WeightMatr[i][j] != float('inf'):
                self.__g.add_edge(i + 1, j + 1, weight=self.WeightMatr[i][j])
        nx.draw_shell(self.__g, with_labels=True)  #малюємо граф
        nx.draw_networkx_edge_labels(self.__g, pos=nx.shell_layout(self.__g), font_size=15 - self.V / 2) #пишемо ваги ребер
        plt.axis('off')  #виключаємо осі координат
        plt.show(block=False) #показуємо наш граф

    def __MST_show(self): #показ на графі його найкоротшого остовного дерева
        edge_colors=[] #список кольорів ребер
        node_colors=['#1f78b4' for i in range(self.V)]
        plt.clf() #очистка екрана
        for (i,j) in self.edge_list:
            if self.MST_Matr[i][j] != float('inf'):
                edge_colors+=['red']
                node_colors[i]=node_colors[j]='green'
            else:
                edge_colors+=['black']
        nx.draw_shell(self.__g, with_labels=True, edge_color=edge_colors, node_color=node_colors) #намалювання графа, де MST-червоні ребра
        nx.draw_networkx_edge_labels(self.__g, pos=nx.shell_layout(self.__g), font_size=15 - self.V / 2)  # пишемо ваги ребер
        plt.pause(1)

    def graph_clear(self): # очистка графа (потрібна при некоректній ініціалізації графа)
        for i in range(self.V):
            self.WeightMatr[i].clear()
        self.edge_list.clear()