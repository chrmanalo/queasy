from queasy import app

def test_evaluate_boolean():
    question = {
        'type': 'Boolean',
        'answer': 'True'
    }
    answer = 'T'
    print(f'score is {app.evaluate(question, answer)}')

if __name__ == '__main__':
    test_evaluate_boolean()