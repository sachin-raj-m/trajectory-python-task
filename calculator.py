x=int(input("Enter 2 Numbers:"))
y=int(input())
op = input("Input an Operator from +,-,*,/\n")

if op=='+':
    print ("Sum =",(x+y))
elif op=='-':
    print ("Difference =",(x-y))
elif op=='*':
    print ("Product =",(x*y))
elif op=='/':
    print ("Quotient =",(x/y))