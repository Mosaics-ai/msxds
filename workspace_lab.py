import os 
import pandas as pd
import ETL_engine as EE
from connect_minio import minio_connect

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

		self.status = True

	def fetch_df_from_minio(self):

		df = minio_connect().get_df(
        	csvName = 'superstore_dataset_formattedID.csv'
    	)	

		return df

	def execute_from_minio(self):

		# Create data frame
		df = self.fetch_df_from_minio()

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
		df = self.fetch_df_from_minio()
		column_hash = EE.hashing(df = df)
		index = column_hash.column_hasher(
			col_list = [
				"formattedID",
				"State",
				"Country",
			],
			return_type = "data frame"
		)
		print(colors.GREEN + "Column Hash test passed" + colors.END)
		# except Exception as e:
		# 	print(colors.RED)
		# 	print(e)
		# 	print("Column Hash Failed" + colors.END)

		# Test binning function
		df = self.fetch_df_from_minio()
		binning = EE.binner(df = df)
		bin_df = binning.bin_columns(return_type = "data frame")
		print(colors.GREEN + "Binning test passed" + colors.END)

		# Test null handling function
		df = self.fetch_df_from_minio()
		n = EE.null_handler(df = df)
		n.return_null_list()
		print(colors.GREEN + "Null handler test passed" + colors.END)

		# Test imputing mean/mode function
		df = self.fetch_df_from_minio()
		fill_empty = EE.fill_empties(df = df)
		filled = fill_empty.iterate_cols(return_type = "data frame")
		print(colors.GREEN + "Impute mean/mode test passed" + colors.END)

		# Test standardization function
		df = self.fetch_df_from_minio()
		standardized = EE.standardization(df = df)
		standardized.normalize(return_type = "data_frame")
		print(colors.GREEN + "Standardization test passed" + colors.END)

		# Test datepart function
		df = self.fetch_df_from_minio()
		dateparts = EE.datepart_extractor(df = df)
		dateparts = dateparts.return_datepart_cols(
			col_list = [
				"Order Date", 
				"Ship Date",
			],
			return_type = "data frame"
		)
		print(colors.GREEN + "Dateparts test passed" + colors.END)

	def execute(self):

		os.chdir("test datasets")

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

class testing_minio_connection:
	"""
	- Going to be cleaning data science functions in different orders
	- Each 'iteration' is a different variation of testing cleaning in different order
	"""
	def __init__(self):

		# First need to import initial dataset
		self.df = minio_connect().get_df(
        	csvName = 'superstore_dataset_formattedID.csv'
    	)	

	def iteration_0(self):
		"""
		0) Binning
		1) Normalization
		2) Datepart extractor
		"""
		# Binning
		self.df = EE.binner(df = self.df).bin_columns(return_type = "data frame")

		# Normalization.  --   can't really normalize after binning
		self.df = EE.standardization(df = self.df).normalize(return_type = "data frame")

		# Datepart extractor
		self.df = EE.datepart_extractor(df = self.df).return_datepart_cols(
			col_list = [
				"Order Date", 
				"Ship Date",
			],
			return_type = "data frame"
		)
		return self.df

	def iteration_1(self):
		"""
		0) null handler
		1) fill empties
		2) binning
		3) 
		"""

		return 


if __name__ == "__main__":

	# Function that executes by querying from minio
	# test().execute_from_minio()

	# Testing different iterations of data cleaning and uploading to Minio
	df = testing_minio_connection().iteration_0()