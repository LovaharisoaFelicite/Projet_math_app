from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, LpStatus, value

def solve_linear_program(mode="max"):
    """
    Résout un problème de programmation linéaire simple.
    Exemple fictif : 
        max z = 3x + 2y 
        sous contraintes : 
            x + y <= 4
            3x + 2y <= 12
            x, y >= 0
    """
    # Créer le problème
    if mode == "max":
        prob = LpProblem("Programme_Linéaire", LpMaximize)
    else:
        prob = LpProblem("Programme_Linéaire", LpMinimize)

    # Variables
    x = LpVariable("x", lowBound=0)
    y = LpVariable("y", lowBound=0)

    # Fonction objectif
    prob += 3*x + 2*y

    # Contraintes
    prob += x + y <= 4
    prob += 3*x + 2*y <= 12

    # Résoudre
    prob.solve()

    if LpStatus[prob.status] == "Optimal":
        return {"x": value(x), "y": value(y)}
    else:
        return None

# Test rapide
if __name__ == "__main__":
    result = solve_linear_program("max")
    print("Solution:", result)

