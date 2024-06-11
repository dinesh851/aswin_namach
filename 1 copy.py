from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def fa():
    return "fewefWS"


@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    print(data)
    data=[
    {
        "date": "2024-06-11",
        "success_count": "10"
    },
    {
        "_bkt": "intuit_ist_switch~1008~27C9E931-8514-4737-9400-AA9E01FCE980",
        "_cd": "1008:43199426" 
    }
]
    json_data = json.dumps(data, indent=4)
    print(json_data)

    # Return the received data as a JSON response
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
