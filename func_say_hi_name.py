def say_hi(name):
    """This is just to say Hi and respect"""
    print('Hi {}!'.format(name))

say_hi('Jason')
say_hi('Everybody')

def say_who(name= 'there'):
    print('Hi {}!'.format(name))

say_who()
say_who('HARSHA')


def say_me(first,middle,last):
    print('Hi {} {} {}!'.format(first,middle,last))

say_me('HARSHA','SHIVAPPA','PUJAR')
say_me(middle='HARSHA',first='AVANEESH',last='PUJAR')
say_me(last='PUJAR',first='AYUSHMAN',middle='HARSHA')
