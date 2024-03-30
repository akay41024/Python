while True:
    print("Geometry Area Calculator")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        radius = int(input("Enter the radius: "))
        area = 3.14 * radius * radius
        print("Area of circle: ", area)
    elif choice == 2:
        side = int(input("Enter the side: "))
        area = side * side
        print("Area of square: ", area)
    elif choice == 3:
        length = int(input("Enter the length: "))
        breadth = int(input("Enter the breadth: "))
        area = length * breadth
        print("Area of rectangle: ", area)
    elif choice == 4:
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        area = 0.5 * base * height
        print("Area of triangle: ", area)
    elif choice == 5:
        break
    else:
        print("Invalid choice")
    
    print()
