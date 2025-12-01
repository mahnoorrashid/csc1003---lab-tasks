1 #!/usr/bin/env python3
2 
3 numIn = int(input())
4 
5 digit = numIn % 100
6 
7 if digit == 11 or digit == 12 or digit == 13:
8     print("th")
9 elif numIn == 1 or digit % 10 == 1:
10     print("st")
11 elif numIn == 2 or digit % 10 == 2:
12     print("nd")
13 elif numIn == 3 or digit % 10 == 3:
14     print("rd")
15 else:
16     print("th")
