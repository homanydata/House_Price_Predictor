from flask import Flask, jsonify, request, render_template
import numpy
import pickle
import xgboost


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def Home():
    return render_template('index.html', prediction_text='insert data to have a prediction')


@app.route("/predict", methods=["POST"])
def predict():
    features = request.form
    X_test = extract_features_raw_values(features)
    y_pred = model.predict(X_test)[0]
    prediction_text = f'I think this house price is around {y_pred:,.0f} 💲💲'

    return render_template('index.html', prediction_text=prediction_text)


def extract_features_raw_values(features: dict) -> numpy.ndarray:
    """
    Transforms raw feature values from an HTML form into a NumPy array suitable for making predictions with a scikit-learn model

    Args:
        features (dict): dict of values inputted by the user
    Returns:
        (np.ndarray) transformed features as the model needs them in order to predict correctly
    """
    sqft_living = float(features.get('sqft_living'))
    sqft_above = float(features.get('sqft_basement_percentage')) * sqft_living / 100
    bedrooms = float(features.get('bedrooms'))
    bathrooms = float(features.get('bathrooms'))
    year_built = float(features.get('year_built'))
    zipcode = float(features.get('zipcode'))
    view = float(features.get('view'))
    condition = float(features.get('condition'))

    transformed_features = numpy.array([sqft_above, sqft_living, bedrooms, bathrooms, year_built, zipcode, view, condition]).reshape(1, -1)

    return transformed_features


if __name__ == '__main__':
    app.run(debug=True)
