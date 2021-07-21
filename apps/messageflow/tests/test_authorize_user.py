import pytest
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
# import models
from django.contrib.auth.models import User

# import usecase
from apps.messageflow.usecases.user import (
    AuthorizeUser,
    UserUnauthorizedError
)


def create_user(username, email, password, **extra_fields):
    # mock for "create_user" method on the User model
    # to avoind touching the database. Unit tests should not
    # touch databases :)

    return User(
        id=1,
        username=username,
        email=email,
        password=password,
        **extra_fields
    )

@pytest.fixture
def mock_execute_dependencies(mocker):
    # already tested on TestValidData
    mocker.patch.object(AuthorizeUser, 'valid_data', return_value=None)

    mocker.patch.object(AuthorizeUser, '_get_app_info', return_value={
            "app_id": 'testapp',
            "namespace": 'testapp',
        })


class TestExecute:
    # Test the execute method on AuthorizeUser use case

    def setup_method(self):
        # setup method will be executed on each test
        rf = RequestFactory()
        req = rf.get('/testapp/messageflow/test/')

        user = create_user('testuser', 'test@test.com', 'password')
        self._use_case = AuthorizeUser(
            user=user,
            path=req.path,
        )

    def test_return_service_info(self, mock_execute_dependencies):
        expected = {
            "owner_id": 1,
            "app_id": 'testapp',
            "namespace": 'testapp',
        }
        result = self._use_case.execute()
        assert result == expected


class TestValidData:
    # Test the valid_data method on AuthorizeUser use case

    def test_when_user_not_authenticated_error(self, mocker):
        with pytest.raises(UserUnauthorizedError):
            use_case = AuthorizeUser(
                user=AnonymousUser(),
                path='/testapp/messageflow/test/',
            )

            use_case.valid_data()

    def test_when_user_authenticated_true(self, mocker):
        expected_result = True

        user = create_user('testuser', 'test@test.com', 'password')

        use_case = AuthorizeUser(
            user=user,
            path='/testapp/messageflow/test/',
        )

        result = use_case.valid_data()
        assert result == expected_result
