#import library
from flask import Flask, request
import flask
from flask_restful import Resource, Api
from flask_cors import CORS

import csv
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


# inisiasi object
app = Flask(__name__)

# insiasi objeck flask restful
api = Api(app)

# inisiasi object flask_cors
CORS(app)

# inisiasi variabel kosong bertipe dictionary
data = {}
data["nama"] = ""
data["nilai_admin"] = ""
data["test_1"] = ""
data["test_2"] = ""
data["interview"] = ""
data["hasil"] = ""

# model Naive Bayes
df = pd.read_csv("data.csv")
# Variabel independen
x = df.drop(['Diterima'], axis = 1)
# Variabel dependen
y = df['Diterima']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4, random_state = 12)

modelnb = GaussianNB()
nbtrain = modelnb.fit(x_train, y_train)

# membuat class Resource

class ContohResource(Resource):
    # method get dan post
    def get(self):
        # response = {"msg" : "Hallo Dunia, ini app restful pertamaku"}
        response = df.to_json()
        return response

    def post(self):
        nama = request.form["nama"]
        nilai_admin = request.form["nilai_admin"]
        test_1 = request.form["test_1"]
        test_2 = request.form["test_2"]
        interview = request.form["interview"]
        data["nama"] = nama
        data["nilai_admin"] = nilai_admin
        data["test_1"] = test_1
        data["test_2"] = test_2
        data["interview"] = interview

        hasil = [(nilai_admin,test_1,test_2,interview)]
        f = open('test.csv', 'w')
        w = csv.writer(f)
        w.writerow(('Nilai Admin','Test 1','Test 2','Interview'))
        for h in hasil:
            w.writerow(h)
        f.close()
        test = pd.read_csv("test.csv")

        y_pred = nbtrain.predict(test)
        hasil = y_pred.tolist()

        if hasil[0] == 1:
            response = {
                "nama":nama,
                "msg":"Diterima",
                "status":"true"
                }
        else:
            response = {
                "nama":nama,
                "msg":"Tidak Diterima",
                "status":"false"
                }
        return response

# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
