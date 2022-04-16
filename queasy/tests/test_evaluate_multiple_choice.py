from queasy import app

def test_evaluate_multiple_choice():
    question = {
        'type': 1,
        'choices': ['PDF', 'XLS', 'CSV', 'TXT', 'XML'],
        'answer': 'CSV'
    }
    answer = 'C'
    print(f'score is {app.evaluate(question, answer)}')

if __name__ == '__main__':
    test_evaluate_multiple_choice()