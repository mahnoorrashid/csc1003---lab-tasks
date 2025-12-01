1 #!/usr/bin/env python3
2 
3 weight = int(input())
4 height = int(input())
5 
6 bmi = weight / (height * height) * 10000
7 
8 if bmi >= 30:
9     print("obese")
10 elif bmi >= 25:
11     print("overweight")
12 elif bmi >= 18.5:
13     print("normal")
14 elif bmi < 18.5:
15     print("underweight")
