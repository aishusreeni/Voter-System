from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

voters = {}
c1 = 0
c2 = 0

class Vote(Resource):
  
    def get(self, voter_id): 
       return {voter_id : voters[voter_id]}
    
    def post(self, voter_id):
	voters[voter_id] = request.form['id']
	if voter_id is 'candidate1':
		global c1
		c1 = c1 + 1
	else:
		global c2
		c2 = c2 + 1
	print c1 , " " , c2
	return {'voter_id' : voters[voter_id]}

api.add_resource(Vote, '/<string:voter_id>')

if __name__ == '__main__':
    app.run(debug=True)
