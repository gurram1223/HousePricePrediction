import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'TotalSF':1491.0,'TotalBsmtSF':1484.0,	'OverallQual':5, 'GarageCars':2, 'BsmtFinSF1':0.0, 
                            '1stFlrSF':7, 'YearRemodAdd':1971, 'LotArea':9, 'KitchenQual':5, 'GrLivArea':7.0, 
                            'GarageFinish':3, 'GarageArea':487.0, 'FullBath':2, 'ExterQual':5, 'BsmtQual':6, '2ndFlrSF':0})

print(r)

