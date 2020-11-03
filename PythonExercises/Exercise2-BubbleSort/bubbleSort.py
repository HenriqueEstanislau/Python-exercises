print('-----------')
print('Bubble sort')
print('-----------')

numbers = [1,13, 16, 3, 8, 5, 9]
temp = 0

print("numbers before: ", numbers)
for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
print("numbers after:  ",numbers)


numbers2 = [143,33, 92, 75, 107, 123, 49]
print("\nnumbers2 before: ",numbers2)

for i in range(len(numbers2)):
    for j in range(len(numbers2)-1):
        if numbers2[j] > numbers2[j+1]:
            numbers2[j], numbers2[j+1] = numbers2[j+1], numbers2[j]
print("numbers2 after:  ",numbers2)
