from starlette.status import HTTP_204_NO_CONTENT

from .utils import *
from routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'bbots_test'
    assert response.json()['email'] == 'bullbeary.bots@outlook.com'
    assert response.json()['first_name'] == 'Bullbeary'
    assert response.json()['last_name'] == 'Bots'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '(111)-111-1111'


def test_change_password_success(test_user):
    response = client.put('/user/password', json={
        'password': 'admin123',
        'new_password': 'test123'
    })
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={
        'password': 'wrongpassword123',
        'new_password': 'test123'
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}


def test_change_phone_number(test_user):
    response = client.put('/user/phone-number/12345')
    assert response.status_code == status.HTTP_204_NO_CONTENT
