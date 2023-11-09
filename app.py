from flask import Flask,request, jsonify
import json

app = Flask(__name__)  #instance of the flask web application


#Route to accept POST request

@app.route('/post',methods=['POST']) #This line defines a route for handling POST requests.
def store_input():
            try:
                data = request.get_json()
                print(data)
                if data:
                    with open('data.json', 'w') as json_file:
                        json_file.write(json.dumps(data, indent=4))
                    return jsonify({"message": "Data stored successfully"}), 201
                else:
                    return jsonify({"error": "Invalid JSON data received"}), 400
            except Exception as e:
                return jsonify({"error": f"An error occurred: {str(e)}"}), 500
            
            #jsonify:- it is returned as a response in JSON format

#Route to accept GET request

@app.route("/get", methods=['GET'])
def get_data():
    try:
        with open("data.json",'r') as json_file:
            data = json.load(json_file)
            return jsonify(data)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
                
#Route to accept pull requests

@app.route("/put", methods=['PUT'])
def overwite_data():
    try:
        data = request.get_json()
        if 'input' in data:
            with open("data.json","w") as json_file:
                json.dump(data,json_file)
                        
            return jsonify({"message": "Data overwrite Successfully."}),204
        else:
            return jsonify({"error":"Invalid payload format."}), 400
    except Exception as e:
        return jsonify({"error":str(e)}), 500
                

#route for patch requests

@app.route("/patch",methods=['PATCH'])
def modify_data():
    try:
        data = request.get_json()
        if 'input' in data:
            with open("data.json","r+") as json_file:
                content = json.load(json_file)
                content["input"] = data["input"]

            #update the data in json file
            with open("data.json","w") as json_file:
                json.dump(content,json_file)
            return jsonify({"message":"Data patched successfully."}),204
        else:
            return jsonify({"error":"Invalid Payload Format"}),400
    except Exception as e:
         return jsonify({"error":str(e)}),500

# Route to accept DELETE requests

@app.route('/delete', methods=['DELETE'])
def delete_data():
    try:
        # Delete the data from the JSON file
        with open('data.json', 'w') as json_file:
            json.dump({}, json_file)

        return jsonify({"message": "Data deleted successfully."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
            


if __name__ == '__main__':
    app.run(debug=True)

