import numpy as np
import krippendorff

# Each ROW is one scorer. Each COLUMN is one item (one PC in one test case).
# Scores are 0 to 3. These numbers are MADE UP, for practice only.

# Scorers who disagree a lot (like Round 1, no rubric)
disagree = np.array([
    [3, 0, 2, 1, 3],
    [1, 2, 0, 3, 1],
    [2, 3, 1, 0, 2],
], dtype=float)

# Scorers who mostly agree (like Round 2, with rubric)
agree = np.array([
    [3, 1, 2, 0, 3],
    [3, 1, 2, 1, 3],
    [3, 1, 2, 0, 2],
], dtype=float)

a_dis = krippendorff.alpha(reliability_data=disagree, level_of_measurement="ordinal")
a_agr = krippendorff.alpha(reliability_data=agree, level_of_measurement="ordinal")

print("Alpha when scorers disagree:", round(a_dis, 2))
print("Alpha when scorers agree:   ", round(a_agr, 2))