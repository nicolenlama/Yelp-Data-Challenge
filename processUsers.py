# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:25:09 2019

@author: nlama
"""
from __future__ import print_function
import json
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import unicodecsv as csv

file = "D:/Documents2/YelpDataSetChallenge/user.json"
print("Reading in data from JSON file...")
data = list()
with open(file, encoding="utf8") as f:
    for line in f:
        data.append(json.loads(line))

print("Calculating all elite years represented in the data...")
all_elite_years = []
for row in data:
    if row['elite']:
        all_elite_years += row['elite']
all_elite_years = sorted(list(set(all_elite_years)))

print("Processing data...")
new_data = list()
for row in data:
    new_row = {}
    for k, v in row.items():
        if k not in ['elite', 'friends']:
            new_row[k] = v
        else:
            if k == 'elite' and row['elite']:
                for year in all_elite_years:
                    new_row['elite_' + year] = (year in row['elite'])
            elif k == 'friends' and row['friends']:
                new_row['friends'] = len(row['friends'])
    new_data.append(new_row)

print("Writing processed data to CSV...")
with open('yelp_academic_dataset_user.csv', 'wb') as f:
    fieldnames = sorted(new_data[0].keys())
    dw = csv.DictWriter(f, fieldnames=fieldnames, encoding='UTF-8')
    dw.writeheader()
    dw.writerows(new_data)
#
#
#G.add_nodes_from(pos.keys())
#for n, p in pos.items():
#   G.node[n]['pos'] = p
#
#
#nx.draw(G, pos=pos, with_labels=True, font_size=8, node_size=5)
#plt.show()
#G = nx.Graph()