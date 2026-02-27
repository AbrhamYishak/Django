from django.test import TestCase
from django.utils.text import slugify
from .utils import slugify_article
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        self.numberOfTest = 5
        for _ in range(self.numberOfTest):
            obj = Article.objects.create(title = "django test database",content = "testing django test database")
            obj.save()
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
    def test_count_match(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(),self.numberOfTest)
    def test_hello_world(self):
        obj = Article.objects.all().order_by("id").first()
        slug = obj.slug
        title = obj.title
        self.assertEquals(slug,slugify(title))
    # def test_slugify_method(self):
    #     obj = Article.objects.all().last()
    #     slugs = []
    #     for i in range(0,5):
    #         instance = slugify_article(obj)
    #         slugs.append(instance.slug)
    #     print(slugs)
    #     uniqueSlug = list(set(slugs))
    #     self.assertEqual(len(slugs),len(uniqueSlug))