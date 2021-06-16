import pandas as pd
import matplotlib.pyplot as plt
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = parentdir + "/results/acc_2.csv"

df = pd.read_csv(path)
x = [(1+i/1000)/2 for i in range(50)]
plt.plot(x, df.p_log, label="Price Log")
plt.plot(x, df.n_lin, label="Nash Linear")
plt.plot(x, df.n_log, label="Nash Log")
plt.plot(x, df.elec, label="Election / Price Linear")
plt.xlabel("Mean Accuracy")
plt.ylabel("Accuracy of system(2000 trials)")
plt.legend()
plt.show()
