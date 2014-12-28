from functools import wraps
from api import BCFerriesAPI

class BCFerriesAbstractObject(object):
  def __str__(self):
    return "{} ({})".format(self.__class__.__name__, self.name)

  def __repr__(self):
    return self.__str__()

def cacheable(f):
  @wraps(f)
  def wrapper(self, *args, **kwargs):
    ignore_cache = kwargs.get('ignore_cache', False)
    if 'ignore_cache' in kwargs:
      del kwargs['ignore_cache']
    if ignore_cache is True:
      BCFerriesAPI.ignore_cache = True
      result = f(self, *args, **kwargs)
      BCFerriesAPI.ignore_cache = False
      return result
    else:
      return f(self, *args, **kwargs)
  return wrapper
