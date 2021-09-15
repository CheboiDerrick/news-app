import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("cnn","CNN NEWS","For daily news",'https://cnn.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_source.id,"cnn")
        self.assertEqual(self.new_source.name,"CNN NEWS")
        self.assertEqual(self.new_source.description,"For daily news")
        self.assertEqual(self.new_source.url,'https://cnn.com')
       
if __name__ == '__main__':
    unittest.main()