1 #!/usr/bin/env python3
2 
3 year = int(input())
4 leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
5 print(leap)
