from flask_restful import Resource

class HelloWorld(Resource):            #  Create a RESTful resource
    def get(self):                     #  Create GET endpoint
        return "Hello I'm Weather Agent"

