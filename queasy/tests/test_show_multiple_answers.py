from queasy import app

def test_show_multiple_answers():
    question = {
        'type': 2,
        'category': 3,
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
    app.show_question(question, instruction='Choose multiple letters that best satisfy the question.')

if __name__ == '__main__':
    test_show_multiple_answers()