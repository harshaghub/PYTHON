animals = ['cow', 'bear', 'deer']

sorted_animals = sorted(animals)
print('Animals list:              {}'.format(animals))
print('Sorted animals list:       {}'.format(sorted_animals))
animals.sort()
print('Animals after sort method: {}'.format(animals))


animals2=['pig', 'tiger', 'lion']
more_animals = ['elephant', 'giraffe']
all_animals = animals + animals2 + more_animals

print(all_animals)

print(len(all_animals))
all_animals.append('zebra')
print(len(all_animals))

print("***********This is next script************")
for number in range(3):
    print(number)

print("***********This is next script************")
for number in range(2,6):
    print(number)

print("***********This is next script************")
for number in range(1,10,2):
    print(number)

print("***********This is next script************")
for number in range(0,len(all_animals),2):
    print(all_animals[number])
