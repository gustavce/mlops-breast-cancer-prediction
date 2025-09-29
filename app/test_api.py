import unittest
import json
from api import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.get_json())

    def test_predict_valid(self):
        # Ejemplo de datos de una muestra maligna (M)
        input_data = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,
                      1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,
                      25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
        response = self.client.post("/predict", json={"input": input_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.get_json())

    def test_predict_invalid(self):
        # Faltan datos
        response = self.client.post("/predict", json={"input": [1,2,3]})
        self.assertEqual(response.status_code, 500)
        self.assertIn("error", response.get_json())

    def test_predict_missing_field(self):
        response = self.client.post("/predict", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

if __name__ == "__main__":
    unittest.main()
