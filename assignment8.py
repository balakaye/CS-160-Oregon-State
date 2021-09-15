def printLetterOccurances(names: list) -> list:
    
    letters = {}
    for name in names:
        for chars in name:
            try:
                letters[chars] += 1

            except:
                letters[chars] = 1
            
    print(letters)


def sortNames(names: list) -> list:
    new_names = []
    lowest = names[0]

    while len(names) != 0:
        lowest = names[0]
        for name in names:
            if ord(name[0]) <= ord(lowest[0]):
                lowest = name
        new_names.append(lowest)
        names.remove(lowest)
    return new_names

def main():
    names = []
    num_names = int(input('How many names do you want?(#): '))

    for i in range(num_names):
        names.append(input('Enter a name: '))

    print(printLetterOccurances(names))
    print(sortNames(names))


main()