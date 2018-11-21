class Const(object):
    class ConstError(PermissionError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            raise self.ConstError( "Can't rebind const(%s)" % name)
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const(%s)" % name)
        raise NameError(name)



import sys
sys.modules[__name__] = Const()

from contant_example import constant
# set your constant
constant.MY_CONSTANT = 1
constant.MAX_COUNT = 100
