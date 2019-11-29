import random
import json
from src.tests.helper.base_test import BaseTestCase


class TestUserInteractions(BaseTestCase):

    def test_get_user_interaction(self):
        user_id = int(random.uniform(1, 5))
        response = self.client.get(f'/user/{user_id}/interactions')
        data = json.loads(response.data)
        assert response.status_code == 200
        for interaction in data:
            assert interaction.get('name') != None
            assert interaction.get('plataform') != None
            assert interaction.get('interaction') != None
    
    def test_get_invalid_user(self):
        response = self.client.get(f'/user/10000000/interactions')
        data = json.loads(response.data)
        assert response.status_code == 404
