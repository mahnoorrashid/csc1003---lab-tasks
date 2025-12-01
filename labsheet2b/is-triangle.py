1 #!/usr/bin/env python3
2 
3 a = int(input())
4 b = int(input())
5 c = int(input())
6 
7 if ((a + b) > c) and ((c + b) > a) and ((a + c) > b):
8     print("yes")
9 else:
10     print("no")
