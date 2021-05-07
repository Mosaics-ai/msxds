from minio import Minio 
import pandas as pd
import io
from io import BytesIO
import os 
import json

class colors:
	RED = "\033[91m"
	BLUE = "\033[94m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	END = "\033[0m"

class minio_connect_fromJson:

	def __init__(self, endpoint, access_key, secret_key, secure, schema):

		self.client = Minio(
			endpoint = endpoint,
			access_key = access_key,
			secret_key = secret_key,
			secure = True
		)
		self.scheme = "/minio"
		self.schema = schema

	def get_df(self, csvName):
		"""
		After connection is established, return dataframe to work with in pandas
		"""
		# Get object from Minio
		csv = self.client.get_object(
			bucket_name = self.schema,
			object_name = csvName
		)

		try:
			# Create pandas data frame
			data = io.StringIO(csv.read().decode('latin-1'))
			df = pd.read_csv(data)
			df = pd.DataFrame(df)
			print(colors.BLUE + "data frame successfully created from Minio connection" + colors.END)

			return df
		except Exception as e:
			print(colors.RED + e + colors.END)

		return False

	def upload_df(self, df, csvName):
		"""
		Establish connection and then upload csv
		Most-likely done after cleaning a dataset and having a new version in Minio

		df has to come in as pandas data frame object
		"""

		csv_bytes = df.to_csv().encode('utf-8')
		csv_buffer = BytesIO(csv_bytes)

		self.client.put_object(
			self.schema,
			self.schema + self.scheme + csvName,
			data=csv_buffer,
			length=len(csv_bytes),
			content_type='application/csv'
			)

		"""
		Need to define the output pointer and convert to .json, then save that .json
		"""
		output_pointer = {
			"dataset" : "",
			"scheme" : "",
			"schema" : "",
			"gotchas" : [],
		}
		output_pointer = json.dumps(
			output_pointer,
			indent = 4
		)

		return False

	def alter_df(self):
		"""
		In the case that there needs to be an irreplaceable version of a dataset,
			this function will accomplish just that
		"""
		return 

class implement_json_minio:

	def __init__(self):
		"""
		Import json files
		"""
		# Pointer to minio
		with open(os.getcwd() + "/ChiefYeetOfficer/data-cleaning/" + "point_minio.json") as f:
			point_minio = json.load(f)

		# Pointer to input file
		with open(os.getcwd() + "/ChiefYeetOfficer/data-cleaning/" + "point_input.json") as f:
			point_input = json.load(f)


		"""
		Construct graphs to be used for getting data from JSON pointers
		"""
		# Create client 
		self.Client = minio_connect_fromJson(
			endpoint = point_minio['client info']['endpoint'],
			access_key = point_minio['client info']['access_key'],
			secret_key = point_minio['client info']['secret_key'],
			secure = True,
			schema = point_minio['schema']
		)
		self.dataset = self.Client.get_df(
			csvName = point_input['dataset']
		)
		print("Fetched data from minio")

		"""
		Upload dataset back to minio
		"""
		self.Client.upload_df(
			df = self.dataset,
			csvName = "test_test.csv"
		)
		print("Put data back in to minio")


if __name__ == "__main__":

	implement_json_minio()