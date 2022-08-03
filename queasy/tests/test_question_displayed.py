from queasy import app

QUESTION_TEXT_LIMIT = 256

def test_show_multiple_choice(capsys):
    i = 1
    n_items = 10
    question = {
        'domain': 5,
        'type': 1,
        'text': 'Which file format is supported when exporting report data from the AWS Cost Explorer?',
        'choices': ['CSV', 'PDF', 'XLS', 'XML', 'TXT']
    }
    app.show_question(i, question, n_items, instruction='Choose the letter of the correct answer.')
    captured = capsys.readouterr()
    expected_out = ''.join([
        'Domain: Domain 6: Cost and Performance Optimization\n',
        'Instruction: Choose the letter of the correct answer.\n',
        '----------------------------------------------------------------\n'
        'Question (2/10): Which file format is supported when exporting report data from the AWS Cost Explorer?\n'
    ])
    # Limited checking of output because the multiple choice is always randomly shuffled
    assert captured.out[:QUESTION_TEXT_LIMIT] == expected_out[:QUESTION_TEXT_LIMIT]

def test_show_multiple_answers(capsys):
    i = 1
    n_items = 10
    question = {
        'domain': 5,
        'type': 3,
        'text': 'When should you use AWS Cost Explorer?',
        'answers': [
            'if you want to identify under-utilized EC2 instances that may be downsized on an instance by instance basis within the same instance family',
            'if you want to understand the potential impact on your AWS bill by taking into account your RIs and Savings Plans'
        ],
        'wrongs': [
            'if you want to look at instance type recommendations beyond downsizing within an instance family',
            'if you want to understand the performance risks and how your workload would perform on various EC2 instance options to evaluate the price-performance trade-off for your workloads'
        ]
    }
    app.show_question(i, question, n_items, instruction='Choose multiple letters that best satisfy the question.')
    captured = capsys.readouterr()
    expected_out = ''.join([
        'Domain: Domain 6: Cost and Performance Optimization\n',
        'Instruction: Choose multiple letters that best satisfy the question.\n',
        '----------------------------------------------------------------\n'
        'Question (2/10): When should you use AWS Cost Explorer?\n'
    ])
    # Limited checking of output because the multiple answers are always randomly shuffled
    assert captured.out[:QUESTION_TEXT_LIMIT] == expected_out[:QUESTION_TEXT_LIMIT]