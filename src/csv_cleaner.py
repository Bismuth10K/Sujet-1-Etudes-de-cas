import os

import pandas as pd

data_dir = "../Data/"
datas = os.listdir(data_dir)

for file in datas:
	if file.endswith('.csv'):
		print(file)
		df = pd.read_csv(data_dir + file, sep=";")
		df = df.replace('mq', None)
		df.to_csv(data_dir + file, index=False)
