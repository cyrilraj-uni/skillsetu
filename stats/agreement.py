import numpy as np
import krippendorff
import matplotlib
matplotlib.use("Agg")          # lets it save a chart without opening a window
import matplotlib.pyplot as plt

def load(path):
    # skip_header=1 skips the item names; empty cells become nan (missing score)
    return np.genfromtxt(path, delimiter=",", skip_header=1)

def alpha(data):
    return krippendorff.alpha(reliability_data=data, level_of_measurement="ordinal")

round1 = load("data/round1.csv")
round2 = load("data/round2.csv")

a1 = alpha(round1)
a2 = alpha(round2)

print("Round 1 (no rubric):  ", round(a1, 2))
print("Round 2 (with rubric):", round(a2, 2))
print("Scorers:", round1.shape[0], "| Items:", round1.shape[1])

plt.figure(figsize=(5, 4))
plt.bar(["Without rubric", "With rubric"], [a1, a2], color=["#999999", "#1f6f5c"])
plt.axhline(0, color="black", linewidth=0.8)
plt.ylabel("Krippendorff's alpha")
plt.title("Agreement between scorers (pilot)")
plt.ylim(-0.5, 1)
plt.tight_layout()
plt.savefig("stats/agreement_chart.png", dpi=150)
print("Chart saved to stats/agreement_chart.png")