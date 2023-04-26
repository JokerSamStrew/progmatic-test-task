from main import * 
import unittest
import random


class CalculationTestCase(unittest.TestCase):
    def test_example_case(self):
        results = []
        tokens_variety([('', '9')], 8, results) 

        for result in results:
            str_result = tokens_to_str(result)
            self.assertEqual(eval(str_result), 200, 
                        f'expression "{str_result}" doesn\'t equal 200')

