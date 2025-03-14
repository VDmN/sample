import random
random.seed(333)

a = 'УйссБkА'
a2 = a[1:-1]

def list_random(xxx):
    for j in range(len(xxx)):
        random.shuffle(xxx)
        xxx[j] = ''.join(random.sample(xxx[j], len(xxx[j])))        
    return(xxx)


spis = ['ue7Ятatc0OKб',
        'DЪукТЫjsчГлvwю',
        'А5XPхсжdNФшЬBъ',
        'Нx2GRVЖzБиД9',
        'вфЦQ|rЕВiЩ4цС',
        'ClqHokIЮКИ',
        'm+J&эh,Ё3ЗО',
        'E6YыШ1МПьL',
        'S.bёгЛWЙдерйf',
        'ZУРMнnзyAапмU',
        'яЭЧ8FоХgTpщ'
        ]

spis = list_random(spis)

k_rand = ''
for j in range(len(spis)):
    if a[0] in spis[j]:
        k_rand += str(j)
        k_rand += str(spis[j].index(a[0]))
#print(k_rand)

for _ in range(int(k_rand)):
    spis = list_random(spis)

txx = ''
for j in a2:
    spis = list_random(spis)
    for k in range(len(spis)):
        if j in spis[k]:
            txx += str(k) + str(spis[k].index(j))
print(txx)