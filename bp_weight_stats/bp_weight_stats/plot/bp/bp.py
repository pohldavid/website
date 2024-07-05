import pandas as pd
import matplotlib.pyplot as plt


bp = pd.read_csv("bp.csv", index_col=0, parse_dates=True)

print(bp)

bp.plot()
plt.show()
#plt.savefig("bpchart.png")
