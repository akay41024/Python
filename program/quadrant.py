x = float(input("Enter x-quadrant: "))
y = float(input("Enter y-quadrant: "))

if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-Axis")
elif y == 0:
    print("X-Axis")
else:
    print("On Axis but not in any Quadrant")
