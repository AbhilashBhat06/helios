from django.test import TestCase
from django.test import SimpleTestCase

#Sample tests to check for correctness of code
class SimpleTests(SimpleTestCase): 
	def test_home_page_status(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
	
