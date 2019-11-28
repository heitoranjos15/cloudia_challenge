import json
import mock
from src.tests.helper.base_test import BaseTestCase


class TestAnswerRoute(BaseTestCase):
    def tests_answer(self):
        payload = json.dumps({"quote": "3 5 9 120", "user": {
            "name": "john",
            "plataform": "twitter"
        }})
        response = self.client.post('/answer', data=payload)
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data.get('answer') == 'Fizz Buzz Fizz FizzBuzz'

    def test_send_nothing(self):
        payload = json.dumps({})
        response = self.client.post('/answer', data=payload)
        assert response.status_code == 400

    def test_send_invalid_message(self):
        payload = json.dumps({'quote': 'Ola mensagem invalida', "user": {
            "name": "john",
            "plataform": "invalid"
        }})
        response = self.client.post('/answer', data=payload)
        assert response.status_code == 400

    def test_send_invalid_user(self):
        payload = json.dumps({"quote": "3 5 9 120", "user": {
            "name": "john",
            "plataform": "invalid"
        }})
        response = self.client.post('/answer', data=payload)
        assert response.status_code == 400

    def test_unexpected_error(self):
        with mock.patch('src.views.answer.get_answer') as answerMock:
            answerMock.side_effect = Exception('unexpected')
            payload = json.dumps({'quote': '3 5 9 120'})
            response = self.client.post('/answer', data=payload)
            answerMock.assert_called()
            assert response.status_code == 500
