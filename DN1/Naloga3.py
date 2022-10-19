x= input('Vnesi prvo stevilo ')
y= input('Vnesi drugo stevilo ')
z= input('Vnesi tretje stevilo ')
print(x,type(x),y,type(y),z,type(z))

if y == x:
    print('Druga vrednost je enaka prvi')
else:
    print('Druga vrednost ni enaka prvi')

if z <= x:
    print('Tretja vrednost je manjša ali enaka prvi')
else:
    print('Tretja vrednost je večja kot prva')
