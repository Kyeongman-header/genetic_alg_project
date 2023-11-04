

import time
import random
import numpy as np
from consts import *
from one_generation import *
from offspring import *
from tqdm import trange, tqdm
import pickle

filename=sys.argv[1]
avgs=[]
maxes=[]
best_genes=[]
next_genes=[]
for g in trange(whole_generations):
    results=one_generation(g,canvas,whole_individuals,is_Test=False,best_gene=next_genes)
    results=sorted(results,key=(lambda x: x['time_survive']-x['score']),reverse=True)
    scores=[g['time_survive']-g['score'] for g in results]
    # print("scores : ")
    # print(scores)
    scores=np.array(scores)
    avg=np.mean(scores)
    max=np.max(scores)
    print("Avg : ")
    print(avg)
    print("Max : ")
    print(max)
    avgs.append(avg)
    maxes.append(max)
    best_gene=results[0]['gene']
    best_genes.append(best_gene)
    next_genes=make_offsprings(whole_individuals,results,)
    # input()
    # print(results)
    with open("best_genes_" + filename, "wb") as fp:   #Pickling
        pickle.dump(best_genes, fp)
    with open("avgs_array_" + filename, "wb") as fp:   #Pickling
        pickle.dump(avgs, fp)
    with open("max_array_" + filename, "wb") as fp:   #Pickling
        pickle.dump(maxes, fp)


with open("best_genes_" + filename, "wb") as fp:   #Pickling
    pickle.dump(best_genes, fp)
with open("avgs_array_" + filename, "wb") as fp:   #Pickling
    pickle.dump(avgs, fp)
with open("max_array_" + filename, "wb") as fp:   #Pickling
    pickle.dump(maxes, fp)


# w indow.mainloop()
#

