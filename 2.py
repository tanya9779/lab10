A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
F = A.difference(B)
G = C.difference(D)
H = D.difference(A)
J = B.difference(C)
E=(F.intersection(G)).union(H.intersection(J))
print (E)

