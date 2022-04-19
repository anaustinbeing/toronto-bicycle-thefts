# toronto-bicycle-thefts
A predictive software that would help both the police department and the “general public” to get an idea about the likelihood of bicycle theft and the recovery.

## Summary:
The purpose is to create a predictive software that would help both the police department and the “general public” to get an idea about the likelihood of bicycle theft. It uses the supervised learning techniques on dataset containing the actual values collected by the police department over the period of 5 years.

## Solution:
Model is built using RandomForest Classifier for predicting the likelihood of bicycle theft. The model performed well on the dataset with an accuracy rate of 99% on unseen data.

## Data Exploration, Feature Selection and Findings:
Following are the findings after exploring the dataset through different plots including heatmap and histogram:

	The cost of the bike was the most important feature in the dataset. Higher the cost of bike, more the chance of it being stolen.

	More number of thefts are reported or occurred on week days when compared to weekends.

	The chances of recovery are higher if the thefts are reported on the same day as occurrence.

	Actual dataset was highly imbalanced with very less data in ‘Recovered’ category. Hence, it is upsampled to match the count of values in ‘Stolen’ category.

	Bike_Colour and Cost_of_Bike have several missing values and they are handled by imputing with the most frequent values in that column.

	The columns used for model building are: Primary_Offence, Occurrence_DayOfWeek, Report_DayOfWeek, Hood_ID, Bike_Make, Bike_Type, Bike_Colour, Cost_of_Bike, Status, Location_Type, Premises_Type.

	StandardScaler is used to scale the values on the ‘Cost_of_Bike’ column and the rest of the categorical columns are transformed using OneHotEncoder.

## Model Building:

In addition, performances using the below mentioned classifiers are explored to finalize the model to be used:

a)	Logistic Regression

b)	Support Vector Machine

c)	MLP

d)	RandomForest

e)	DecisionTree


Since the RandomForest Classifier has the highest accuracy, further fine-tuning of the hyparameters are performed on RandomForest using GridSearch. This helps to find the best parameters for the model. The best model then shows an accuracy of 99% on testing data. At the end of model building, the best model and the transformation pipeline are saved using pickle in order to use them for deployment.

## Model Deployment:
Model deployment is done using Flask API. A form is created using HTML to allow users to input the 10 features, and the data provided by the user is first transformed using the saved pipeline, and then the transformed data is used for prediction.

## Model Deployment Testing Screenshots:

Case1: Stolen

![image](https://user-images.githubusercontent.com/17433078/164035646-e1a9bdfc-95e9-42d9-a5ea-792f7a78c761.png)

![image](https://user-images.githubusercontent.com/17433078/164035772-3e12ee59-1044-49d4-93d7-c607ca2d05e2.png)
 
 
Case 2: Recovered

![image](https://user-images.githubusercontent.com/17433078/164035841-ebdbeeae-8b4c-4007-bc34-678cafdc4708.png)

![image](https://user-images.githubusercontent.com/17433078/164035853-888d3ccd-29f3-43e0-86e5-8bfc01eeed53.png)


 
