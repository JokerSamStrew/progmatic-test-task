from main import * 
import unittest


class CalculationTestCase(unittest.TestCase):
    def test_example_case(self):
        test_case_input = '98 + 76 - 5 + 4 - 10'
        expected_result = '98 + 76 - 5 + 43 - 2 - 10'
        result = calculate_expression(test_case_input)

        self.assertEqual(result, expected_result,
                        'example case failed')
        self.assertEqual(eval(result), 200)


    def test_insert_index(self):
        test_case_input = '98 + 76 - 5 + 4 - 10'

        self.assertEqual(possible_insertion_index(test_case_input),
                         14, 'example case failed')


        test_case_input = '98 + 76 - 5 + 444444 - 10'

        self.assertEqual(possible_insertion_index(test_case_input),
                         19, 'example case failed')


    def test_split(self):
        test_case_input = '98 + 76 - 5 + 4 - 10'
        self.assertEqual(split_expression(14, test_case_input), 
                         ('98 + 76 - 5 ', '+ 4 - 10'))
