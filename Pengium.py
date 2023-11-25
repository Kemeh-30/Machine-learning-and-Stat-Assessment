import numpy as np
from scipy.stats import ttest_ind

# Assuming you have the total body mass for male and female gentoo penguins
male_total_mass = 1437000 # Replace with the actual total mass for males
female_total_mass = 1427850  # Replace with the actual total mass for females

# Assuming you also have the number of penguins in each group
num_male_penguins = 168 # Replace with the actual number of male penguins
num_female_penguins = 165  # Replace with the actual number of female penguins

# Calculate the mean body mass for each group
mean_male_mass = male_total_mass / num_male_penguins
mean_female_mass = female_total_mass / num_female_penguins

# Perform independent t-test
t_statistic, p_value = ttest_ind([mean_male_mass] * num_male_penguins, [mean_female_mass] * num_female_penguins)

# Print the results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

# Check for significance
alpha = 0.05
if p_value < alpha:
    print("There is significant evidence of a difference in mean body mass between male and female gentoo penguins.")
else:
    print("There is no significant evidence of a difference in mean body mass between male and female gentoo penguins.")