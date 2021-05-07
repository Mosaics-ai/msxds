"""
Goal of this file is to make a graph structure to easily call 
functions from the ETL engine

Data frame will be passed, and returned from each
"""

from ETL_engine import *
import lab

class index:

    df = lab.test().fetch_df_from_minio()
    col_list = ["formattedID", "State","Country"] # For hashing
    datepart_col_list = ["Order Date", "Ship Date"] # for datepart extracting


    """
    Bear in mind, the df should be passed from each of these classes to the next

    Each takes in a "df", but that df is a new, cleaned version of the previous df, ideally

    Test this functionality
    """
    structure = {
        "hash" : {
            "class" : hashing, # would need to insert "(df=df).column_hasher(col_list)" so function isn't called 
            "function" : column_hasher,
            "add-to-function" : (col_list)
        },  
        "binner" : {
            "class" : binner,  # would need to insert "(df=df).bin_columns"
            "function" : bin_columns
        },
        "null handler" : {
            "class" : null_handler, # would need to insert "(df=df).return_null_list()"
            "function" : return_null_list()
        },
        "fill empties" : {
            "class" : fill_empties, # would need to insert "(df=df).iterate_cols()"
            "function" : iterate_cols
        },
        "standardization" : {
            "class" : standardization, # would need to insert "(df=df).normalize()"
            "function" : normalize(),
        },
        "datepart extractor" : {
            "class" : datepart_extractor, # would need to insert "(df=df).return_datepart_cols(col_list=datepart_col_list)"
            "function" : return_datepart_cols(col_list = datepart_col_list)
        },
    }

if __name__ == "__main__":
    a = index()