

# def mult(*args):
#     result = 1
#     for numero in args:
#         result *= numero
#     return result

# result = mult(2,5,6,8,9,3)
# print(result)

def par_impar(n):
    check = n % 2 == 0
    if check:
        print(f'O número {n} é par!')
        return check
    print(f'O número {n} é impar!')
    return check

print(par_impar(219373642))