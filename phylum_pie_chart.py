import os, csv
import numpy as np
import matplotlib.pyplot as plt
import random
os.chdir('C:\\Users\\user\\Desktop\\analysis\\phylum_data')


def phylum_count(region):
    file = open('.\\' + region + '_phylum.csv', 'r')
    reader = csv.reader(file)
    recnik = {}

    for red in reader:
        if red[2] == 'Taxonomy':
            continue
        size = red[1]
        taxonomy = red[2].split(';')
        phylum =taxonomy[1]
        recnik[phylum] = int(size)

    return recnik

    file.close()

#Color generation of bacterial phylum
bacteria = []
color = []

def add_bacteria_and_color(legend):
    r = lambda: random.randint(0,255)
    for i in legend.get_texts():
        text = i.get_text().split('-')[0]
        if text not in bacteria:
            bacteria.append(text)
            color.append('#%02X%02X%02X' % (r(),r(),r()))

def generate_color_map(bacteria, color):
    output = {}
    for i in range(len(bacteria)):
        output[bacteria[i].rstrip()] = color[i]
    return output

data_dict = {'V1':{},
                'V2': {}, 
                'V3': {}, 
                'V4': {}, 
                'V5': {}, 
                'V6': {}, 
                'V7': {}, 
                'V8': {}
}

for i in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7','V8']:
     data_dict[i]= phylum_count(i)

color_map = {'Bacteria_unclassified': 'tab:blue', 'Firmicutes': 'tab:orange', 'Proteobacteria': 'tab:green', 'Bacteroidota': 'tab:red', 'Actinobacteriota': 'tab:purple', 'Campylobacterota': 'tab:cyan', 'Verrucomicrobiota': 'tomato', 'Patescibacteria': 'yellow', 'Synergistota': 'blueviolet', 'Planctomycetota': '#D4E6B1', 'Fusobacteriota': '#036673', 'Desulfobacterota': '#A673E2', 'Cyanobacteria': '#1DC84E', 'Spirochaetota': '#2D8741', 'Halanaerobiaeota': '#692311', 'Deinococcota': '#55254A', 'Gemmatimonadota': '#466F02', 'Myxococcota': '#1C75BB'}            

for vregion in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7','V8']:
    x_osa = []
    for i in data_dict[vregion].keys():
        i = i.rstrip('(100)')
        x_osa.append(i)
    x_osa =np.char.array(x_osa)
    y_osa = np.array(list(data_dict[vregion].values()))
 
    patches, texts = plt.pie(y_osa)
    labels = ['{0} - {1}'.format(i,j) for i,j in zip(x_osa, y_osa)]

    for i in range(len(patches)):
        patches[i].set_facecolor(color_map[x_osa[i]])

    sort_legend = True
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y_osa),  key=lambda x: x[2], reverse=True))
    
    plt.title(vregion + ' region', fontsize=24)
    legend = plt.legend(patches, labels, loc='best', bbox_to_anchor=(0, 1), fontsize=16)
    
    #uncomment for color generation
    #add_bacteria_and_color(legend)

    plt.figure()
    plt.show()

#uncomment to print color generation
#print(generate_color_map(bacteria, color))