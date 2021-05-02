def fiz_buz(n):
    temp = []
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            temp.append('FizzBuzz')

        if i % 3 == 0:
            temp.append('Fizz')
        if i % 5 == 0:
            temp.append('Buzz')

        temp.append(str(i))