from flask import Flask,request, jsonify
import json

app = Flask(__name__)

# input = [
#     {
#         'id': 1,
#         'title': 'My_First_API',
#         'description': 'Take_Input, Title, description,',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': 'Learn Python',
#         'description': 'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]



@app.route('/store_input',methods=['POST'])
def store_input():
            try:
                data = request.get_json()
                print(data)
                if data:
                    with open('data.json', 'w') as json_file:
                        json_file.write(json.dumps(data, indent=4))
                    return jsonify({"message": "Data stored successfully"})
                else:
                    return jsonify({"error": "Invalid JSON data received"}), 400
            except Exception as e:
                return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

if __name__ == '__main__':
    app.run(debug=True)

