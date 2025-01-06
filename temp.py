import os

def list_content(folder):
    for item in os.listdir(folder):
        full_path = os.path.join(folder, item)
        print(full_path)
        if os.path.isdir(full_path):
            list_content(full_path)

list_content('d:/temp')


film = dict(name="A New Hope", year=1977)
film.keys()    # возвращает все ключи (здесь это - 'name', 'year')
film.values()  # возвращает все значения ('A New Hope', 1977)
film.items()   # возвращает все элементы (пары ключ:значения)

film['name']   # возвращает "A New Hope"
film['year']   # возвращает 1977
