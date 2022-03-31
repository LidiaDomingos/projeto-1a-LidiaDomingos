from database import Database, Note
from utils import load_data, load_template, build_response
from urllib.parse import unquote_plus

def index(request, Database):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave_valor = unquote_plus(chave_valor)
            index = chave_valor.find("=")
            params[chave_valor[:index]] = chave_valor[index+1:]
        
        add_nota(params, Database)

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id = dados.id,title = dados.title, details = dados.content)
        for dados in load_data(Database)
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)

    if request.startswith('POST'):
        return build_response(body=body, code=303, reason='See Other', headers='Location: /')
    else:
        return build_response(body=body)

def add_nota(params, Database):
    i,j = params.values()
    note = Note(title=i, content=j)
    Database.add(note)

def delete(request, Database):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        print(corpo)
        id, valor = corpo.split('=')
        Database.delete(valor)

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id = dados.id,title = dados.title, details = dados.content)
        for dados in load_data(Database)
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)

    if request.startswith('POST'):
        return build_response(body=body, code=303, reason='See Other', headers='Location: /')
    else:
        return build_response(body=body)

def erro(request):
    return build_response(body=load_template('erro.html'))