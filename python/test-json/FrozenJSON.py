from collections import abc
from keyword import iskeyword
import json
import time


def from_json(json_object):
  if '__class__' in json_object:
    if json_object['__class__'] == 'time.asctime':
      return time.strptime(json_object['__value__'])
    if json_object['__class__'] == 'bytes':
      return bytes(json_object['__value__'])
  return json_object


class FrozenJSON:

  def __new__(cls, arg):
    if isinstance(arg, abc.Mapping):
      return super().__new__(cls)
    elif isinstance(arg, abc.MutableSequence):
      return [cls(item) for item in arg]
    else:
      return arg

  def __init__(self, mapping):
    self.__data = {}
    for key, value in mapping.items():
      if iskeyword(key):
        key += '_'
      self.__data[key] = value

  def __getattr__(self, name):
    if hasattr(self.__data, name):
      return getattr(self.__data, name)
    else:
      return FrozenJSON(self.__data[name])


if __name__ == '__main__':
  entry_json = None
  with open('entry.json', 'r', encoding='utf-8') as f:
    entry_json = json.load(f, object_hook=from_json)
  print(entry_json)
  frozenJSON = FrozenJSON(entry_json)
  print(frozenJSON.keys())
  print(frozenJSON.published_date)
  print(frozenJSON.comments_link)
  print(frozenJSON.internal_id)
  print(frozenJSON.tags)
  print(frozenJSON.title)
  print(frozenJSON.article_link)
  print(frozenJSON.published)
