import pandas as pd
from sklearn.linear_model import LinearRegression

def perform_regression(csv_path):
    """Lit un fichier CSV et retourne les coefficients d'une régression linéaire simple."""
    data = pd.read_csv(csv_path)
    X = data[["x"]].values
    y = data["y"].values
    model = LinearRegression()
    model.fit(X, y)
    return {"coef": model.coef_[0], "intercept": model.intercept_}

if __name__ == "__main__":
    result = perform_regression("data/exemple_donnees.csv")
    print(result)
