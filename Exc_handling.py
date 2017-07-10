animals = ['man','cat','pig','bear']
try:
    ani_index = animals.index('LION','cat')
except:
    ani_index = 'No LIONs Found'
print(ani_index)
