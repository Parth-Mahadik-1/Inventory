def openfile(filename):
    try:
      with open(filename,"r") as f:
        print(f.read())
    except FileNotFoundError:
       print("file is not exist ")

openfile("f1.txt")   
openfile("f2.txt")
openfile("f3.txt")