x = input('Enter one of the following foods: Chocolate, Ice cream, Tacos, Steak, Chicken, Strogonoff, Pasta: ')
y = input('Enter a fun fact: french, sleep, brazil, nose, skydive, music, minecraft, plane, texas, twin, football, skis: ')

if x == 'Chocolate':
    if y == 'french':
        print('Lucas loves that food and is also 20 percent french!')
elif y== 'skydive':
    print('Blake loves that food and has also skydived!')
if x == 'Ice cream':
    if y == 'sleep':
        print('Cheng loves ice cream and loves to sleep')
if x== 'Tacos':
    if y == 'minecraft':
        print('Bob loves that food and minecraft!')
elif y == 'plane':
    print('John loves tacos and has never been on an airplane before!')
if x== 'Chicken':
    if y == 'music':
        print('Sylvester loves chicken and every type of music!')
if x== 'Strogonoff':
    if y == 'brazil':
        print('George loves that food and is from Brazil!')
if x == 'Steak':
    if y == 'nose':
        print('Ethan likes steak and never gets bloddy noses')
if x == 'Pasta':
    if y == 'texas':
        print('Ava is from Texas and likes pasta.')
    elif y == 'twin':
        print('Emily is a twin and also likes pasta.')
    elif y == 'football':
        print('Tanner plays football and also likes pasta.')
    elif y == 'skis':
        print('Jack skis and also likes pasta.')
else:
    print('No one has that combo of favorite food and fun fact!')





food = input('What is this persons favorite food? Ribs or Chocolate: ')
fact = input('What is their fun fact? 20 percent french, 11 toes, only child: ')

if food == 'Chocolate':
    if fact == '20 percent french':
        print('Lucas likes Chocolate and is 20 percent french!')
else:
    print('You should get to know Lucas.')
    