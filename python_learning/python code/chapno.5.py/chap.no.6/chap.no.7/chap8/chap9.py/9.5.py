a = [ "donkey", "chu", "stupid","mad"]

with open("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\my.txt","r") as f:
    p=f.read()
    for i in a :
     p = p.replace( i ,"@!##$$!")
    

    with open("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\my.txt","w") as f:
          f.write(p)

 