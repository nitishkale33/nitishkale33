from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from employee import UpdateEmployee

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(UpdateEmployee,'/update')  # TODO: Update employee

if __name__=='__main__':
    app.run(debug=True, port=45020)
