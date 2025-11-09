from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QTabWidget
from PyQt5.QtGui import QFont
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd
from core.systeme_lineaire import solve_with_numpy, solve_with_gauss
from core.programmation_lineaire import solve_linear_program
from core.regression_lineaire import perform_regression
from core.processus_stochastique import simulate_markov_chain

class MathApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Mathématique Scientifique")
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(self.create_systeme_tab(), "Système Linéaire")
        self.tabs.addTab(self.create_programmation_tab(), "Programmation Linéaire")
        self.tabs.addTab(self.create_regression_tab(), "Régression Linéaire")
        self.tabs.addTab(self.create_processus_tab(), "Processus Stochastique")

    def create_systeme_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.result_label_sys = QLabel("Résultat:")
        self.result_label_sys.setFont(QFont("Arial", 12))
        layout.addWidget(self.result_label_sys)
        btn = QPushButton("Calculer AX = b")
        btn.clicked.connect(self.solve_systeme)
        layout.addWidget(btn)
        tab.setLayout(layout)
        return tab

    def solve_systeme(self):
        A = np.array([[2, -1, 3], [1, 0, 1], [3, 2, -2]])
        b = np.array([5, 6, 4])
        x = solve_with_numpy(A, b)
        self.result_label_sys.setText(f"Solution: {x}")

    def create_programmation_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.result_label_prog = QLabel("Résultat:")
        self.result_label_prog.setFont(QFont("Arial", 12))
        layout.addWidget(self.result_label_prog)
        btn = QPushButton("Résoudre le programme linéaire")
        btn.clicked.connect(self.solve_programmation)
        layout.addWidget(btn)
        tab.setLayout(layout)
        return tab

    def solve_programmation(self):
        result = solve_linear_program("max")
        self.result_label_prog.setText(f"Résultat: {result}")

    def create_regression_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.result_label_reg = QLabel("Résultat:")
        self.result_label_reg.setFont(QFont("Arial", 12))
        layout.addWidget(self.result_label_reg)
        btn = QPushButton("Charger CSV et calculer la régression")
        btn.clicked.connect(self.solve_regression)
        layout.addWidget(btn)
        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)
        tab.setLayout(layout)
        return tab

    def solve_regression(self):
        data = pd.read_csv("data/exemple_donnees.csv")
        X = data[["x"]].values
        y = data["y"].values
        coef, intercept = perform_regression("data/exemple_donnees.csv").values()
        self.result_label_reg.setText(f"y = {coef:.2f}x + {intercept:.2f}")
        plt.clf()
        plt.scatter(X, y, label='Données')
        plt.plot(X, coef * X + intercept, color='red', label='Régression')
        plt.legend()
        self.canvas.draw()

    def create_processus_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.result_label_proc = QLabel("Trajectoire:")
        self.result_label_proc.setFont(QFont("Arial", 12))
        layout.addWidget(self.result_label_proc)
        btn = QPushButton("Simuler chaîne de Markov")
        btn.clicked.connect(self.solve_processus)
        layout.addWidget(btn)
        tab.setLayout(layout)
        return tab

    def solve_processus(self):
        P = np.array([[0.1, 0.6, 0.3], [0.4, 0.4, 0.2], [0.3, 0.3, 0.4]])
        trajectory = simulate_markov_chain(P, initial_state=0, steps=10)
        self.result_label_proc.setText(f"États: {trajectory}")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = MathApp()
    window.show()
    app.exec_()