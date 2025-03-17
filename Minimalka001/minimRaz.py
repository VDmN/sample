import random
random.seed(777)

a = input('Введите зашифрованную 6-ти значную строку : ')
a2 = a[:-1]

def list_random(xxx):
    for j in range(len(xxx)):
        xxx[j] = random.sample(xxx[j], len(xxx[j]))
    random.shuffle(xxx)
    return (xxx)


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
    if a[-1] in spis[j]:
        k_rand += str(j)
        k_rand += str(spis[j].index(a[-1]))
#print(k_rand)

for _ in range(int(k_rand)):
    spis = list_random(spis)


txx = ''
for j in a2:
    spis = list_random(spis)
    for k in range(len(spis)):
        if j in spis[k]:
            txx += str(k) + str(spis[k].index(j))

print(f'Ваш номер: ({txx[:3]})-{txx[3:6]}-{txx[6:8]}-{txx[8:]}')