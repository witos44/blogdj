import pytest
pytestmark = pytest.mark.django_db

class TestPostModel:
    def test_str_return(self,post_factory): # we will use PostFactory created in conftest.py in this namespace like post_factory here..
        post = post_factory(title='test-post')
        assert post.__str__() == 'test-post'
        
    def test_add_tag(self,post_factory):
        x = post_factory(title='test-post',tags=['test'])
        assert x.tags.count() == 1