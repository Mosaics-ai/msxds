import numpy as np
import pandas as pd 
import random
import string
import json 
from sklearn.preprocessing import MinMaxScaler

class hashing:
    """
    ID hashing for PII or more consistent use of characters
    """
    
    def __init__(self, df):
        
        # Initial variables
        self.df = df
        self.index = {}     # connect original ID to hashed ID 
        self.hashed_IDs = []    # for check if ID is available

    def hashing_func(self, column_name):
        """
        Function used for any sort of hashing for values
        """
        # Index for hashing
        index = {}
        
        # Iterate through ID's and Hash
        hashed = ""
        N = 0
        uniques = self.df[column_name].unique()
        for ID in uniques:
            
            hashed = ""
            while hashed not in self.hashed_IDs:

                hashed = self.rand_ID_function()
                self.hashed_IDs.append(hashed)
                
            # Update index graph
            index[ID] = hashed

            N += 1

            # print(ID + " : " + str(N) + " : " + str(len(uniques)))  # show number hashed vs len

        # Convert index to json 
        # index = json.dumps(index, indent = 4)

        return index
        
    def returnHashed_ID_df(self, ID_col_name):
        """
        Specifically returns hashed ID's data frame
        """
        self.ID_col_name = ID_col_name
        
        self.index = self.hashing_func(column_name = ID_col_name)
            
        # Save this index later if need the .csv to join on 
        self.index_df = pd.DataFrame(self.index, index = ["Hashed ID"]).T  

        hashed_list = []
        for element in self.df[self.ID_col_name]:
            update_with_hashed = self.index[element]
            hashed_list.append(update_with_hashed)

        # Add Hashed IDs to the data frame
        self.df["Hashed IDs"] = hashed_list

        # Remove original column from data frame 
        self.df = self.df.drop(columns = [self.ID_col_name], inplace = True)

        # Convert index to json 
        self.index = json.dumps(self.index, indent = 4)  
        
        return self.df, 
        
    def rand_ID_function(self, N = 10):
        """
        Generate ID of length N
        """
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = [str(j) for j in range(10)]
        
        ID = ""
        for j in range(N):
            letter_or_number = random.choice(["letter", "number"])
            if letter_or_number == "letter":
                char = random.choice(string.ascii_letters)
            else:
                char = random.choice(numbers)
            ID += char
            
        return ID

    def column_hasher(self, col_list):
        """
        Return data frame with hashed column values 
        Update a stored index graph of values to tie back to later 
        """
        # Iterate through columns and find values
        index = {}
        for col in col_list:
            index[col] = self.hashing_func(col)

        # Convert to json
        index = json.dumps(index, indent = 4)

        return index
        
class data_filter:
    """
    This is an interesting one
    I need to think about how I want things returned in the context of what George can use 
    i.e., if I return something, it has to be compatible and reverant to the UI   
    If I pass something through the filter, and someone wants to do a Find and Replace, for example,   
        then how can that return in the best way for it to be useful?
    """
    def __init__(self, df):
        
        self.df = df
        
    def filter_col(self):
        
        return 
        
    def isCategorical(self, col):
        """
        Test to determine whether categorical
        Test to determine cardinality
        """
        # Determine number of uniques in the column
        # Use nunique() method in pandas which counts number of distinct values per variable
        # Use unique() method to output the distinct categories in the variable
        
        return # Return True if Categorical, False if Numerical

class binner:

    def __init__(self, df):

        self.df = df
        self.data = []  # Updated as recurses 

    def bin_from_numerical(self, N):
        """
        **Could maybe add some refinements to this method**
        - Performed on the column level
        - Look at normal distribution 
        - Find categorized bins based on the ranges in there 
        - Account for tails and outliers, off skews

        mean +/- (3*sigma) is the middle 99.7% of a normal distribution 
        so, if within ^ range:
            - then fall in to 1/N percent range bin 
        else if > range
            - fall in to > normal bin   
        else if < range 
            - fall in to < normal bin 
        """

        # Mean and 3 sigma
        data_mean = int(np.mean(self.data))
        three_sigma = int(3 * np.std(self.data))

        # Create bins
        lower, upper = int(data_mean - three_sigma), int(data_mean + three_sigma)
        if lower < min(self.data):
            lower = int(min(self.data))
        if upper > max(self.data):
            upper = int(max(self.data))
        incrementer = int((upper - lower) / N)
        bin_list = [lower + j * incrementer for j in range(N)]
        bin_list_strings = [str(element) for element in bin_list]

        # Now create list of ranges for bins (strings)
        # This should be like a <x_1, x_1-x_2, x_2-x_3, etc. type of thing
        bin_list_bins = ["<" + str(bin_list_strings[0])]
        
        bin_graph = {bin_list_bins[0] : {"lower" : min(self.data), "upper" : float(bin_list_strings[0])}}
        for k, element in enumerate(bin_list):
            if k < len(bin_list)-1:
                # For bins list
                lower = bin_list_strings[k]
                upper = bin_list_strings[k + 1]
                concatenated = lower + " - " + upper
                bin_list_bins.append(concatenated)

                # Update graph check
                bin_graph[concatenated] = {
                    "lower" : float(lower), 
                    "upper" : float(upper),
                    }
        bin_list_bins.append(">" + str(bin_list_strings[-1]))

        # Now to sort through data and bin them in to the previously defined categories
        binned_data = []
        for k, element in enumerate(self.data):
            element = float(element)
            for option in bin_graph:
                lower = bin_graph[option]["lower"]
                upper = bin_graph[option]["upper"]
                if element >= lower and element <= upper:
                    binned_data.append(option)
                    break

        return binned_data

    def bin_from_categorical(self, N):
        """
        When greater than N categories:
            1) do a histogram type count distribution  
            2) take the top N values  
            3) Everything else returns in to 'Other' category
            4) Return new categorical bins 
        """

        # Number of categories
        num_categories = self.data.nunique()

        # Value counts 
        val_counts = self.data.value_counts()

        # Top N categories
        top_N = val_counts.index[0:N]

        # Iterate if N > num_categories, else return
        if num_categories > N:
            # Do stuff
            binned_data = []
            for k, element in enumerate(self.data):
                if element not in top_N:
                    binned_data.append("other")
                else:
                    binned_data.append(element)
            return binned_data
        else:
            return self.data
        

    def bin_columns(self):
        """
        Algorithm that iterates through each column and bins by numerical or categorical
        """
        new_df = {}
        global col
        for col in self.df.columns:
            if "id" not in col.lower() and "postal" not in col.lower():
                self.data = self.df[col]  # Update array used in binning funcs
                if self.data.dtype.name == 'category' or self.data.dtype.name == 'object':
                    new_df[col] = list(self.bin_from_categorical(N = 3))
                else:
                    if 'date' not in col.lower() and 'time' not in col.lower():
                        new_df[col] = list(self.bin_from_numerical(N = 9))
                    else:
                        new_df[col] = list(self.data)

        new_df = json.dumps(new_df, indent = 4)

        return new_df 

class null_handler:
    """
    Drops columns with too many Nulls
    """
    def __init__(self, df):

        self.df = df

    def return_null_list(self):
        """
        Iterate through columns 
        Determine which columns have > 50% nulls 
        Return dictionary of percent Nulls in column  
        Return dictionary for data frame with no null columns
        """
        null_list = {}
        without_nulls_dict = {}
        for col in self.df.columns:
            series = self.df[col]
            check = series.isna().sum()
            if check / len(self.df) > 0.50:
                null_list[col] = "drop column, > 50% nulls"
            else:
                null_list[col] = "pass"
                without_nulls_dict[col] = list(series)

        # Convert dict to json 
        without_nulls_dict = json.dumps(without_nulls_dict, indent = 4)

        return  null_list, without_nulls_dict

class fill_empties:
    """
    Impute:
    - Mean for numerical  
    - Mode for categorical
    """
    def __init__(self, df):

        self.df = df 
        self.data = ""

    def iterate_cols(self):

        filled_df = {}
        for col in self.df:
            self.data = self.df[col]

            if self.data.dtype.name == 'category' or self.data.dtype.name == 'object':
                filled_df[col] = self.impute_mean()
            else:
                filled_df[col] = self.impute_mode()

        return filled_df

    def impute_mean(self):
        try:
            mean = self.data.mean()
            return self.data.fillna(mean)
        except:  # If an ID or zip code where mean can't really be computed
            return self.data

    def impute_mode(self):
        mode = self.data.mode()[0]
        return self.data.fillna(mode)

class standardization:
    """
    Prevent any unequal weighting among numerical columns
    """

    def __init__(self, df):

        self.df = df   

    def normalize(self):
        """
        MinMaxScaler works with numerous columns -- making the values scaled to each other 
        Therefore, need to compile list of columns to be compiled first, and then do the function
        """

        global col 
        columns_to_normalize = {}
        for col in self.df.columns:
            self.data = self.df[col]  # Update array used in binning funcs
            if self.data.dtype.name != 'category' and self.data.dtype.name != 'object':
                if "id" not in col.lower() and "postal" not in col.lower():
                    columns_to_normalize[col] = self.data

        # MinMaxScaler on columns to normalize
        columns_to_normalize = pd.DataFrame(columns_to_normalize)
        scaler = MinMaxScaler(feature_range = (0, 1))
        columns_to_normalize[columns_to_normalize.columns] = scaler.fit_transform(columns_to_normalize)

        # Make data graph with normalized -- ML prepped and ready
        graph_with_standardized = {}
        for col in self.df.columns:
            self.data = self.df[col]
            if col not in columns_to_normalize.columns:
                data = list(self.data)
            else:
                data = list(columns_to_normalize[col])
            graph_with_standardized[col] = list(data)

        # Make JSON data type 
        graph_with_standardized = json.dumps(graph_with_standardized, indent = 4)

        return graph_with_standardized

class datepart_extractor:
    """
    Take out dateparts similar to SQL 
    - day of week
    - day of month   
    - day of year
    - week of year 
    - month of year 
    - quarter 
    - maybe time of day? -- early morning, morning, early afternoon, fringe, evening, late night
    """
    def __init__(self, df):

        self.df = df 
        self.data = ""
        self.datepart_list = {
            "day_of_week" : self.day_of_week,
            "day_of_month" : self.day_of_month,
            "day_of_year" : self.day_of_year,
            "week_of_year" : self.week_of_year,
            "month_of_year" : self.month_of_year,
            "quarter" : self.quarter,
        }

    def return_datepart_cols(self, col_list):

        # Iterate through timestamp columns and compile date parts
        datepart_df = {}
        for col in col_list:

            # Convert column to_datetime
            self.data = pd.to_datetime(self.df[col])

            # Iterate through dateparts and add a column for each to data frame
            for datepart in self.datepart_list:
                col_string = col + "_" + datepart
                datepart_df[col_string] = list(self.datepart_list[datepart]())

        # Convert to json
        datepart_df = json.dumps(datepart_df, indent = 4)

        return datepart_df

    def day_of_week(self):

        return self.data.dt.dayofweek

    def day_of_month(self):

        return self.data.dt.day

    def day_of_year(self):

        return self.data.dt.dayofyear

    def week_of_year(self):

        return self.data.dt.weekofyear

    def month_of_year(self):

        return self.data.dt.month

    def quarter(self):

        return self.data.dt.quarter
    