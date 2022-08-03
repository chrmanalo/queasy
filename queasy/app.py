import argparse
import copy
import random
from queasy.utils import yaml_reader, converters, tracer

SEPARATOR = 16*'----'
parser = argparse.ArgumentParser(description='Arguments being passed to the program')
parser.add_argument('--type', '-t', nargs='+', type=int, required=False, help='Question type')
parser.add_argument('--items', '-n', type=int, required=False, help='Number of items')
args = parser.parse_args()

@tracer.trace
def show_question(i, question, n_items, instruction):
    categories = yaml_reader.read('queasy/data/aws_product_categories.yml')
    new_question = copy.deepcopy(question)
    print(f'Category: {categories[question["category"]]}')
    print(f'Instruction: {instruction}')
    print(SEPARATOR)
    print(f'Question ({i+1}/{n_items}): {question["text"]}')
    if question['type'] == 1:
        choices = question['choices']
        new_question['answer'] = choices[0]
        new_question['choices'] = random.sample(choices, len(choices))
        print('\n'.join([f'{converters.number_to_upper(i+1)}. {choice}' for i, choice in enumerate(new_question['choices'])]))
    elif question['type'] == 2:
        choices = question['answers'] + question['wrongs']
        new_question['choices'] = random.sample(choices, len(choices))
        print('\n'.join([f'{converters.number_to_upper(i+1)}. {choice}' for i, choice in enumerate(new_question['choices'])]))
    return new_question

def evaluate(question, answer):
    score = 0
    answer_found = False
    if question['type'] == 0:
        boolean_answers = (['FALSE', 'F', 0], ['TRUE', 'T', 1])
        answer_found = list(filter(lambda answers: answer in answers and question['answer'] in answers, boolean_answers))
        if answer_found:
            print('Correct!')
            score = 1
        else:
            print(f'The correct answer is {question["answer"]}.')
    elif question['type'] == 1:
        correct_answer_in_choice = list(filter(lambda choice: question['answer'] == choice[1], enumerate(question['choices'])))
        corresponding_letter = converters.number_to_upper(correct_answer_in_choice[0][0]+1)
        if answer == corresponding_letter:
            print('Correct!')
            score = 1
        else:
            print(f'The correct answer is {corresponding_letter}. {question["answer"]}.')
    elif question['type'] == 2:
        no_whitespace = ''.join(answer.split())
        answer_set = set(no_whitespace)
        correct_answers = list(filter(lambda choice: choice[1] in question['answers'], enumerate(question['choices'])))
        correct_letters = list(map(lambda correct_answer: converters.number_to_upper(correct_answer[0]+1), correct_answers))
        if answer_set == set(correct_letters):
            print('Correct!')
            score = 1
        else:
            print(f'The correct answers are:')
            print('\n'.join([f'  {letter}. {answer[1]}.' for letter, answer in zip(correct_letters, correct_answers)]))
    return score

def ask(i, question, n_items):
    print(SEPARATOR)
    if question['type'] == 0:
        show_question(i, question, n_items, instruction='True or False.')
    elif question['type'] == 1:
        question = show_question(i, question, n_items, instruction='Choose the letter of the best possible answer.')
    elif question['type'] == 2:
        question = show_question(i, question, n_items, instruction='Choose multiple letters that best satisfy the question.')
    else:
        pass
    answer = input('Answer: ').upper()
    return evaluate(question, answer)

def has_valid_types(types, question):
    for type in types:
        if question['type'] == type and type in range(0, 3):
            return True
    return False

def run():
    questions = yaml_reader.read('queasy/data/questions.yml')
    
    filtered_questions = list(filter(lambda question: has_valid_types(args.type, question), questions)) if args.type != None else questions
    n_items = len(filtered_questions) if args.items == None else args.items
    sampled_questions = random.sample(filtered_questions, n_items)

    score_list = map(lambda q: ask(*q, n_items), enumerate(sampled_questions))
    score = sum(score_list)
    score_percentage = score/n_items*100
    print(SEPARATOR)
    print(f"You scored {score} out of {n_items} ({score_percentage}%)!")

if __name__ == '__main__':
    run()