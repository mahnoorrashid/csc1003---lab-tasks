1 #!/usr/bin/env python3
2 
3 number = int(input())
4 
5 if number % 3 == 0 and number % 5 == 0:
6     print('fizz-buzz')
7 elif number % 3 == 0:
8     print('fizz')
9 elif number % 5 == 0:
10     print('buzz')
11 else:
12     print(number)
