import json
import pandas as pd
import numpy as np
from core.systeme_lineaire import solve_with_numpy
from core.programmation_lineaire import solve_linear_program
from core.regression_lineaire import perform_regression
from core.processus_stochastique import simulate_markov_chain

# Test système linéaire
with open("data/systeme_lineaire_test.json", "r") as f:
    data_sys = json.load(f)
A = np.array(data_sys["A"])
b = np.array(data_sys["b"])
sol_sys = solve_with_numpy(A, b)
print("✅ Système Linéaire - Solution:", sol_sys)

# Test programmation linéaire
with open("data/programmation_lineaire_test.json", "r") as f:
    data_prog = json.load(f)
sol_prog = solve_linear_program(data_prog["mode"])
print("✅ Programmation Linéaire - Résultat:", sol_prog)

# Test régression linéaire
result_reg = perform_regression("data/exemple_donnees.csv")
print("✅ Régression Linéaire - Coef:", result_reg["coef"], "Intercept:", result_reg["intercept"])

# Test processus stochastique
with open("data/processus_stochastique_test.json", "r") as f:
    data_proc = json.load(f)
P = np.array(data_proc["P"])
initial_state = data_proc["initial_state"]
steps = data_proc["steps"]
trajectory = simulate_markov_chain(P, initial_state, steps)
print("✅ Processus Stochastique - Trajectoire:", trajectory)