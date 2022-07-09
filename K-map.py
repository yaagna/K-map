#This program is used to minimize logical expression using Quine Mccluskey algorithm

#multiply 2 minterms
def minterm_multiply(x,y):
    res = []
    for i in x:
        if i+"'" in y or (len(i)==2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            return []
        else:
            res.append(i)
    return res
    
