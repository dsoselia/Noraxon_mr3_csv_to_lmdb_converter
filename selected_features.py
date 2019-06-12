# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 03:32:39 2018

@author: Dati
"""
import numpy as np
def get_labels(path = 'labels.csv'):
    with open(path) as csv:
        content = csv.readlines()[0].lower()
        content  = content.replace('","', "TARA")
        content  = content.replace(',', " ")
        content  = content.replace('"', " ")
        content  = content.replace('\n', " ")
        content  = content.replace('TARA', " , ")
        content = content.split(",")
        return content
    
def get_indexes (term = 'shank rt', direction = 'rt'):
    term = term.split(' ')
    direction = term[1]
    term = term[0]
    labels = get_labels()
    #return[3]
    return [b for b in range(len(labels)) if (term in labels[b] and direction in labels[b])]

def select_features(matrix, term = 'shank rt' ):
    return matrix[:, get_indexes(term = term)]

def select_features_list():
    [[ line[i] for i in range(len(line)) if i in b ] for line in a]