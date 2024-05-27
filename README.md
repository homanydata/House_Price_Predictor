# House_Price_Predictor
This project is website to predict the price of a house based on given features' values

## Components:
### Supervised Regression Model:
- Read dataset and choose most important features using Pandas. Dataset is from [kaggle](https://www.kaggle.com/datasets/shivachandel/kc-house-data).
- Dataset was splitted into 3 parts:
    - train set will be used to train all models
    - validate set will be used to evaludate each model, and choose the best one
    - test set will be used only once at the end, for the final model chosen
- Using scikit-learn and xgboost libraries, several models where created
- Train each model on the data
- Save models scores over the validation subset, choose best one, then test it using testing subset.
- Save best model as pkl file using pickle library

### Prediction:
Using Flask, a simplistic page was created, that inputs house features like area, number of bedrooms & bathrooms... and then predicts the price of the house based on the best model saved.

HTML & CSS files can be found inside [/templates](/templates/) and [/static](/static/) respectively


## Usage
Below you find all the necessary steps to use or try the project:

- Download [Python](https://www.python.org/downloads/)
- Download this [project](https://github.com/homanydata/House_Price_Predictor/archive/refs/heads/main.zip)
- Open the command line inside the project folder to install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```
- Run app.py
- Insert the details of the house you wanna estimate its price, then click PREDICT

It is important to note that the dataset is for a specific area, it might not be actually accurate or beneficial for you in the real world.
