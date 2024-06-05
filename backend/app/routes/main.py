from flask import Blueprint, request, jsonify, current_app
from multiprocessing import Queue, Process
import os
from ..services.processing import format_file

main_bp = Blueprint('main', __name__)

# Send dataPoints (thedata) on Response
@main_bp.route('/process', methods=['POST'])
def api_process():
    #  Receiving the filName options: small or large
    fileData = request.get_json()
    fileName = "points_small.txt" if fileData['file_Name'] == "small" else "points_large.txt"
    file_path = os.path.join(current_app.static_folder, fileName)

    # Checking whether the file's path exist
    if not os.path.exists(file_path):
        return jsonify({"error": f"File {fileName} not found"}), 404

    # Calling the global parameters
    cancelProcess = current_app.config['cancelProcess']
    cancelProcess.value = False

    # Creating a Queue for storing the data in the parallel processing task
    q = Queue()

     # Creating the Parallel Process
    processTetra = Process(target=format_file, args=(q, file_path, cancelProcess,))
    processTetra.start()

    # Setting a time duration for the main process to execute on points_small.txt or points_large.txt
    if fileName == "points_small.txt":
        processTetra.join(20)
    elif fileName == "points_large.txt":
        processTetra.join(120)

    # Handling Cancel & Close interruption of the parallel process
    if cancelProcess.value or processTetra.is_alive():
        processTetra.terminate()
        processTetra.join()
        current_app.config['thedata'] = current_app.config['initialData']
        print("The process has been canceled by the User")
        return jsonify(current_app.config['thedata'])

    # Finally, storing the data points in the global variable: thedata :)
    dataQ = q.get()
    current_app.config['thedata'] = dataQ
    return jsonify(current_app.config['thedata'])

# Returning the JSON data points on the /api route
@main_bp.route('/api', methods=['GET'])
def api():
    return jsonify(current_app.config['thedata'])
