#main
from Kmap import Kmap2
from Kmap import Kmap3
from Kmap import Kmap4

ask='y'
while ask=='y':
    for _ in range(50):print("-",end='')
    print()
    nfinp=int(input("Enter no of Inputs(2,3,4) : "))
    mimastr=input("Enter 'SOP' for SOP(Minterms) or 'POS' for POS(Maxterms) : ").lower()
    if mimastr=='pos':
        mima=2
    elif mimastr=='sop':
        mima=1
    if mima==1:
        mt=list(map(int,input("Enter Minterms : ").split()))
    else:
        mt=list(map(int,input("Enter Maxterms : ").split()))
    if nfinp==2:
        Kmap2(mt,mima)
    elif nfinp==3:
        Kmap3(mt,mima)
    elif nfinp==4:
        Kmap4(mt,mima)
    else:
        print("You committed some mistake, please check the inputs next time.")
    ask=input("Enter 'y' for another K-Map or 'n' to exit : ").lower()
    for i in range(25):print("--",end='')
    print()