from flask import Flask, jsonify, render_template, redirect, url_for
from flask.wrappers import Request
from flask import request
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from sklearn.ensemble import GradientBoostingClassifier
import joblib

save_path = 'gradientboostmodel.joblib'
enc_save_path = 'onehotencoding.joblib'
db_password = "##############"
engine = create_engine(f"postgresql://postgres:{db_password}@localhost:5432/groupproject")

classifier = joblib.load(save_path)
enc = joblib.load(enc_save_path)
app = Flask(__name__, template_folder='.')

@app.route('/')
def hello_world():
    # TODO: Pull data from database
    imported_full_df = pd.read_sql("SELECT * FROM bank JOIN contact ON contact.index = bank.index LIMIT 400;", con=engine).drop(["index"], axis=1)
    data = imported_full_df.to_dict('records')
    return render_template("index.html", data = data)

@app.route('/model',  methods=['POST'])
def model():
    d = request.form.to_dict()
    d = {
        'age': [int(d['age']) if d['age'] != '' else 44],
        'job': [d['job'] if d['job'] != '' else "unknown"],
        'marital': [d['marital'] if d['marital'] != '' else "single"],
        'education': [d['education'] if d['education'] != '' else "tertiary"],
        'default': [bool(d['default']) if d['default'] != '' else False], 
        'balance': [float(d['balance']) if d['balance'] != '' else 2143],
        'housing': [bool(d['housing']) if d['housing'] != '' else False],
        'loan': [bool(d['loan']) if d['loan'] != '' else False],
        'campaign': [1],
        'pdays': [-1],
        'previous': [0],
        'poutcome': ['unknown'],
        'pdays_bool': [False],
        'contact': ['unknown']
    }

    bank_df = pd.DataFrame(data=d)
    encoded_data = enc.transform(bank_df[["job", "marital", "education", "contact", "poutcome"]]).toarray()
    encoded_features = enc.get_feature_names(["job", "marital", "education", "contact", "poutcome"])

    new_df = pd.DataFrame(encoded_data, columns = encoded_features)

    bank_df = pd.concat([bank_df.copy(), new_df], axis=1)
    bank_df = bank_df.drop(["job", "marital", "education", "contact", "poutcome"], axis=1)
    print(bank_df)
    print(classifier.predict(bank_df))
    return jsonify(classifier.predict(bank_df).tolist())


if __name__ == "__main__":
   app.run()