from queasy.utils import yaml_reader 

def test_yaml_reader():
    print('Testing yaml_reader...')
    test_data = yaml_reader.read('queasy/tests/data/test_data.yml')
    print(test_data)

if __name__ == '__main__':
    test_yaml_reader()