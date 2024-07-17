# try:
#     10/0
# except ZeroDivisionError:
#     print('cannot divide by 0')
    
# try:
#     result=10/int('string')
# except (ZeroDivisionError, ValueError) as e:
#     print(f'Error: {e}')

# def check_positive(no):
#     if no<=0:
#         raise ValueError("No not positive")
#     return no
# try:
#     check_positive(-10)
# except ValueError as e:
#     print(e)

# def leap_year(year):
#     if year%4!=0:
#         raise ValueError('Not leap year')
#     return year
# try:
#     a=int(input('enter year'))
#     leap_year(a)
# except ValueError as e:
#     print(e)

class NegativeNoError(Exception):
    def __init__(self,no,msg='no must be positive'):
        self.no=no
        self.msg=msg
        super().__init__(self.msg)
def divide(a,b):
    try:
        if a<0 or b<0:
            raise NegativeNoError(a if a<0 else b)
        result=a/b
    except ZeroDivisionError:
        print('Cannot divide by 0')
    except NegativeNoError as ne:
        print(f'error: {ne}')
    except Exception as e:
        print(f'unexpected error: {e}')
    else:
        print(f'result: {result}')
    finally:
        print('Execution done')
divide(10,0)
divide(-10,5)
divide(10,2)