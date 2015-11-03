''' Синхронизовать словари en-ru.txt и ru-en.txt
'''
en_ru=dict()
ru_en=dict()
#--- чтение из файлов ----
in_f=open('en-ru.txt')
s=in_f.readline().rstrip()
while len(s)>0:
    en,ru=list(s.split('\t-\t'))
    en_ru[en]=ru
    s=in_f.readline().rstrip()

in_f=open('ru-en.txt')
s=in_f.readline().rstrip()
while len(s)>0:
    ru,en=list(s.split('\t-\t'))
    ru_en[ru]=en
    s=in_f.readline().rstrip()
#--- синхронизация -------
ru_en1=ru_en.copy()
for i in en_ru:
    if en_ru[i] in ru_en: # # если есть такое значение
        ru_en[en_ru[i]]=ru_en[en_ru[i]]+', '+i
    else:
        ru_en[en_ru[i]]=i

for i in ru_en1:
    if ru_en1[i] in en_ru: # # если есть такое значение
        en_ru[ru_en1[i]]=en_ru[ru_en1[i]]+', '+i
    else:
        en_ru[ru_en1[i]]=i
#---- запись в файлы -------
out_f=open('en-ru.txt','w')
key_sort=sorted(en_ru.keys())
for i in key_sort:
    print('\t-\t'.join( (i,en_ru[i]) ),file=out_f)

out_f=open('ru-en.txt','w')
key_sort=sorted(ru_en.keys())
for i in key_sort:
    print('\t-\t'.join( (i,ru_en[i]) ),file=out_f)