ru_en=dict()
in_f=open('input.txt')
out_f=open('output.txt','w')
s=in_f.readline().rstrip()
while len(s)>0:
    en,ru=list(s.split('\t-\t'))
    # ru может иметь несколько значений через запятую- разобьем
    if ',' in ru:
        for i in ru.split(','):
            i=i.lstrip()
            if i in ru_en: # если есть такое значение
                ru_en[i]=ru_en[i]+', '+en
            else:
                ru_en[i]=en
    else:
        if ru in ru_en: # # если есть такое значение
            ru_en[ru]=ru_en[ru]+', '+en
        else:
            ru_en[ru]=en

    s=in_f.readline().rstrip()

key_sort=sorted(ru_en.keys())
for i in key_sort:
    print('\t-\t'.join( (i,ru_en[i]) ),file=out_f)
