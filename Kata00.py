# Write a function that returns the total surface area and volume of a box as an array: [area, volume].
#CodeWar Challenge

box_measurements = []

length = int(input("Input Length: "))
width = int(input("Input Width: "))
height = int(input("Input Height: "))

volume = length * width * height
area = length * width

box_measurements.append(area)
box_measurements.append(volume)
print(box_measurements)
