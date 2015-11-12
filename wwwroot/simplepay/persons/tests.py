from django.core.urlresolvers import reverse
from django.test import TestCase, Client

class BaseTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.post("/admin/", {'name': 'admin', 'passwd': '12345'})
        self.assertEqual(response.status_code, 302)

class ViewTestCase(TestCase):
    
    def test_index_page(self):
        view_name = 'index'

        url = reverse(view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)        

    def test_tag_page(self):
        view_name = 'tag'
        
        url = reverse(view_name, kwargs={'tag_name': 'aaa'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)        

    def test_person_page(self):
        view_name = 'person'
        
        url = reverse(view_name, kwargs={'person_name': 'Jerry'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)              
    

