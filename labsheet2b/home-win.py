1 #!/usr/bin/env python3
2 
3 home_score = int(input())
4 away_score = int(input())
5 
6 if home_score > away_score:
7     print("Home win.")
8 elif home_score < away_score:
9     print("Away win.")
10 else:
11     print("Draw.")
