text = input("enetr a text")

if ("make a lot of money" in text):
    spam=True
elif("buy this" in text):
    spam=True
elif("subscribe this chinel" in text):
    spam=True
else:
    spam=False
if(spam):
    print("this text is spam ")
else:
    print("this text is not spam")