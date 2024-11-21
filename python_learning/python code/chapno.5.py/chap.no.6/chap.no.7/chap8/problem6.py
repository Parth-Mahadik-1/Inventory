
def remove(str,word):
    S = str.replace(word,"")
    return S.strip()
A = ("i am a parth i study data science")
P = remove(A,"parth")
print(P)


        
