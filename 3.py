words = dict()
in_f = open('/usr/share/licenses/python/LICENSE', 'r')
s=in_f.readline().rstrip()
while len(s)>0:
    s=s.replace('.',' ')
    s=s.replace(',',' ')
    s=s.replace('!',' ')
    s=s.replace('?',' ')
    s=s.lower()
    tmp=list(s.split())
    for i in tmp:

		words[i]=words.get(i,0)+1
		s=in_f.readline().rstrip()
max_n=0
max_word=' '
for key in words:
	if words[key]>max_n:
		max_n=words[key]
		max_word=key
print(max_word,max_n)

