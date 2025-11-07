import unittest
from app import app

class BasicTests(unittest.TestCase):

    # إعداد التطبيق للاختبار
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # اختبار الصفحة الرئيسية
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    # اختبار الصفحة الثانية
    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About", response.data)

if __name__ == "__main__":
    unittest.main()
