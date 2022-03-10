from database import *

def extract_route(s):
    split = s.split()
    route = split[1]
    return route[1:]

def read_file(path):
    with open(path, 'rb') as file:
        content = file.read()
    return content

def load_data(Database):
    data = Database.get_all()
    return data

def load_template(file_name):
    with open("templates/"+file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}'
    if len(headers):
        response+= f'\n{headers}'

    response+= f'\n\n{body}'
    return response.encode()
