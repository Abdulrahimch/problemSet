import argparse

parser = argparse.ArgumentParser(description='Formatting name and surname')

parser.add_argument('first_name', type=str, help='this is the first name')
parser.add_argument('last_name', type=str, help='this is the last name')

parse = parser.parse_args()

def func(first_name, last_name):
    print(first_name + ' ' + last_name)

if __name__ == '__main__':
    func(parse.first_name, parse.last_name)

'Hi there'
