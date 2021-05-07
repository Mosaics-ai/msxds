import os 
import pandas as pd
import ETL_engine as EE

class colors:
	RED = "\033[91m"
	BLUE = "\033[94m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	END = "\033[0m"

class test:

	def __init__(self):

		os.chdir("test datasets")

	def execute(self):

		# Create data frame
		df = pd.read_csv("superstore_dataset_formattedID.csv")
		df = pd.DataFrame(df)

		# Instatiate hash class
		id_hash = EE.hashing(
			df = df
		)
		new_df = id_hash.returnHashed_ID_df(
			ID_col_name = "formattedID"
		)
		print(colors.GREEN + "Hashing ID test passed" + colors.END)

		# Test column hasher
		# Create data frame
		# try:
		df = pd.read_csv("superstore_dataset_formattedID.csv")
		df = pd.DataFrame(df)
		column_hash = EE.hashing(df = df)
		index = column_hash.column_hasher(
			col_list = [
				"formattedID",
				"State",
				"Country",
			]
		)
		print(colors.GREEN + "Column Hash test passed" + colors.END)
		# except Exception as e:
		# 	print(colors.RED)
		# 	print(e)
		# 	print("Column Hash Failed" + colors.END)

		# Test binning function
		df = pd.read_csv("superstore_dataset_formattedID.csv")
		df = pd.DataFrame(df)
		binning = EE.binner(df = df)
		binning.bin_columns()
		print(colors.GREEN + "Binning test passed" + colors.END)

		# Test null handling function
		df = pd.read_csv("superstore_dataset_formattedID.csv")
		df = pd.DataFrame(df)
		n = EE.null_handler(df = df)
		n.return_null_list()
		print(colors.GREEN + "Null handler test passed" + colors.END)

		# Test imputing mean/mode function
		df = pd.read_csv("superstore_dataset_formattedID.csv")
		df = pd.DataFrame(df)
		fill_empty = EE.fill_empties(df = df)
		filled = fill_empty.iterate_cols()
		print(colors.GREEN + "Impute mean/mode test passed" + colors.END)

		# Test standardization function
		df = pd.read_csv("superstore_dataset_formattedID.csv")
		df = pd.DataFrame(df)
		standardized = EE.standardization(df = df)
		standardized.normalize()
		print(colors.GREEN + "Standardization test passed" + colors.END)

		# Test datepart function
		df = pd.read_csv("superstore_dataset_formattedID.csv")
		df = pd.DataFrame(df)
		dateparts = EE.datepart_extractor(df = df)
		dateparts = dateparts.return_datepart_cols(
			col_list = [
				"Order Date", 
				"Ship Date",
			]
		)
		print(colors.GREEN + "Dateparts test passed" + colors.END)

if __name__ == "__main__":

	test().execute()