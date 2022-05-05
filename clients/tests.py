from django.test import TestCase

class TestViews(TestCase):
    def test_clients_page_redirects_when_not_logged_in(self):
        """ Test that the clients page redirects when user is not logged in """
        response = self.client.get('/clients/')
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'clients/view_clients.html')
    