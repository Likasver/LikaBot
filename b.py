import cProfile
def main():
n=int(input('Введите число N:'))
summa=sum(range(1,N+1))
print(f'Сумма чисел от 1 до {N} равна {summa}')
if_name_=='_main_':(
    cProfile.run('main()'))