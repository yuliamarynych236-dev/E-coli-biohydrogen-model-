import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Glucose uptake": [5, 10, 15, 20],
    "H2 production": [35.00441, 87.86023, 138.76932, 189.67841]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.plot(
    df["Glucose uptake"],
    df["H2 production"],
    marker="o"
)

plt.xlabel("Glucose uptake (mmol/gDW/h)")
plt.ylabel("H2 production (mmol/gDW/h)")
plt.title("Effect of glucose uptake on hydrogen production")
plt.grid(True)
plt.tight_layout()

plt.savefig("hydrogen_production.png", dpi=300)
plt.show()
