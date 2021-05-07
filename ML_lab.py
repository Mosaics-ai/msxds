"""
Niklaus Parcell

- Test 'data cleaned' data frames in ML algorithms 
"""

import numpy as np   
import pandas as pd  
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, auc
from sklearn.preprocessing import train_test_split, LabelEncoder

class ML_preprocessing:
	"""
	ML ready format
	Inputs X, outputs Y
	"""
	def __init__(self, df, target):

		self.df = df 

class model:
	"""
	Train and test a model
	Also return some metrics 
	"""
	def __init__(self, X, Y):

		self.X = X   
		self.Y = Y

	def return_scores(self):

		return 

if __name__ == "__main__":

	# Data Cleaning from other module


	# ML_preprocessing


	# model and metrics


	pass 
