import pytest
class TestDynamoPost:
    # Correctly updates current_app config with valid JSON input
    def test_correctly_updates_config_with_valid_json(self, mocker):
        from backend.app.routes.dynamo import dynamo_post
        from flask import Flask

        app = Flask(__name__)
        app.config['thedat'] = None

        with app.test_request_context(json={'file_Name': 'test_file.txt'}):
            mocker.patch('backend.app.routes.dynamo.current_app', app)
            response = dynamo_post()
            assert response.json == {'dynamoUpdated': "ok"}
            assert app.config['thedat'] == 'test_file.txt'

    # Missing 'file_Name' key in JSON input
    def test_missing_file_name_key_in_json(self, mocker):
        from backend.app.routes.dynamo import dynamo_post
        from flask import Flask

        app = Flask(__name__)
        app.config['thedat'] = None

        with app.test_request_context(json={'wrong_key': 'test_file.txt'}):
            mocker.patch('backend.app.routes.dynamo.current_app', app)
            with pytest.raises(KeyError):
                dynamo_post()

class TestDynamoData:

    # Returns 'dynamo.html' template when 'thedat' is not set
    def test_returns_dynamo_html_when_thedat_not_set(self, mocker):
        mocker.patch('backend.app.routes.dynamo.current_app')
        mocker.patch('backend.app.routes.dynamo.render_template')
        current_app.config.get.return_value = None
        render_template.return_value = 'dynamo.html'
    
        from backend.app.routes.dynamo import dynamo_data
        result = dynamo_data()
    
        render_template.assert_called_once_with('dynamo.html')
        assert result == 'dynamo.html'

    # 'thedat' is set to an unexpected value
    def test_thedat_unexpected_value(self, mocker):
        mocker.patch('backend.app.routes.dynamo.current_app')
        mocker.patch('backend.app.routes.dynamo.render_template')
        current_app.config.get.return_value = 'unexpected'
        render_template.return_value = 'dynamo.html'
    
        from backend.app.routes.dynamo import dynamo_data
        result = dynamo_data()
    
        render_template.assert_called_once_with('dynamo.html')
        assert result == 'dynamo.html'

class TestReadFile:

    # valid file_id returns correct content and 200 status
    def test_valid_file_id_returns_correct_content_and_200_status(self, mocker):
        from backend.app.routes.dynamo import read_file
        mocker.patch('backend.app.routes.dynamo.retrieve_file', return_value='file content')
        response, status_code = read_file('valid_file_id')
        assert status_code == 200
        assert response.json == {'FileID': 'valid_file_id', 'Content': 'file content'}