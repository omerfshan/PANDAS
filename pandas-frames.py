import pandas as pd

list=[["ahmet",50],["ali",60],["yağmur",30],["can",80]]
dict={"Name":["Ahmet","Ali","Yağmur","Can"],"Grade":[50,60,70,80]}
dict_list=[
    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"Yağmur","Grade":70},
    {"Name":"Can","Grade":80}
]

df=pd.DataFrame()
df=pd.DataFrame([1,2,3,4])
df=pd.DataFrame(dict)
df=pd.DataFrame(dict,index=["212","232","236","456"])
df=pd.DataFrame(dict_list)
df=pd.DataFrame(dict_list,index=["212","232","236","456"])
df=pd.DataFrame(list,index=[1,2,3,4],columns=["Name","Grade"])
print(df)

# s1=pd.Series([3,2,0,1])
# s2=pd.Series([0,3,7,2])
# data=dict(apples=s1,oranges=s2)
# df=pd.DataFrame(data)
