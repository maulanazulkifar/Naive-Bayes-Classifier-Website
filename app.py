#import library
from flask import Flask, request
import flask
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi object
app = Flask(__name__)

# insiasi objeck flask restful
api = Api(app)

# inisiasi object flask_cors
CORS(app)

# inisiasi variabel kosong bertipe dictionary
identitas = {}
identitas["nama"] = "maulana"
identitas["umur"] = "24"

# membuat class Resource


class ContohResource(Resource):
    # method get dan post
    def get(self):
        # response = {"msg" : "Hallo Dunia, ini app restful pertamaku"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg": "Data berhasil dimasukan"}
        return response


# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
