import math
degree=input('enter the degree:')
degree=int(degree)
tan = math.tan(math.radians(degree))
sin = math.sin(math.radians(degree))
cos = math.cos(math.radians(degree))
sec = 1/cos
cot = 1/tan
cosec = 1/sin
print (f'tan: {tan},\nsin:{sin},\ncos:{cos},\nsec:{sec},\ncot:{cot},\ncosec:{cosec} ' )
