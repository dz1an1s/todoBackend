import json
import os


def print_with_indent(value, indent=0):
    indentation = '\t' * indent
    print (f"{indentation}{value}")


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def add_entry(self, entry):
        self.entries.append (entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent (self, indent)
        for entry in self.entries:
            entry.print_entries (indent + 1)

    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json () for entry in self.entries]
        }
        return res

    def save(self, path):
        p = os.path.join (path, f'{self.title}.json')
        content = self.json ()
        with open (p, 'w', encoding='utf-8') as f:
            json.dump (content, f)

    @classmethod
    def from_json(cls, value):
        new_entry = Entry (value['title'])
        for sub_entry in value.get ('entries', []):
            new_entry.add_entry (cls.from_json (sub_entry))
        return new_entry

    @classmethod
    def load(cls, filename):
        with open (filename, 'r', encoding='utf-8') as f:
            content = json.load (f)
        a = cls.from_json (content)
        return a

    def __str__(self):
        return self.title


class EntryManager:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries = []

    def load(self):
        if not os.path.isdir (self.data_path):
            os.makedirs (self.data_path)
        else:
            for filename in os.listdir (self.data_path):
                if filename.endswith ('.json'):
                    entry_path = os.path.join (self.data_path, filename)
                    entry = Entry.load (entry_path)
                    self.entries.append (entry)
        return self

    def save(self):
        for i in self.entries:
            i.save (self.data_path)

    def add_entry(self, title: str):
        self.entries.append (Entry (title))

# grocery_list = {
#   "title": "Продукты",
#   "entries": [
#     {
#       "title": "Молочные",
#       "entries": [
#         {
#           "title": "Йогурт",
#           "entries": []
#         },
#         {
#           "title": "Сыр",
#           "entries": []
#         }
#       ]
#     }
#   ]
# }

# entry_from_json(grocery_list)

# groceries = Entry('Продукты')
# category = Entry('Мясное')

# category.add_entry(Entry('Курица'))
# category.add_entry(Entry('Говядина'))
# category.add_entry(Entry('Колбаса'))

# groceries.add_entry(category)

# groceries.print_entries()


# 
