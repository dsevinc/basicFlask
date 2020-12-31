from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"about":"hello world!"}
    
    def post(self):
        some_json = request.get_json()
        return {'sent': some_json}, 201

class Multi(Resource):
    def get(self, num):
        return {'result':num*10}

class Hello(Resource):
    def get(self, name):
        return render_template('hello.html', name=name)

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')
# api.add_resource(Hello, '/hello/')
api.add_resource(Hello, '/hello/<name>')
# def index():
#     if (request.method == 'POST'):
#         some_json = request.get_json()
#         return jsonify({'sent': some_json}), 201
#     else:
#         return jsonify({"about":"hello world!"})

# @app.route('/multi/<int:num>', methods=['GET'])
# def get_multiply10(num):
#     return jsonify({"result":num*10})


if __name__ == '__main__':
    app.run(debug=True)