import numpy as np
from scipy.stats import chi2_contingency

# Create a 2D array (contingency table) with the provided data
observed = np.array([[43, 57], [56, 45]])

# Perform the chi-squared test
chi2, p, dof, expected = chi2_contingency(observed)

# Print the results
print(f"Chi-squared statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)
