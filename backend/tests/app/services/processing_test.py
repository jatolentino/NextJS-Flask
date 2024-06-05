import pytest

class TestFormatFile:

    # correctly formats a file by removing parentheses and spaces
    def test_correctly_formats_file(self, mocker):
        from backend.app.services.processing import format_file
        from queue import Queue
        import tempfile
        import os

        # Create a temporary input file
        input_content = "(1, 2, 3)\n(4, 5, 6)\n"
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_input:
            temp_input.write(input_content.encode())
            input_path = temp_input.name

        # Create a temporary output file path
        output_path = input_path.replace(".txt", "") + "_formatted.txt"

        # Mock the cancel_flag
        cancel_flag = mocker.Mock()
        cancel_flag.value = False

        # Create a queue
        q = Queue()

        # Call the function
        format_file(q, input_path, cancel_flag)

        # Check the output file content
        with open(output_path, 'r') as outfile:
            output_content = outfile.read()

        expected_output = "1,2,3\n4,5,6\n"
        assert output_content == expected_output

        # Clean up temporary files
        os.remove(input_path)
        os.remove(output_path)

    # handles an empty input file gracefully
    def test_handles_empty_input_file(self, mocker):
        from backend.app.services.processing import format_file
        from queue import Queue
        import tempfile
        import os

        # Create a temporary empty input file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_input:
            input_path = temp_input.name

        # Create a temporary output file path
        output_path = input_path.replace(".txt", "") + "_formatted.txt"

        # Mock the cancel_flag
        cancel_flag = mocker.Mock()
        cancel_flag.value = False

        # Create a queue
        q = Queue()

        # Call the function
        format_file(q, input_path, cancel_flag)

        # Check the output file content
        with open(output_path, 'r') as outfile:
            output_content = outfile.read()

        expected_output = ""
        assert output_content == expected_output

        # Clean up temporary files
        os.remove(input_path)
        os.remove(output_path)