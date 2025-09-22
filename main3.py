data_tuple = ('s', 6.13,'C','e','T',True,'k','e',3,'e',1,'g')
data_tuple = list(data_tuple)
letters = []
numbers = []
for i in data_tuple: 
    if type (i) == str:
        letters.append(i)
    else:
        numbers.append(i)
        
numbers.remove(6.13)

numbers.remove(True)
letters.append(True)

numbers.sort()
letters.reverse()

letters = letters[:5] + [letters[-1]]

print('letters: ',letters)
print('numbers:', numbers)
