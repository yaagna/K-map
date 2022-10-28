
#This program is used to minimize logical expression using Quine Mccluskey algorithm


#for 2 input Kmap
def Kmap2(mt, nip):
    for i in range(50):
        print("-", end="")
    print()
    prnt = input("Enter Variables eg. (A B):").split(" ")
    for i in range(len(mt)):
        mt[i] = '0b'+ bin(mt[i])[2:].lstrip('0')
    op=''
    ans=[[0,0],[0,0]]
    ansmx = [[0,0],[0,0]]
    flag = 0
    temp = []

    for i in range(2):
        for j in range(2):
            p = '0b'+ (bin(i)[2:]+bin(j)[2:]).lstrip('0')
            if p in mt:
                ans[i][j] = 1
    
    for i in range(50):
        print("-", end="")
    print()
    print("K-map done")
    if nip==1:
        for i in range(2):
            for j in range(2):
                if ans[i][j] == 1:
                    ansmx[i][j] = 0 
            
        
