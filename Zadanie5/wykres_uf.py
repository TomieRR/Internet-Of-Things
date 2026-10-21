from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
tabela = pd.read_csv(folder / "pomiary_uf.csv", sep=";", decimal=",")
tabela = tabela.sort_values("U_V")

# Przeliczamy p po ewentualnej zmianie U lub f w CSV.
tabela["p_Hz_V"] = tabela["f_Hz"] / tabela["U_V"]
p_srednie = tabela["p_Hz_V"].mean()
print(tabela.to_string(index=False))
print(f"\nŚrednie p = {p_srednie:.4f} Hz/V")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

ax1.plot(tabela["U_V"], tabela["f_Hz"], "o-", color="tab:blue")
ax1.set_title("Przetwornik U/f — częstotliwość w zależności od napięcia")
ax1.set_ylabel("Częstotliwość f [Hz]")
ax1.grid(alpha=0.3)

ax2.plot(tabela["U_V"], tabela["p_Hz_V"], "o-",
         color="tab:orange", label="p = f/U")
ax2.axhline(p_srednie, color="black", linestyle="--",
            label=f"Średnie p = {p_srednie:.2f} Hz/V")
for _, wiersz in tabela.iterrows():
    ax2.annotate(wiersz["pomiar"],
                 (wiersz["U_V"], wiersz["p_Hz_V"]),
                 xytext=(5, 7), textcoords="offset points")
ax2.set_title("Współczynnik przetwarzania w zależności od napięcia")
ax2.set_xlabel("Napięcie U [V]")
ax2.set_ylabel("Współczynnik p [Hz/V]")
ax2.grid(alpha=0.3)
ax2.legend()

fig.tight_layout()
fig.savefig(folder / "wykres_uf.png", dpi=200)
plt.show()
