import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self) -> None:
        """Create a survey and a set of responses for use in all test methods."""
        self.question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(self.question)
        self.responses = [ 'English', 'Spanish', 'Mandarin' ]

    def test_store_single_response(self):
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)
        self.assertEqual(self.question, self.my_survey.question)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        self.assertEqual(self.question, self.my_survey.question)       

if __name__ == '__main__':
    unittest.main()