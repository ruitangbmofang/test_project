from app import create_app
from app.api.bills import Bills
from flask_restful import Api

app = create_app()
api = Api(app)
api.add_resource(Bills, '/bills', '/bills/<string:id>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=9990)
