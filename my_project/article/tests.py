from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from article.views import ArticleView
from article.models import Article
import json


class TestArticles(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = ArticleView.as_view()
        self.uri = '/articles/'
        Article.objects.create(
            title='Charlie Chaplin', description="Funny story", body='Woahhh', author_id=1)
        Article.objects.create(
            title='Jeffrey Archer', description="Business", body='Suspense', author_id=1)
        print(Article.objects.all())

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        print("get-response:", response)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestCreateArticles(APITestCase):

        def setUp(self):
            self.client = APIClient()
            self.factory = APIRequestFactory()
            self.view = ArticleView.as_view()
            self.uri = '/articles/'
            Article.objects.create(
                title='Charlie Chaplin', description="Funny story", body='Woahhh', author_id=1)
            Article.objects.create(
                title='Jeffrey Archer', description="Business", body='Suspense', author_id=1)
            print(Article.objects.all())

        def test_create(self):
            # self.client.login(username="test", password="test")
            params = {
                "article":{

                "title": "heyaa",
                "description": "Noahhh",
                "body": "Woahhhh",
                "author_id": "1"
                }
            }
            response = self.client.post(self.uri, data=json.dumps(params), content_type='application/json')
            print("created_response_mess:-", response.data)
            self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'
                             .format(response.status_code))


class TestUpdateArticles(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = ArticleView.as_view()
        self.uri = '/articles/'
        Article.objects.create(
            title='Charlie Chaplin', description="Funny story", body='Woahhh', author_id=1)
        Article.objects.create(
            title='Jeffrey Archer', description="Business", body='Suspense', author_id=1)
        print(Article.objects.all())

    def test_update(self):
        # self.client.login(username="test", password="test")
        params = {

            "article":{
            "title": "Hurrah"
            }
        }
        response = self.client.put(self.uri+"1", data=json.dumps(params), content_type='application/json')
        print("updated_response_message:-", response.data)
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestDeleteArticles(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = ArticleView.as_view()
        self.uri = '/articles/'
        Article.objects.create(
            title='Charlie Chaplin', description="Funny story", body='Woahhh', author_id=1)
        Article.objects.create(
            title='Jeffrey Archer', description="Business", body='Suspense', author_id=1)
        print(Article.objects.all())

    def test_delete(self):
        response = self.client.delete(self.uri+"1")
        print("deleted_response_message:-", response.data)
        self.assertEqual(response.status_code, 204, 'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))


class TestSearchArticles(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = ArticleView.as_view()
        self.uri = '/articles/'
        Article.objects.create(
            title='Charlie Chaplin', description="Funny story", body='Woahhh', author_id=1)
        Article.objects.create(
            title='Jeffrey Archer', description="Business", body='Suspense', author_id=1)
        print(Article.objects.all())

    def test_search(self):
        params = {'id': 2}
        response = self.client.get(self.uri, params)
        # response = self.view(request, params)
        print("search-response:", response.data)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
