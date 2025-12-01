1 #!/usr/bin/env python3
2 
3 n = int(input())
4 
5 third_dig = n % 10
6 n = n // 10
7 
8 second_dig = n % 10
9 n = n // 10
10 
11 first_dig = n % 10
12 n = n // 10
13 
14 print(first_dig)
15 print(second_dig)
16 print(third_dig)
