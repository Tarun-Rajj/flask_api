from flask import Flask, jsonify
import json

app = Flask(__name__)

input = [
    {
        'id': 1,
        'title': 'My_First_API',
        'description': 'Take_Input, Title, description,',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/store_input',methods=['GET'])
def store_input():
    return jsonify(input)
    

if __name__ == '__main__':
    app.run(debug=True)

