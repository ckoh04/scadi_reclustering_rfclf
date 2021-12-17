import pandas as pd
import numpy as np

df = pd.read_csv("SCADI.csv")
df = df.drop(["Gender", "Age", "Classes"], axis = 1)
#df["Anomaly"] = 1
#df.loc[df["Classes"] == "class7", "Anomaly"] = 0
df = df.to_numpy()
print(df)



np.save('SCADI.npy',df)
#df.to_csv("SCADI_edited.csv", sep=',', encoding='utf-8', index=False)
print(np.genfromtxt("SCADI_edited.csv", delimiter = ","))

