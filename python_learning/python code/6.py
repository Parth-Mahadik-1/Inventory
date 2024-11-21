# data frame 5x8
import pandas as pd
dict={
    "product":["scale","sharpner","eraser","pencil","pen"],
    "price":[10,5,2,10,15],
    "quality":["doms","apsara","xyz","abc","mno"],
    "company":["tata","relains","adani","spacex","microsoft"],
    "mfg_date":["20/19","24/19","13/19","2/20","31/22"],
    "branch":["chennai","mumbai","kolkata","panjab","delhi"],
    "pinocde":[111,23212,223433,12233,12],
    "city":["virar","nalasopara","vasai","naigav","bhaindar"],
    "actor":["mukesh ambani","adani","salaman khan","sharukh khan","virat kholi"]
}
a=pd.DataFrame(dict)
print(a)






        
