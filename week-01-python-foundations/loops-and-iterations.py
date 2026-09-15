#Day 6 - Loops and Iterations

#for loop
nums = (1, 2, 3, 4, 5)
for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)

dict = {"name": "Somesh", "age": 25, "city": "New York"}
for key in dict:
    if key == "age":
        print("Age is found!")
        break

for key, value in dict.items():
    if key == "age":
        print(value)

for i in range(1, 11):
    print(i)


#while loop
x = 0
while x<5:
    if x == 3:
        print("Found!")
        break
    print(f"The value of x is: {x}")
    x += 1
