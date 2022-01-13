class SetGet:
  @classmethod
  def get(self, dict, path):
    print('hello get.')

  @classmethod
  def set(self, dict, path, value):
    print('hello set', dict)

class nx(SetGet):
  @classmethod
  def each(self, list, fn):
    print('each.')


dict1 = {
  "a": {
    "b": {
      "c": 'abc'
    }
  }
}

nx.get(dict1, 'a.b.c')
nx.set(dict1, 'a.b.c', 'hello')
