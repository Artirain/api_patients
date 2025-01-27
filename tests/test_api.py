import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from api.models import CustomUser, Patient

User = get_user_model()

@pytest.mark.django_db
def test_login_success():
    user = User.objects.create_user(username='testuser', password='testpass')
    client = APIClient()
    response = client.post('/api/login/', {'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_login_fail():
    client = APIClient()
    response = client.post('/api/login/', {'username': 'wrong', 'password': 'wrong'})
    assert response.status_code == 401


@pytest.mark.django_db
def test_patients_access_with_doctor_role():
    # создаем пользователя с ролью doctor
    user = CustomUser.objects.create_user(username='doctor1', password='password123', role='doctor')


    # создаем пациента
    patient = Patient.objects.create(
        date_of_birth='1985-05-10',
        diagnoses=['Диагноз 1', 'Диагноз 2']
    )


    # авторизация
    client = APIClient()
    response = client.post('/api/login/', {'username': 'doctor1', 'password': 'password123'})
    
    # проверка, успешный логин и получение access token
    assert response.status_code == 200
    access_token = response.data['access']

    # Отправляем запрос с токеном
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = client.get('/api/patients/')

    # проверка
    assert response.status_code == 200
    assert len(response.data) == 1  #мы создали одного пациента
    assert response.data[0]['diagnoses'] == ['Диагноз 1', 'Диагноз 2']


@pytest.mark.django_db
def test_patients_access_without_doctor_role():
    user = User.objects.create_user(username='user1', password='password123')

    client = APIClient()
    response = client.post('/api/login/', {'username': 'user1', 'password': 'password123'})
    access_token = response.data['access']

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = client.get('/api/patients/')
    assert response.status_code == 403
