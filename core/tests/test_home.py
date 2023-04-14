import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db

class TestHomePage:
    def test_homepage_url(self,client):
        url = reverse('homepage')
        response = client.get(url)
        assert response.status_code == 200 # if it works correctly it will return 200, and if not then it will return other response codes
        
    def test_post_htmx_fragment(self,client):
        headers = {'HTTP_HX-Request':'true'}
        response = client.get('/',**headers)
        assertTemplateUsed(response, 'blog/post-list-elements.html')
        