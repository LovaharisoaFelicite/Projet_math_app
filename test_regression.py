from core.regression_lineaire import perform_regression

result = perform_regression("data/exemple_donnees.csv")
print("Coefficient directeur :", result["coef"])
print("Ordonnée à l'origine :", result["intercept"])
