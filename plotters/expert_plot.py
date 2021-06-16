import pandas as pd
import matplotlib.pyplot as plt
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = parentdir + "/results/expert_3.csv"

df = pd.read_csv(path)
x = [i for i in range(3, 51, 2)]
plt.plot(x, df.p_log, label="Price Log")
plt.plot(x, df.n_lin, label="Nash Linear")
plt.plot(x, df.n_log, label="Nash Log")
plt.plot(x, df.elec, label="Election / Price Linear")
plt.xlabel("N agents")
plt.ylabel("Accuracy (1000 trials)")
plt.legend()
plt.show()
