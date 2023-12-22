class BaseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

# 复数错误
class PluralElementError(BaseError):
    """
        当要求长度是1时，实际长度大于1会报错
    """
    pass

class DifferError(BaseError):
    """
        当两个本应相同的值或对象不一致时会报错
    """
    pass

class SameError(BaseError):
    """
        当两个本应不同的值或对象一致时会报错
    """
    pass

class FindNoElementError(BaseError):
    """
        没有找到元素会报错
    """
    pass

class FindElementError(BaseError):
    """
        找到元素会报错,这个元素应该消失
    """
    pass

class CompareError(BaseError):
    """
        比大小结果不正确时，会报错
    """
    pass

class MoveError(BaseError):
    """
        移动时距离有问题，会报错
    """
    pass

class InvalidOperationError(BaseError):
    pass