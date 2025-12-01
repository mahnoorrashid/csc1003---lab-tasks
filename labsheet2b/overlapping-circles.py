1 #!/usr/bin/env python3
2 
3 x1 = int(input())
4 y1 = int(input())
5 r1 = int(input())
6 x2 = int(input())
7 y2 = int(input())
8 r2 = int(input())
9 
10 if ((x2 - x1) ** 2) + ((y2 - y1) ** 2) < (r1 + r2) ** 2:
11     print("yes")
12 else:
13     print("no")
