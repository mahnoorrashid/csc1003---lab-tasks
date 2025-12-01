1 #!/usr/bin/env python3
2 
3 mark = int(input())
4 
5 if 40 > mark:
6     print("first: False")
7     print("second: False")
8     print("third: False")
9     print("fail: True")
10 elif 40 <= mark <= 49:
11     print("first: False")
12     print("second: False")
13     print("third: True")
14     print("fail: False")
15 elif 50 <= mark <= 69:
16     print("first: False")
17     print("second: True")
18     print("third: False")
19     print("fail: False")
20 elif 70 <= mark:
21     print("first: True")
22     print("second: False")
23     print("third: False")
24     print("fail: False")
