import inspect

def introspection_info(obj):
  

  info = {}
  info['type'] = type(obj)
  info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))] # Исправлено: атрибуты - это то, что не является callable
  info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
  info['module'] = inspect.getmodule(obj)  # Используем inspect для определения модуля

  # Дополнительная информация в зависимости от типа объекта:
  if isinstance(obj, str):
    info['length'] = len(obj)
  elif isinstance(obj, list):
    info['length'] = len(obj)
    info['elements'] = obj
  elif isinstance(obj, dict):
    info['length'] = len(obj)
    info['keys'] = list(obj.keys())
    info['values'] = list(obj.values())

  return info

# Создание собственного класса
class MyClass:
  def __init__(self, value):
    self.value = value

  def get_value(self):
    return self.value

# Тестирование
number_info = introspection_info(42)
print("Информация о числе:", number_info)

string_info = introspection_info("Hello, world!")
print("Информация о строке:", string_info)

list_info = introspection_info([1, 2, 3])
print("Информация о списке:", list_info)

dict_info = introspection_info({'key1': 'value1', 'key2': 'value2'})
print("Информация о словаре:", dict_info)

my_object = MyClass(10)
object_info = introspection_info(my_object)
print("Информация о созданном объекте:", object_info)
