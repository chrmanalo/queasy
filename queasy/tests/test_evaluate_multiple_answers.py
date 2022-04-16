from queasy import app

def test_evaluate_multiple_answers():
    question = {
        'type': 2,
        'choices': ['PDF', 'XLS', 'CSV', 'TXT', 'XML'],
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
    answer = 'abb bscde'.upper()
    print(f'score is {app.evaluate(question, answer)}')

if __name__ == '__main__':
    test_evaluate_multiple_answers()