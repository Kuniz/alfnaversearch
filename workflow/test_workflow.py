# coding=utf-8
import unittest

import certifi
import naver_search
import naver_shopping
import krdic_naver_search
import hanja_naver_search
import endic_naver_search
import enendic_naver_search
import common_naver_search


class MyTestCase(unittest.TestCase):
    def test_naver_search(self):
        res = naver_search.get_data('한글')

        self.assertTrue(len(res['items']) > 0)

    def test_shopping(self):
        res = naver_shopping.get_data('한글')

        self.assertTrue(len(res['items']) > 0)

    def test_krdic(self):
        res = krdic_naver_search.get_dictionary_data('한글')

        self.assertTrue(len(res['items']) > 0)

    def test_hanjadic(self):
        res = hanja_naver_search.get_dictionary_data('한글')

        self.assertTrue(len(res['items']) > 0)

    def test_endic(self):
        res = endic_naver_search.get_dictionary_data('한글')

        self.assertTrue(len(res['items']) > 0)

    def test_enendic(self):
        res = enendic_naver_search.get_dictionary_data('한글')

        self.assertTrue(len(res['items']) > 0)

    def test_common_naver_dic(self):
        langs = ['ja', 'zh', 'vi', 'th', 'uz', 'de', 'fr', 'it', 'es', 'ru', 'id', 'ne', 'mn', 'my', 'sw', 'ar',
                 'km', 'fa', 'hi', 'nl', 'sv', 'uk', 'ka', 'cs', 'hr', 'tr', 'pt', 'pl', 'fi', 'hu', 'sq', 'ro',
                 'la', 'el']

        for lang in langs:
            print('Test of %s\n' % lang)
            res = common_naver_search.get_dictionary_data(lang, '한글')

            self.assertTrue(len(res['items']) > 0)


if __name__ == '__main__':
    unittest.main()
