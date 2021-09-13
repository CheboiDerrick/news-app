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
        self.new_source = Source(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_source.id,1234)
        self.assertEqual(self.new_source.tittle,"Python Must Be Crazy")
        self.assertEqual(self.new_source.overview,"A thrilling new Python Series")
        self.assertEqual(self.new_source.poster,'https://image.tmdb.org/t/p/w500/khsjha27hbs')
        self.assertEqual(self.new_source.vote_average,8.5)
        self.assertEqual(self.new_source.vote_count,129993)


if __name__ == '__main__':
    unittest.main()