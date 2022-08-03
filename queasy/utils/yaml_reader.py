import yaml

def read(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)
