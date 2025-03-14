import random
k_xxx = random.randint(10, 99)
random.seed(333)
from copy import deepcopy


while 1:
    tel_num = input('Введите 10-значный номер: ')
    if tel_num.isdigit() and len(tel_num) == 10:
        break
    else:
        print('Некорректный ввод!')
        
def list_random(xxx):
    for j in range(len(xxx)):
        random.shuffle(xxx)
        xxx[j] = ''.join(random.sample(xxx[j], len(xxx[j])))        
    return(xxx)      
        
    
spis_2 = ['ue7Ятatc0OKб',
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

spis_2 = list_random(spis_2)

spis_1 = deepcopy(spis_2)


s = [[0]*2 for _ in range(len(tel_num) // 2)]

k = 0
for j in range(len(tel_num) // 2):
    s[j][0] = int(tel_num[k])
    s[j][1] = int(tel_num[k+1])
    k += 2


# print(k_xxx)
for _ in range(k_xxx):
    spis_1 = list_random(spis_1)


sxx = ''
for j in s:
    spis_1 = list_random(spis_1)
    sxx += spis_1[j[0]][j[1]]
    
k_xxx = list(map(int, list(str(k_xxx))))
# print(k_xxx)
    
print(f'{spis_2[k_xxx[0]][k_xxx[1]]}{sxx}{random.choice(spis_1[1])}')
            
            