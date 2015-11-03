en_ru=dict()
in_f = open('en-ru.txt', 'r')
s=in_f.readline().rstrip()
while len(s)>0:
    en,ru=list(s.split('\t-\t'))
    en_ru[en]=ru
    s=in_f.readline().rstrip()

in_f = open('input.txt')
out_f=open('output.txt','w')
s=in_f.readline().rstrip()
while len(s)>0:
    en=list(s.split())
    ru=''
    for i in en:
        if i.lower().replace('.','') in en_ru:
            ru+=''+en_ru[i.lower().replace('.','')]
        else:
            ru+=' '+i
            
    print(s,file=out_f)
print(ru.lstrip(),file=out_f)
    s=in_f.readline().rstrip()
