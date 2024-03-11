import numpy
import pandas as pd
import numpy as np

data_dir = "../Data/"

jan = pd.read_csv(data_dir + "synop.202301.csv")

print(jan)
print(jan.loc[:, 't'])
