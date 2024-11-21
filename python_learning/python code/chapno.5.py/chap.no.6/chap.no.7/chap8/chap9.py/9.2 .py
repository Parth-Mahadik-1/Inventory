def game():
    return 556

score=game()

with open("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\my.txt") as f:
    highscore=int(f.read())

if highscore<score:
    with open ("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\my.txt","w") as f:
        f.write(str(score)) 
    print 