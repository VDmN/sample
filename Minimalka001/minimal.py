import random
k_random = random.randint(10, 99)
random.seed(777)   # дальше имеем предсказуемый рандом


def list_random(xxx):   # Перемешивание спика и каждого его элемента.
    for j in range(len(xxx)):
        xxx[j] = random.sample(xxx[j], len(xxx[j]))
    random.shuffle(xxx)
    return (xxx)


spis_1 = ['ue7Ятatc0OKб',
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
          ]   # солянка из алфавитов

spis_1 = list_random(spis_1)
x, y = int(str(k_random)[0]), int(str(k_random)[1])
alpha_x   = spis_1[x][y]


while 1:
    tel_num = input('Введите 10-значный номер, и получите шифровку - 6 знаков: ')
    if tel_num.isdigit() and len(tel_num) == 10:
        break
    else:
        print('Некорректный ввод!')


for j in range(k_random):
    spis_1 = list_random(spis_1)


s = [[0] * 2 for _ in range(len(tel_num) // 2)]

k = 0
for j in range(len(tel_num) // 2):
    s[j][0] = int(tel_num[k])
    s[j][1] = int(tel_num[k + 1])
    k += 2

sxx = ''
for j in s:
    spis_1 = list_random(spis_1)
    sxx += spis_1[j[0]][j[1]]

sxx += alpha_x
print('Вот ваша шифровка:', sxx, sep='\n')
