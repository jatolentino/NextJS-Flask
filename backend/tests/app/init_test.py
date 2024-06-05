import pytest

class TestCreateApp:

    # app instance is created successfully
    def test_app_instance_created_successfully(self):
        app = create_app()
        assert app is not None
        assert isinstance(app, Flask)

    # template_folder path does not exist
    def test_template_folder_path_does_not_exist(self, mocker):
        mocker.patch('os.path.exists', return_value=False)
        with pytest.raises(Exception):
            create_app()