# John Rey Bulfa
# ITELEC2
# Laboratory #16 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def main():
    import math
    def circle_area(radius):
        area = math.pi * (radius ** 2)
        return area
    radius_value = 5
    area_result = circle_area(radius_value)
    print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")

if __name__ == "__main__":
    main()