
# coding: utf-8

# In[1]:

def predicting_algo(Input):

	import numpy as np
	from sklearn.metrics import mean_squared_error
	from sklearn.ensemble import GradientBoostingRegressor
	import pickle
	from geopy.geocoders import Nominatim, GoogleV3
	# from geopy.geocoders import 

	address, month, weekday, city = Input.split("|")

  	geolocator = GoogleV3(format_string = "%s, " + city )
  	_ , (latitude, longitude) = geolocator.geocode(address)
  	Input = [latitude, longitude, int(month), int(weekday)]
  	scaler = pickle.load(open('Scaler_file', "rb" ))
  	est = pickle.load(open('Estimator', "rb" ))
  	test_sample = scaler.transform(np.reshape(np.array(Input), [1,4]))

  	return est.predict(test_sample)[0]

    

# For testing
if __name__ == "__main__":
	Input = "7660 oakdale street massillon ohio 44646|12|1|canton"#[34.049273,-118.245468,6,0]
	print(predicting_algo(Input))
