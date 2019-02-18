import unittest
import concatenate


class TestStringConcatenateTransform(unittest.TestCase):

    def test_concatenate_empty(self):
        transformer = concatenate.StringConcatenateTransform()
        self.assertEqual('', transformer.transform_many([]))

    def test_concatenate_without_join_text(self):
        transformer = concatenate.StringConcatenateTransform()
        self.assertEqual('a', transformer.transform_many(['a']))
        self.assertEqual('ab', transformer.transform_many(['a', '', 'b']))
        self.assertEqual('abcdef', transformer.transform_many(['ab', 'cd', 'ef']))

    def test_concatenate_with_join_text(self):
        transformer = concatenate.StringConcatenateTransform()
        self.assertEqual('a b c', transformer.transform_many(['a', 'b', 'c'], options={'join_text':' '}))
        self.assertEqual('**', transformer.transform_many(['', '', ''], options={'join_text':'*'}))
