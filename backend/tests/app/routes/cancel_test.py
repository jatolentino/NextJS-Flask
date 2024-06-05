import pytest
class TestCancelProcess:

    # returns correct JSON response when cancelData['cancel'] is "true"
    def test_returns_correct_json_response_when_cancel_is_true(self, mocker):
        from backend.app.routes.cancel import cancel_process
        from flask import Flask, jsonify

        app = Flask(__name__)
        app.config['cancelProcess'] = mocker.Mock()
        app.config['initialData'] = 'initial data'
        app.config['thedata'] = 'some data'

        with app.test_request_context(json={'cancel': 'true'}):
            with app.app_context():
                response = cancel_process()
                assert response.json == {'cancelled': "Process has been cancelled"}
                assert app.config['cancelProcess'].value is True
                assert app.config['thedata'] == 'initial data'

    # handles missing 'cancel' key in cancelData
    def test_handles_missing_cancel_key_in_cancelData(self, mocker):
        from backend.app.routes.cancel import cancel_process
        from flask import Flask, jsonify

        app = Flask(__name__)
        app.config['cancelProcess'] = mocker.Mock()
        app.config['initialData'] = 'initial data'
        app.config['thedata'] = 'some data'

        with app.test_request_context(json={}):
            with app.app_context():
                response = cancel_process()
                assert response.json == {'cancelled': "Process has been cancelled"}
                assert app.config['cancelProcess'].value is not True
                assert app.config['thedata'] == 'initial data'