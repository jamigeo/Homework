power = lambda friend: friend*friend

for i in range (1, 114):
    print ('{}^2 = {}'.format (i, power (i)))
print()

pro = lambda friend, girlfriend: friend*girlfriend

for i in range (2, 365):
    for j in range (4, 500):
        print ('{}*{} = {}'.format (i, j, pro (i, j)))
print()

girl_friend = lambda *args: {i: 'girl' if i%2 == 0 else 'friend' for i in args}
print (girl_friend (1, 3, 5, 7, 11, 13, 17, 23))
print ()

output = map (lambda friend: '{:3}'.format (str(friend)) if friend % 8 != 0 else '{:3}\n'.format (str(friend)), range (1, 100))
print (''.join (list(output)))

best = ['Thuy', 'Justine']

sentence = 'I love you!'

no_best = filter (lambda friend: friend.lower() not in best, sentence)
print (''.join (list (no_best)))
print ()

from functools import reduce

num = 23
fac = reduce (lambda friend, girlfriend: friend * girlfriend, [i for i in range (1, num + 1)])
print ('The best of {} is {}.'.format (num, fac))