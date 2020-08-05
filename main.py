from flask import Flask, render_template, request
from flask_restful import Api, Resource
from route.AiRoute import AiRoute
from loader import Service, Route, Model

#create app
app = Flask(__name__)
api = Api(app)

#initialize by DI
aiRoute = Route.aiRoute()

#temp route for flask-resful
class tempRouteHandler(Resource):
    def post(self):
        return aiRoute.post()

#add routing 
api.add_resource(tempRouteHandler, "/api/ai")

#constructor
if __name__ == "__main__":
    # Run app with port 50000
    app.run(host="0.0.0.0", port=50000)