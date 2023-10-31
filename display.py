import pickle
from consts import *
from one_generation import *
from offspring import *
import matplotlib.pyplot as plt
import sys

filename=sys.argv[1]
last_n_samples=int(sys.argv[2])

with open("best_genes_" + filename, "rb") as fp:   # Unpickling
    best_genes = pickle.load(fp)
with open("avgs_array_" + filename, "rb") as fp:   # Unpickling
    avgs = pickle.load(fp)
with open("max_array_" + filename, "rb") as fp:   # Unpickling
    maxes = pickle.load(fp)

print(avgs)
print(maxes)

whole_len=len(best_genes)
best_genes=best_genes[-last_n_samples:]
# print(best_genes)
one_generation(whole_len-last_n_samples,canvas,len(best_genes),is_Test=True,best_gene=best_genes)
# for g,best_gene in enumerate(best_genes):
#     one_generation(g,canvas,1,is_Test=True,best_gene=best_gene)
plt.plot(avgs,label='avg')
plt.plot(maxes,label='max')
plt.legend()
plt.show()
plt.close()