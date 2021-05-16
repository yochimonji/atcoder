import math

n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

center = ((x0+xn2)/2, (y0+yn2)/2)
r = math.pow((center[0]-x0)**2 + (center[1]-y0)**2, 0.5)
angle = 2*math.pi/n + math.atan2(y0-center[1], x0-center[0])

print(center[0]+r*math.cos(angle), center[1]+r*math.sin(angle))