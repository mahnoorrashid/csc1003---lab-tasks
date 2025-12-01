1 #!/usr/bin/env python3
2 
3 longest_side = int(input())
4 side1 = int(input())
5 side2 = int(input())
6 
7 sides = [longest_side, side1, side2]
8 
9 right_angle = sides[0]**2 == sides[1]**2 + sides[2]**2
10 
11 print(right_angle)
