'''
Operatori: aritmetici: +, -, *, /, % (aflarea restului impartirii)
de comparare: < > == != <= >=
logici: and, or (si, sau) ! (not)

'''

a = 3;
b = 5;

print(a+b) #3+5 => 8
print(a-b) #-2
print(a*b) #15
print(a/b) #0.6
print(a%b) #3

print(a==b) #a este egal cu b? False
print(a>b) #f
print(a<b) #t
print(a!=b) #t
print(a>=b) #f
print(a<=b) #t

print(a<b and a<4) #3<5 true 3<4 true => True
print(a<b or a<2) #true sau false => true

#print(a or b or (bunicu and bunica) daca vine doar mama ok, vine doar tata ok, vine doar bunicu notok, vine doar bunica not ok.
mama=False
tata=False
bunicu=True
bunica=True
print(mama or tata or (bunicu and bunica))