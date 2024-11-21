import pandas as pd
data={
    "id":[2618,2637,2691,2696,2695,2699,2919,2917,2623,2652],
    "Name":["Parth","Yogesh","Naiogav","pradyum","Sahil","Sanvi","viraj","sunny","catholith","chinmay"],
    "Course":["Ds","IT","MOVIE","MOYE","DS","Ds","IT","CS","Ds","DS"],
    "subject":["python","C","C++","MOye","FOs","OPP","DBMS","PYHTON","chiken","Python"]
}
a=pd.DataFrame(data)
print(a)