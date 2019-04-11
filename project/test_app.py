import os
import json
import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_METHODS'] = []  # Turn off csrf protection for testing
    client = app.test_client()

    return client


def test_success_form(client):
    data = {
        'school_name': 'test',
        'street': 'test',
        'house': '57',
        'city': 'test',
        'region': 'Vinnytsia',
        'director_name': 'test',
        'director_phone': '12345',
        'director_email': 'test@test.ru',
        'children_quantity': '50',
        'text': 'text',
    }
    response = client.post('/', data=json.dumps(data))
    assert b'We received your message.' in response.data
    


def test_wrong_email(client):
    data = {
        'school_name': 'test',
        'street': 'test',
        'house': '57',
        'city': 'test',
        'region': 'Vinnytsia',
        'director_name': 'test',
        'director_phone': '12345',
        'director_email': 'test',
        'children_quantity': '50',
        'text': 'text',
    }
    response = client.post('/', data=json.dumps(data))
    assert 'Вы ввели некорректный email. Попробуйте еще раз.'.encode(
        'utf-8') in response.data
