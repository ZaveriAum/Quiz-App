import html
from data import question_data, options


class QuizBrain:

    question_data_for_checking_answer = question_data
    options_for_checking_answer = options

    def __init__(self, q_list, q_option):
        self.question_number = -1
        self.score = 0
        self.question_options = q_option
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number + 1}: {q_text}"

    def check_option_a(self):
        correct_answer = QuizBrain.question_data_for_checking_answer[self.question_number]['correct_answer']
        return QuizBrain.options_for_checking_answer[self.question_number][0] == correct_answer

    def check_option_b(self):
        correct_answer = QuizBrain.question_data_for_checking_answer[self.question_number]['correct_answer']
        return QuizBrain.options_for_checking_answer[self.question_number][1] == correct_answer

    def check_option_c(self):
        correct_answer = QuizBrain.question_data_for_checking_answer[self.question_number]['correct_answer']
        return QuizBrain.options_for_checking_answer[self.question_number][2] == correct_answer

    def check_option_d(self):
        correct_answer = QuizBrain.question_data_for_checking_answer[self.question_number]['correct_answer']
        return QuizBrain.options_for_checking_answer[self.question_number][3] == correct_answer

    def check_true_answer(self):
        correct_answer = self.current_question.answer
        return "true" == correct_answer.lower()

    def check_false_answer(self):
        correct_answer = self.current_question.answer
        return "false" == correct_answer.lower()