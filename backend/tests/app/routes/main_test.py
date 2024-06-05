import pytest
class TestApiProcess:

    # process small file successfully within time limit
    def test_process_small_file_successfully_within_time_limit(self, mocker):
        from backend.app.routes.main import api_process
        from flask import Flask, jsonify
        import multiprocessing

        app = Flask(__name__)
        app.config['cancelProcess'] = multiprocessing.Value('b', False)
        app.config['initialData'] = {}
        app.config['thedata'] = {}

        with app.test_request_context(json={'file_Name': 'small'}):
            mocker.patch('backend.app.routes.main.os.path.exists', return_value=True)
            mocker.patch('backend.app.routes.main.format_file', return_value=None)
            mocker.patch('backend.app.routes.main.Queue', return_value=mocker.Mock(get=lambda: {'data': 'test'}))

            response = api_process()
            assert response.status_code == 200
            assert response.get_json() == {'data': 'test'}