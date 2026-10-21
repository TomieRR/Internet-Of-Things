import pandas as pd
import matplotlib.pyplot as plt

tabela1 = pd.read_csv("tabela1.csv", sep=";", decimal=",")
tabela2 = pd.read_csv("tabela2.csv", sep=";", decimal=",")

tabela1 = tabela1.sort_values("A_V")
tabela2 = tabela2.sort_values("A_V")

tabela1["R_V"] = tabela1["A_V"] - tabela1["B_V"]
tabela2["R_V"] = tabela2["A_V"] - tabela2["B_V"]

plt.figure(figsize=(10, 6))

plt.plot(
    tabela1["A_V"], tabela1["R_V"],
    "o-", label="Tabela 1 — pojedyncze bity"
)
plt.plot(
    tabela2["A_V"], tabela2["R_V"],
    "s-", label="Tabela 2 — kilka bitów"
)

plt.xlabel("Ustawione napięcie A [V]")
plt.ylabel("Różnica R = A − B [V]")
plt.title("Przetwornik BCD — ustawienie vs. błąd")
plt.axhline(0, color="black", linewidth=1)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("bcd_ustawienie_blad.png", dpi=200)
plt.show()