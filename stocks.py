from yahoo_finance import Share
from pprint import pprint
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import time

DATAFILE = "datafile.csv"
SYMBOLS = ['YHOO', 'GM', 'APPL','C','FB']
pd.DataFrame({'Symbols' : SYMBOLS}).to_csv("datafile.csv", index = False)
FREQ =  10.0 # In seconds


def getPrice (symbol):
	tmp = Share(symbol).get_price()
	if tmp: # nan control
		return str(tmp)
	return ""

def addOneColData():
	""" input :
	dt = 2d array with 1st column of symbols,
	rest of the columns go by datetime -> price 
	"""	
	dt = pd.read_csv(DATAFILE)
	dt[str(datetime.now())] = dt['Symbols'].apply(getPrice)  # apply getPrice to all symbols
	dt.to_csv(DATAFILE, index=False)



starttime=time.time()
while True:
  addOneColData()
  time.sleep(FREQ - ((time.time() - starttime) % FREQ))