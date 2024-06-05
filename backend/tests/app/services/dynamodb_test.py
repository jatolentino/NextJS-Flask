import pytest

class TestRetrieveFile:

    # retrieve existing file content by valid file_id
    def test_retrieve_existing_file_content_by_valid_file_id(self, mocker):
        from backend.app.services.dynamodb import retrieve_file
        table = mocker.patch('backend.app.services.dynamodb.table')
        table.get_item.return_value = {'Item': {'Content': 'file content'}}
    
        file_id = 'valid_file_id'
        result = retrieve_file(file_id)
    
        assert result == 'file content'
        table.get_item.assert_called_once_with(Key={'FileID': file_id})

    # file_id is an empty string
    def test_file_id_is_empty_string(self, mocker):
        from backend.app.services.dynamodb import retrieve_file
        table = mocker.patch('backend.app.services.dynamodb.table')
        table.get_item.return_value = {}
    
        file_id = ''
        result = retrieve_file(file_id)
    
        assert result is None
        table.get_item.assert_called_once_with(Key={'FileID': file_id})