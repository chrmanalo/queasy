from queasy import app

def test_evaluate_boolean_true():
    question = {
        'type': 0,
        'answer': 'True'
    }
    assert app.evaluate(question, 'TRUE') == 1
    assert app.evaluate(question, 'T') == 1
    assert app.evaluate(question, 1) == 1
    assert app.evaluate(question, 'F') == 0
    assert app.evaluate(question, '123') == 0
    assert app.evaluate(question, '') == 0

def test_evaluate_boolean_false():
    question = {
        'type': 0,
        'answer': 'False'
    }
    assert app.evaluate(question, 'FALSE') == 1
    assert app.evaluate(question, 'F') == 1
    assert app.evaluate(question, 0) == 1
    assert app.evaluate(question, 'T') == 0
    assert app.evaluate(question, '123') == 0
    assert app.evaluate(question, '') == 0

def test_evaluate_multiple_choice():
    question = {
        'type': 1,
        'choices': ['PDF', 'XLS', 'CSV', 'TXT', 'XML'],
        'answer': 'CSV'
    }
    answer = 'C'
    print(f'score is {app.evaluate(question, answer)}')
    assert app.evaluate(question, 'C') == 1
    assert app.evaluate(question, 'c') == 1
    assert app.evaluate(question, ' c ') == 1
    assert app.evaluate(question, 'a') == 0
    assert app.evaluate(question, 'ca') == 0
    assert app.evaluate(question, 'c     a') == 0

def test_evaluate_multiple_answers():
    question = {
        'type': 2,
        'answers': [
            'if you want to identify under-utilized EC2 instances that may be downsized on an instance by instance basis within the same instance family',
            'if you want to understand the potential impact on your AWS bill by taking into account your RIs and Savings Plans'
        ],
        'wrongs': [
            'if you want to look at instance type recommendations beyond downsizing within an instance family',
            'if you want to understand the performance risks and how your workload would perform on various EC2 instance options to evaluate the price-performance trade-off for your workloads'
        ],
        'choices': [
            'if you want to look at instance type recommendations beyond downsizing within an instance family',
            'if you want to understand the performance risks and how your workload would perform on various EC2 instance options to evaluate the price-performance trade-off for your workloads',
            'if you want to identify under-utilized EC2 instances that may be downsized on an instance by instance basis within the same instance family',
            'if you want to understand the potential impact on your AWS bill by taking into account your RIs and Savings Plans'
        ]
    }
    assert app.evaluate(question, 'c d '.upper()) == 1
    assert app.evaluate(question, 'cd'.upper()) == 1
    assert app.evaluate(question, ' d c '.upper()) == 1
    assert app.evaluate(question, 'dc'.upper()) == 1
    assert app.evaluate(question, 'ab'.upper()) == 0
    assert app.evaluate(question, 'ac'.upper()) == 0
    assert app.evaluate(question, 'acd'.upper()) == 0
    assert app.evaluate(question, 'cd a'.upper()) == 0


