def decorator(func):
    def decorated(width, height):
        if width > 0 and height > 0:
            func(width, height)
        else:
            print('Error')
    return decorated

@decorator
def three_angle(width, height):
    th = width * height * 0.5
    print(th)

@decorator
def four_angle(width, height):
    fo = width * height
    print(fo)

three_angle(3, 4)
four_angle(3, 4)



#-----------------------

def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            func(width, height)
        else:
            raise ValueError('Input must be positive value')
    return decorated

@ check_integer
def


@check_integer
def

#-----------------------

class User:
    def __init__(self, auth):
        self.is_authenticated = auth

user = User(auth=False)

r_area = rect_area(user, 10, 10)


def login_required(func):
    def decorated(user, width, height):
        if user.is_authenticated:
            func(user, width, height)
        else:
            raise PermissionError('Login required')
    return decorated


def decorator(func):
    def decorated(user, width, height):
        if width > 0 and height > 0:
            func(user, width, height)
        else:
            print('Error')

    return decorated


@decorator
@
def three_angle(width, height):
    th = width * height * 0.5
    print(th)


@decorator
def four_angle(width, height):
    fo = width * height
    print(fo)


three_angle(3, 4)
four_angle(3, 4)



