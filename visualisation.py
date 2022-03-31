import numpy as np
import matplotlib.pyplot as plt
import json
import os

os.getdir()
os.chdir('C:\\Users\\user\\Desktop\\analysis')

with open('.\\Data_for_Visualisation\\V1.json') as v1:
    v1_dict = json.load(v1)

with open('.\\Data_for_Visualisation\\V2.json') as v2:
    v2_dict = json.load(v2)

with open('.\\Data_for_Visualisation\\V3.json') as v3:
    v3_dict = json.load(v3)

with open('.\\Data_for_Visualisation\\V4.json') as v4:
    v4_dict = json.load(v4)

with open('.\\Data_for_Visualisation\\V5.json') as v5:
    v5_dict = json.load(v5)

with open('.\\Data_for_Visualisation\\V6.json') as v6:
    v6_dict = json.load(v6)

with open('.\\Data_for_Visualisation\\V7.json') as v7:
    v7_dict = json.load(v7)

with open('.\\Data_for_Visualisation\\V8.json') as v8:
    v8_dict = json.load(v8)

phylum = [v1_dict['phylum']['classif'],v2_dict['phylum']['classif'], v3_dict['phylum']['classif'], v4_dict['phylum']['classif'],v5_dict['phylum']['classif'], v6_dict['phylum']['classif'],v7_dict['phylum']['classif'],v8_dict['phylum']['classif'], 2527]
clazz = [v1_dict['class']['classif'],v2_dict['class']['classif'], v3_dict['class']['classif'], v4_dict['class']['classif'],v5_dict['class']['classif'], v6_dict['class']['classif'],v7_dict['class']['classif'],v8_dict['class']['classif'], 2527]
order = [v1_dict['order']['classif'],v2_dict['order']['classif'], v3_dict['order']['classif'], v4_dict['order']['classif'],v5_dict['order']['classif'], v6_dict['order']['classif'],v7_dict['order']['classif'],v8_dict['order']['classif'], 2527]
family = [v1_dict['family']['classif'],v2_dict['family']['classif'], v3_dict['family']['classif'], v4_dict['family']['classif'],v5_dict['family']['classif'], v6_dict['family']['classif'],v7_dict['family']['classif'],v8_dict['family']['classif'], 2527]
genus = [v1_dict['genus']['classif'],v2_dict['genus']['classif'], v3_dict['genus']['classif'], v4_dict['genus']['classif'],v5_dict['genus']['classif'], v6_dict['genus']['classif'],v7_dict['genus']['classif'],v8_dict['genus']['classif'], 2527]

n = 9
r = np.arange(n)
width = 0.15

plt.bar(r-2*width, phylum, color = 'royalblue',
        width = width, edgecolor = 'k',
        label='tip')
plt.bar(r - width, clazz, color = 'palegreen',
        width = width, edgecolor = 'k',
        label='klasa')
plt.bar(r, order, color = 'tomato',
        width = width, edgecolor = 'k',
        label='red')
plt.bar(r + width, family, color = 'orchid',
        width = width, edgecolor = 'k',
        label='porodica') 
plt.bar(r + 2*width , genus, color = 'gold',
        width = width, edgecolor = 'k',
        label='rod') 
    
plt.xlabel("Hipervarijabilni region", fontsize = 'large',  fontweight = 'bold')
plt.ylabel("Broj sekvenci",  fontsize = 'large', fontweight = 'bold')
plt.title('Broj oporavljenih sekvenci nakon klasifikacije mothur alatom:', fontsize = 'large')
  
plt.xticks(r + width/2,['V1','V2','V3','V4','V5','V6','V7', 'V8', 'Referentni podaci'])
plt.legend()
plt.show()

