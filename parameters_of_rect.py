print("Enter dimensions of rectangle: ")
length = int(input())
width = int(input())
height = int(input())

meta = length + width + height

Sum_of_length = meta * 4
print(Sum_of_length)

psilo = (length * width) + (width * height) + (length * height)

Surface_Area = psilo * 2
print(Surface_Area)

Volume = length * width * height
print(Volume)
