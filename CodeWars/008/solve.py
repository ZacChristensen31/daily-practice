# Problem comes from CodeWars
# Solved on Tuesday May 17th, 2022

def zero(func=None): return base(0, func)
def one(func=None):  return base(1, func)
def two(func=None):  return base(2, func)
def three(func=None):  return base(3, func)
def four(func=None):  return base(4, func)
def five(func=None):  return base(5, func)
def six(func=None):  return base(6, func)
def seven(func=None):  return base(7, func)
def eight(func=None):  return base(8, func)
def nine(func=None):  return base(9, func)

def base(num: int, func=None): return num if not func else func(num)


def plus(y): return lambda x: x + y
def minus(y):  return lambda x: x - y
def times(y):  return lambda x: x * y
def divided_by(y): return lambda x: x // y

if __name__ == '__main__':
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3