from ..utils.tetrahedron import find_smallest_tetrahedron
from flask import current_app

# Creating formatted raw TXT files
def format_file(q, file_path, cancel_flag):
    output_path = file_path.replace(".txt", "") + "_formatted.txt"
    with open(file_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            if cancel_flag.value:
                print("Process interrupted from within the function")
                return
            line = line.strip().replace('(', '').replace(')', '').replace(' ', '')
            outfile.write(line + '\n')

    # Waiting for Client Clear/Cancel process
    if cancel_flag.value:
        print("Process interrupted from within the function after file processing")
        return

    # Finding the smalled tetradron
    best_tetra_list, dataPoints = find_smallest_tetrahedron(output_path)

    # Adding the solution points to Queue: q
    q.put(dataPoints)
