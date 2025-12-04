import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestNVIDIAPrivacyService(unittest.TestCase):
    
    def test_health_endpoint(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("status", data)
        self.assertIn("model_loaded", data)
        self.assertIn("device", data)
        
    def test_evaluate_endpoint(self):
        # Test with empty text
        response = client.post("/evaluate", json={"text": ""})
        self.assertEqual(response.status_code, 400)
        
        # Test with valid text
        response = client.post("/evaluate", json={"text": "John Doe email john@example.com"})
        # This will return 200 even though it's a mock implementation
        # In a real implementation, it would return detected entities
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()