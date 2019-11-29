import json
import mock
import random
from src.tests.helper.base_test import BaseTestCase


class TestInteraction(BaseTestCase):

    def test_get_interaction(self):
      interaction_id = int(random.uniform(1, 10))
      response = self.client.get(f'/interaction/{interaction_id}')
      data = json.loads(response.data)
      assert response.status_code == 200
      assert data.get('id_interaction') != None
      assert data.get('quote') != None
      assert data.get('answer') != None
      assert data.get('user') != None
    
    def test_get_invalid_interaction(self):
      response = self.client.get(f'/interaction/10000000')
      assert response.status_code == 404
