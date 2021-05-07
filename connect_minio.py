from minio import Minio 
import pandas as pd
import io
from io import BytesIO

class colors:
	RED = "\033[91m"
	BLUE = "\033[94m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	END = "\033[0m"

class minio_connect:

    def __init__(self):

        self.client = Minio(
            endpoint = "minio.mosaics.ai",
            access_key = "miniominio",
            secret_key = "miniominio",
            secure = True,
        )
        self.scheme = "/minio"
        self.schema = "mosaicsai-dev"

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

    def upload_df(self, csvName):
        """
        Establish connection and then upload csv

        Most-likely done after cleaning a dataset and having a new version in Minio
        """
        return

    def alter_df(self):
        """
        In the case that there needs to be an irreplaceable version of a dataset,
            this function will accomplish just that
        """
        return 

if __name__ == "__main__":

    df = minio_connect().get_df(
        csvName = 'superstore_dataset2011-2015.csv'
    )