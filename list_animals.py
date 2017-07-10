animals = ['cow','bear','deer']
print(animals[0])
print(animals[1])
print(animals[2])

animals.append('pig')
print(animals)
print(animals[3])
print(animals[-1])

more_animals = ['tiger','lion']
animals.extend(more_animals)
print(animals)

animals.extend(['elephant','giraffe'])
print(animals)
print(animals[4])
print(animals[5])

animals.insert(0,'horse')
print(animals)

animals.insert(2,'fish')
print(animals)

some_animals = animals[1:4]
print('Some animals: {}'.format(some_animals))

first_two = animals[0:2]
print('first two animals in the list:  {}'.format(first_two))

first_two_again = animals [:2]
print('first two animals again in the list: {}'.format(first_two_again))

last_two = animals[6:10]
print ('last two anmals in the list: {}'.format(last_two))

last_two_again = animals[-2:]
print ('last two animals again in the list: {}'.format(last_two_again))

slices_string = 'horse'[1:4]
print(slices_string)
