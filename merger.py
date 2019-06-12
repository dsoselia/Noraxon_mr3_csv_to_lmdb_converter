import os
from glob import glob
import lmdb
#current directory
top = os.getcwd() + '/CSV_fall_data/**/*.csv'

#takes path to csv, returns csv as string stripped of the metadata
def strip(path):
    end = False
    start= False
    with open(path) as csv:
        content = csv.readlines()
    stripped = ""
    i = 0
    last = ""
    falling = False
    for row in content:
        if (i==4):
            if ('Marker' not in row):
                end = True
            if ('Switch' in row):
                start = True
        if (i > 5):
            new_row = row
            if (end):
                new_row = new_row[:-1]+',0,\n'
            elif ('all' in new_row):
                falling = ~falling
            new_row = new_row.split(',')
            if(start):
                new_row = new_row[3:]
            else:
                new_row = new_row[1:]
            if falling:
                new_row[-2] = '1'
            new_row = ','.join(new_row)
            last = new_row
            stripped += new_row
        i+=1
        if (i%1000 == 1):
            print(i)
            pass
    print(path + str(len(last.split(','))))
    return stripped



#takes path with CSV files parent folder, merges into single CSV file. As default searches in current directory and outputs to merged.csv
def merge(path = os.getcwd() + '/CSV_fall_data/**/*.csv', mergedPath = 'merged.csv'):
    csvs = glob(top)
    merged = ""
    for csv in csvs:
        merged += strip(csv) + '\n'
        #break #FIXME remove break
    open(mergedPath, 'w').write(merged)
#merge()
import os
def printRow(path = os.getcwd() + '/CSV_fall_data/**/*.csv', n = 4):
    csvs = glob(top)
    merged = []
    for csv in csvs:
        with open(csv) as csv:
            content = csv.readlines()
        merged.append(content[n])
    return merged
a = printRow(n=500)



def save_to_lmdb(X_t, Y_t, filename = "converted.dbq"):
    lmdb_env = lmdb.open(filename, map_size=int(1e9))
    
    
    
    for i in range(X_t.shape[0]):
        with lmdb_env.begin(write=True) as lmdb_txn:
            lmdb_txn.put(('X_t_'+str(i)).encode(), X_t[i])
            lmdb_txn.put(('Y_t_'+str(i)).encode(), Y_t[i])
    