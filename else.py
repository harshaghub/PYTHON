distance=input('how far would you like to travel in miles?:')
distance=float(distance)
if distance<3:
    mode_of_transport='walking'
elif distance<300:
    mode_of_transport='driving'
else: 
    mode_of_transport='flying'
    
print('I suggest {} to your destination.'.format(mode_of_transport))
print('Have a nice TRIP!!!:-)')
