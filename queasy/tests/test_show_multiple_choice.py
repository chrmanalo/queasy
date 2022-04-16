from queasy import app

def test_show_multiple_choice():
    question = {
        'type': 'Multiple Choice',
        'category': 3,
        'text': 'Which file format is supported when exporting report data from the AWS Cost Explorer?',
        'choices': ['CSV', 'PDF', 'XLS', 'XML', 'TXT']
    }
    app.show_question(question, instruction='Choose the letter of the correct answer.')

if __name__ == '__main__':
    test_show_multiple_choice()