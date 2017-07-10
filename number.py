def odd_or_even(number):
    """Determine if the number is ODD or EVEN"""
    if number % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'
x=int(input('Enter the number:'))

odd_or_even_string = odd_or_even(x)
print(odd_or_even_string)
