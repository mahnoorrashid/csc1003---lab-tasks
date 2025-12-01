1 #!/usr/bin/env python3
2 
3 month = int(input()) - 1
4 day = int(input()) - 1
5 
6 day_of_week = (month * 30 + day)
7 print(day_of_week % 7 + 1)
