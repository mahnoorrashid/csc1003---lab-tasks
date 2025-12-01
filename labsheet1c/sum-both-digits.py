1 #!/usr/bin/env python3
2 
3 s = input()
4 total = 0
5 
6 i = 0
7 while i < len(s):
8     total = total + int(s[i])
9     i = i + 1
10 print(total)
