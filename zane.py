# Zane's Function
def rect_surface_area(length, width, height):
    # takes parameters length, width, height (int) and returns surface area
    return 2 * (rect_area(length, width) + rect_area(length, height) + rect_area(width, height))