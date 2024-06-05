from flask import Blueprint, request, jsonify, render_template, current_app
import os

dynamo_bp = Blueprint('dynamo', __name__)

# Handling API request from the frontend to rethrieve the TXT files locally
@dynamo_bp.route('/dynamo/post', methods=['POST'])
def dynamo_post():
    data = request.get_json()
    current_app.config['thedat'] = data['file_Name']
    return jsonify({'dynamoUpdated': "ok"})

# Displaying the TXT files upon request
@dynamo_bp.route('/dynamo/data', methods=['GET'])
def dynamo_data():
    thedat = current_app.config.get('thedat', None)
    if thedat == "small":
        file_path = os.path.join(current_app.static_folder, "points_small.txt")
    elif thedat == "large":
        file_path = os.path.join(current_app.static_folder, "points_large.txt")
    else:
        return render_template('dynamo.html')

    with open(file_path, "r") as file:
        lines = file.readlines()
        return render_template('dynamo.html', lines=lines)

# Handling API request from the frontend to rethrieve the TXT files from AWS-DynamoDB
@dynamo_bp.route('/read_file/<file_id>', methods=['GET'])
def read_file(file_id):
    content = retrieve_file(file_id)
    if content:
        return jsonify({'FileID': file_id, 'Content': content}), 200
    else:
        return jsonify({'error': 'File not found'}), 404
