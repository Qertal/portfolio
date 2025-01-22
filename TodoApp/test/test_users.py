from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'qertal'
    assert response.json()['email'] == 'qertal@o2.pl'
    assert response.json()['firstname'] == 'jan'
    assert response.json()['lastname'] == 'kolwaski'
    assert response.json()['role'] == 'admin'
    

def test_change_password_test_success(test_user):
    response = client.put("/users/password", json = {'password': '1234',
                                                    'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put("/users/password", json = {'password': 'wrong_password',
                                                    'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

    