import pandas as pd
c=pd.read_csv("filtered_stars.csv")
c.head()
name = c["Star_name"].to_list()
mass = c["Mass"].to_list()
radius = c["Radius"].to_list()
dist = c["Distance"].to_list()
gravity = c["Gravity"].to_list()
final_star_list = []

temp_dict ={}
for i in range(0,len(name)):
    temp_dict["name"]=name[i]
    temp_dict["mass"]=mass[i]
    temp_dict["radius"]=radius[i]
    temp_dict["distance"]=dist[i]
    temp_dict["gravity"]= gravity[i]
    final_star_list.append(temp_dict)
    temp_dict ={}
print(final_star_list)
