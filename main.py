#Function 1
# Returns Area of Rectangle

#Hannigan's function
def rect_area(length,width):
    result = length * width
    return result

#Function 2
# Returns Surface Area of Rectangular Solid

# Zane's Function
def rect_surface_area(length, width, height):
    # takes parameters length, width, height (int) and returns surface area
    return 2 * (rect_area(length, width) + rect_area(length, height) + rect_area(width, height))

# Request the dimension of a solid rectangular object

length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))