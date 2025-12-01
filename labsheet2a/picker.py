1 #!/usr/bin/env python3
2 
3 a = int(input())
4 b = int(input())
5 c = int(input())
6 
7 evenorodd = c % 2
8 print(a - (a * evenorodd) + (b * evenorodd))
