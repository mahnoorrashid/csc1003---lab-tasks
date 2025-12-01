1 #!/usr/bin/env python3
2 
3 string1 = input()
4 string2 = input()
5 string3 = input()
6 
7 longest_string = string1
8 
9 if len(string2) > len(longest_string):
10     longest_string = string2
11 
12 if len(string3) > len(longest_string):
13     longest_string = string3
14 
15 print(longest_string)
