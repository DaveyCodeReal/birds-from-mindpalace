
import random

birdName1  = ['Great', 'Hover', 'Shrieking', 'Common', 'Rare']
print(random.choice(birdName1), end=' ')

birdName2 = ['Gull', 'Flaplet', 'Nightjar', 'Sparrow', 'Finch']
print(random.choice(birdName2))

wingDesc1 = ['peculiar', 'practical', 'twitchy', 'smelly', 'Very long']  
print(random.choice(wingDesc1), end=' ')

wingDesc2 = ['Olive green', 'pink and gold', 'silver', 'blue', 'rainbow'] 
print(random.choice(wingDesc2), end='')

print (' wings and', end=' ')

addDesc = ['bold red spots on breast.', 'sad little face.', 'long gangly legs.', 'long thick beak.', 'fluffy little muttonchops.', 'tiny pathetic beak.', 'long brown tail.'] 
print(random.choice(addDesc))

habPreface = ['Usually found in', 'Generally found in', 'Typically found in', 'Most often found in', 'Can be found in', 'Look for it in'] 
print(random.choice(habPreface), end=' ')

birdHabitat = ['Peru', 'Northern Ireland', 'Fresno', 'Cold Stone Creamery', 'Oakland CA', 'Large hollow trees with cookie-making elves.', 'The perfume section.', 'Grocery Outlet, bargain market', 'Brooklyn, New York delicatesens', 'Boulder, Colorado', 'The greater Sacramento area'] 
print(random.choice(birdHabitat))

callPreface = ['The call is', 'The call is', 'The most common call is', 'The typical call is', 'Vocalization is', 'Listen for its call,', 'Often heard before seen. Listen for', 'Typical song is'] 
print(random.choice(callPreface), end=' ')

birdCall = ['X', 'X', 'X', 'X', 'X', 'X'] 
print(random.choice(birdCall))
