import csv
import os
import json

os.chdir('C:\\Users\\user\\Desktop\\analysis\\names_accnos')

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Finding removed seqs - unkownTaxa
# 
def grouping_taxAccnos (number):
    file_V_names = open('.\\namesV' + str(number) + '.csv', 'r')
    taxonomyV = open('.\\taxonomyV' + str(number) + '.csv', 'r')
    if number != 4:
        aligned = open('.\\align_accnosV' + str(number) + '.csv', 'r')


    reader1 = list(csv.reader(file_V_names))
    reader2 = list(csv.reader(taxonomyV))
    if number == 4:
        reader3 = []
    else:
        reader3 = list(csv.reader(aligned))

    sanity = 0
    for i in reader2:
        ime = i[0]
        takson = i[1].split(';')
        if takson[0] == 'unknown':
            for j in reader1:
                temp = j[1].split(",")
                if ime == j[0]:
                    sanity += 1
                    unknown_taxon['V' + str(number)].extend(temp)


    if number != 4:

        for i in reader3:
            ime = i[0]
            for j in reader1:
                temp = j[1].split(",")
                if ime == j[0]:
                    not_aligned['V' + str(number)].extend(temp)

 
    file_V_names.close()
    taxonomyV.close()
    if number != 4:
        aligned.close()

def extending (unique): 
    counter = 0
    for niz in unique:
        counter += 1
        file_V_names = open('.\\namesV' + str(counter) + '.csv', 'r')
        reader =list (csv.reader(file_V_names))
        for j in reader:
            imena = j[1].split(",")
            for k in niz:
                if k == imena[0]:
                    niz.extend(imena[1:])
        file_V_names.close()
    return (unique)                
    

def unknownUncultured (x):
    k = []
    l =[]
    for i in uncultured_bact['uncultured bacterium']:
        for j in unknown_taxon['V'+x]:
            if i == j:
                unknown_uncult['V'+x]['size'] += 1
                k.append(j)
                unknown_uncult['V'+x]['data'] = k
    if x != '4':
        for i in uncultured_bact['uncultured bacterium']:
            for j in not_aligned['V'+x]:
                if i == j:
                    uncult_notAligned ['V'+x]['size'] += 1
                    l.append(j)
                    uncult_notAligned ['V'+x]['data'] = l

#--------------------------------------------------------------------------------------------------------------------------------------------------

mothur_unclassifid = open('C:\\Users\\user\\Desktop\\analysis\\Unclassified_phylum.csv', 'r')
final_reff = open('C:\\Users\\user\\Desktop\\analysis\\FINALphylo.csv', 'r')
output_file = open('C:\\Users\\user\\Desktop\\analysis\\Classification.json', 'w')

first_reader = csv.reader(final_reff)
second_reader = csv.reader(mothur_unclassifid)

# Dicts of all unknowns (mothur: uniqe + group)
unknown_taxon = {'V1':[], 'V2': [], 'V3': [], 'V4': [], 'V5': [], 'V6': [], 'V7' : [], 'V8': []}
not_aligned = {'V1':[], 'V2': [], 'V3': [], 'V4': [], 'V5': [], 'V6': [], 'V7' : [], 'V8': []}
uncultured_bact = {'size' : 0, 'uncultured bacterium' : []}

for i in range (1,9):
    grouping_taxAccnos(i)

print(len(not_aligned['V1']))
print(len(not_aligned['V2']))
print(len(not_aligned['V3']))
print(len(not_aligned['V5']))
print(len(not_aligned['V6']))
print(len(not_aligned['V7']))
print(len(not_aligned['V8']))

lista  = []
for red in first_reader:
    name = red[0]
    final_name = red[2]
    if final_name == 'uncultured bacterium':
        uncultured_bact['size'] += 1
        lista.append(name)

uncultured_bact['uncultured bacterium'] = lista

# Info about V-regions for unknown and uncultured:
unknown_uncult = {'V1':{'size': 0, 'data':[]},
                'V2': {'size': 0, 'data':[]}, 
                'V3': {'size': 0, 'data':[]}, 
                'V4': {'size': 0, 'data':[]}, 
                'V5': {'size': 0, 'data':[]}, 
                'V6': {'size': 0, 'data':[]}, 
                'V7': {'size': 0, 'data':[]}, 
                'V8': {'size': 0, 'data':[]}
                }
uncult_notAligned = {'V1':{'size': 0, 'data':[]},
                'V2': {'size': 0, 'data':[]}, 
                'V3': {'size': 0, 'data':[]}, 
                'V4': {'size': 0, 'data':[]}, 
                'V5': {'size': 0, 'data':[]}, 
                'V6': {'size': 0, 'data':[]}, 
                'V7': {'size': 0, 'data':[]}, 
                'V8': {'size': 0, 'data':[]}
                }

for i in range (1,9):
    unknownUncultured(str(i))     



#Info about V-regions for uncultured and unclassified:
uncult_unclassif = {'V1':{'size': 0, 'data':[]},
                'V2': {'size': 0, 'data':[]}, 
                'V3': {'size': 0, 'data':[]}, 
                'V4': {'size': 0, 'data':[]}, 
                'V5': {'size': 0, 'data':[]}, 
                'V6': {'size': 0, 'data':[]}, 
                'V7': {'size': 0, 'data':[]}, 
                'V8': {'size': 0, 'data':[]}
                }

unclassif = {'V1':[], 'V2': [], 'V3': [], 'V4': [], 'V5': [], 'V6': [], 'V7' : [], 'V8': []}

# Writing to lists from csv file  
niz1 = []
niz2 = []
niz3 = []
niz4 = []
niz5 = []
niz6 = []
niz7 = []
niz8 = []

brojac = 0
i = [niz1, niz2, niz3, niz4, niz5, niz6, niz7, niz8]
for V in second_reader:
    niz = V[1].split(',')
    i[brojac].extend(niz)


    brojac +=1

novi_niz = [niz1, niz2, niz3, niz4, niz5, niz6, niz7, niz8]
n = extending(novi_niz)

brojac = 1
for i in n:
    new_list = set(i).intersection(uncultured_bact['uncultured bacterium'])
    uncult_unclassif['V' + str(brojac)]['data'] += list(new_list)
    uncult_unclassif['V' + str(brojac)]['size'] += len(list(new_list))

    newer_list = set(i).difference(uncultured_bact['uncultured bacterium'])
    unclassif['V'+str(brojac)].append(list(newer_list))

    brojac += 1

output = {'Sekvence_koje_se_odnose_na_neklasifikovane_i_nekultivisane_bakterije' : {}, #uncult_unclasif
        'Presek_sekvenci_koje_su_nekultivisane_i_nepoznatog_taksona': {}, # unknown_uncult
        'Sekvence_koje_su_neklasifikovane_ali_ne_pripadaju_nekultivisanoj_grupi' : {},  # unclasiff 
        'Not_aligned_uncultured' : {}, # uncult_notAlign
        'Nekultivisane_bakterije_podaci' : {} }#uncultured_bact dict 

output['Sekvence_koje_se_odnose_na_neklasifikovane_i_nekultivisane_bakterije'] = uncult_unclassif
output['Sekvence_koje_su_neklasifikovane_ali_ne_pripadaju_nekultivisanoj_grupi'] = unclassif
output['Presek_sekvenci_koje_su_nekultivisane_i_nepoznatog_taksona'] = unknown_uncult
output['Nekultivisane_bakterije_podaci'] = uncultured_bact
output['Not_aligned_uncultured'] = uncult_notAligned

file = json.dumps(output, indent=4)
output_file.write(file)

output_file.close()
mothur_unclassifid.close()
final_reff.close()
