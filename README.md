# House Price Prediction - Deployed on Heroku(PaaS)

Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this challenges us to predict the final price of each home.

The Ames Housing dataset was compiled by Dean De Cock for use in data science education.

Dataset - https://www.kaggle.com/c/house-prices-advanced-regression-techniques

## Technologies

Python, Machine Learning (Regression Techniques), Flask, Heroku(PaaS) for Deployment, HTML, CSS, Jquery, Ajax

## Steps Followed

Data Cleaning and preprocessing -> Feature Engineering -> Feature Selection -> Modelling -> Deployment 

## Prerequisites

We must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

## Project Structure

1. app.py - This contains Flask APIs that receives house details through GUI or API calls, computes the precited value based on our model and returns it.

3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.

4. templates - This folder contains the HTML template to allow user to enter House detail and displays the predicted House Price.

5. Procfile - Heroku apps include a Procfile that specifies the commands that are executed by the app on startup. The Procfile must live in your app’s root directory. It does not function if placed anywhere else.

6. requirements.txt - This file is used for specifying what python packages are required to run the project.

7. Trained_Models - Python notebooks where EDA, Feature Engineering, Feature Selection and Modelling are performed.

8. data_description.txt - Detailed explanation of each and every feature/variable.

## Running the project (Local Environment)

1. Ensure that we are in the project home directory.

2. Run app.py using below command to start Flask API - python app.py

3. By default, flask will run on port 5000.

4. Navigate to URL http://localhost:5000. We should be able to view the homepage.

5. We can also send direct POST requests to FLask API using Python's inbuilt request module. Run the beow command to send the request with some pre-popuated values - python request.py

## Heroku - (PaaS - Platform as a service)

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

1. Login to Heroku platform.

2. Create new project. (https://dashboard.heroku.com/apps)

3. Open the project -> Deploy -> Connect to Github -> Deploy Branch. Our model will get deployed.

4. To check logs - open Command Prompt -> Type heroku login (Connects to heroku account)-> heroku logs --tail --app {project_name}

5. If Using CLI - Please follow: https://devcenter.heroku.com/categories/deploying-with-git

6. Here is the project. Please navigate to URL : https://housepriceprediction-ml.herokuapp.com/

We should be able to view the homepage as below :

![Image description](https://github.com/gurram1223/HousePricePrediction/blob/master/Images/Homepage.PNG)

Enter valid details and hit Submit.

![Image description](https://github.com/gurram1223/HousePricePrediction/blob/master/Images/Predicted.PNG)

