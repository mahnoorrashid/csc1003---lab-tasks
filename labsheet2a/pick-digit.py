1 #!/usr/bin/env python3
2 
3 n = int(input())
4 digit = int(input())
5 
6 n = n // (10 ** digit)
7 n = n % 10
8 print(n)
