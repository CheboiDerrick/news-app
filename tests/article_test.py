import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("Maxwell","News Update","For daily news",'https://cnn.com','http://cnn.com/image','2020-09-15')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_article.author,"Maxwell")
        self.assertEqual(self.new_article.title,"News Update")
        self.assertEqual(self.new_article.description,"For daily news")
        self.assertEqual(self.new_article.url,'https://cnn.com')
        self.assertEqual(self.new_article.urlToImage,'https://cnn.com/image')
        self.assertEqual(self.new_article.publishedAt,'2020-09-15')
       
if __name__ == '__main__':
    unittest.main()