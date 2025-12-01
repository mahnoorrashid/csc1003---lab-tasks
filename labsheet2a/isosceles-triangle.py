1 #!/usr/bin/env python3
2 
3 side1 = int(input())
4 side2 = int(input())
5 side3 = int(input())
6 
7 isosceles = (side1 == side2) or (side2 == side3) or (side1 == side3)
8 print(isosceles)
