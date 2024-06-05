from flask import Blueprint, request, jsonify, current_app

cancel_bp = Blueprint('cancel', __name__)

# Handling cancel/interruption directive
@cancel_bp.route('/cancel', methods=['POST'])
def cancel_process():
    cancelData = request.get_json()
    cancelProcess = current_app.config['cancelProcess']
    current_app.config['thedata'] = current_app.config['initialData']
    if cancelData['cancel'] == "true":
        cancelProcess.value = True
    return jsonify({'cancelled': "Process has been cancelled"})
