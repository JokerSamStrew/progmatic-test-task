from main import * 
import unittest


class CalculationTestCase(unittest.TestCase):
    def test_example_case(self):
        test_case_input = '98 + 76 - 5 + 4 - 10'
        expected_result = '98 + 76 - 5 + 43 - 2 - 10'
        result = calculate_expression(test_case_input)

        self.assertEqual(result, expected_result,
                        'example case failed')
        self.assertEqual(eval(result), 200, 
                        'expression doesn\'t equal 200')

        test_case_input = '98 + 76 - 5 + 43 - 2 - 10'
        result = calculate_expression(test_case_input)
        self.assertEqual(result, expected_result,
                        'valid case failed')

    def test_fail_case(self):
        try:
            test_case_input = ['98', '98 + 76 - 5 + 43 - 2']
            calculate_expression(test_case_input)
        except Exception as ex:
            self.assertEqual(repr(ex), "Exception('Solution not found')")


        try:
            for test_case_input in ['', 'dsagasd']:
                calculate_expression(test_case_input)
        except Exception as ex:
            self.assertEqual(repr(ex), "Exception('Failed parse expression')")
