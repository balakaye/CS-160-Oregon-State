
#count numbers in a list of names
'''
name = [bob, blake, elliot, ryan, george]

output_dict = {}
for i in name:
    if i in output_dict:
        output_dict[i] += 1
    else:
        output_dict[i] = 1
for i in output_dict:
    print("Frequency of Letters: ", i, "-", output_dict[i])
    
def print_letters(names: list):
    for name in names:
        print(name)
    for ch in name:
        print(ch)

def get_letter_occur(names: list) -> list:
    occurances = [0] * 128
    concat_string = ''
    for i in names:
        concat_string += i
    for i in concat_string:
        occurances[ord(i)] += 1

def main():
    Input = [] #create an empty list, but you need a list to append to it

    num_names=int(input("How many names do you want to enter? "))
    for i in range(num_names):
        names.append(input("Enter a name: "))
    print_letters(names)
    get_letter_occur(names)
main()
'''
def count_letters():
    diction ={}
    characterlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in characterlist:
        diction[i]= Input.count(i,0,100)
        if diction[i]==0:
            del diction[i]

    for k in diction:
        print(k,':', diction[k])
def main():
    Input = [] #create an empty list, but you need a list to append to it

    num_names=int(input("How many names do you want to enter? "))
    for i in range(num_names):
        Input.append(input("Enter a name: "))
    count_letters()
main()

