answer = input('you are at a crossroads, go right or left: ')

if answer == 'right':
    answer = input('You are in a forest and encounter a monster, run or attack? ')

    if answer == 'attack':
        print('The monster killed you\nGAME OVER')

    else:
        print('Good idea, you got away')
        answer = input('You encounter a boat and a plane, which would you like to take? ')

        if answer == 'plane':
            print('You do not know how to fly a plane and ypu die\nGAME OVER')

        else:
            print('You sped off in the boat')
            answer = input('You come across two islands, one with zombies, the other with a dragon on it. Which one do you go to? (zombies/dragon) ')

            if answer == 'zombies':
                print('You go to the zombie island and they want to eat your brains, you die\nGAME OVER')

            else:
                print('You go to the dragon island and luckily the dragon turns out to be friendly. You make friends with the dragon and ride with him off into the sunset\nCongratulations on beating the text adventure game')

elif answer == 'left':
    print('You fell off a cliff and died, tough luck\nGAME OVER')

else:
    print('Please enter a valid input')