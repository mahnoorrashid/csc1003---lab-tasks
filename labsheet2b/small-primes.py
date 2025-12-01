1 #!/usr/bin/env python3
2 
3 num = int(input())
4 
5 if num == 2 or num == 3:
6     print("prime")
7 elif num % 2 == 0 or num % 3 == 0 or num == 1:
8     print("not prime")
9 else:
10     print("prime")
