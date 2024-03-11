import os
import pandas as pd

data_dir = "../Data/"
datas = os.listdir(data_dir)


def clean_csv():
	for file in datas:
		if file.endswith('.csv') and file != "synop.csv":
			print(file)
			df = pd.read_csv(data_dir + file, sep=";")
			df = df.replace('mq', None)
			df.to_csv(data_dir + file, index=False)


def concat_all_csv():
	final_df = pd.concat([pd.read_csv(data_dir + file) for file in datas], ignore_index=True)
	final_df.to_csv(data_dir + "synop.csv", index=False)


concat_all_csv()
