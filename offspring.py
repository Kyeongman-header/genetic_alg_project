import random
from consts import *

def mutation(gene):
    mutate_number=0
    for n in range(len(gene)):
        prob_mut=random.random()
        if prob_mut>0.999: # 0.1%의 확률로, gene의 염기 서열은 돌연변이가 일어난다.
            if prob_mut>0.9995:
                gene[n]=random.choice(nucleobase)
            else:
                changer=random.choice(range(0,len(gene)))
                temp=gene[changer]
                gene[changer]=gene[n]
                gene[n]=temp
            mutate_number+=1
    return gene,mutate_number

def make_offsprings(num_offsprings,results):
    roulette=[]
    whole_score=0
    for result in results:
        score=result['time_survive']-result['score']
        whole_score+=score
        roulette.append(score)
    
    roulette=[val / whole_score for val in roulette] # roulette : f/sum(f)
    # random하게 부모를 선택할 때 weight이 된다.
    # print(roulette)

    genes=[g['gene'] for g in results]
    offsprings=[]
    for n in range(num_offsprings):
        while True:
            gene_father=random.choices(genes, weights = roulette)[0]
            gene_mother=random.choices(genes,weights=roulette)[0]
            if gene_father!=gene_mother:
                break
        random_division_point=random.choice(range(1,gene_length)) # Cross Over 방식으로 유전자를 섞는다.
        crossover=gene_father[:random_division_point] + gene_mother[random_division_point:]
        mutation_gene,mutate_number=mutation(crossover) # cross over로 섞은 다음, local optimum에 갇히는 것을 막기 위해 mutation이 일어난다.
        offsprings.append(mutation_gene) # offspring gene 생성.

    print("avg mutation numbers : " + str(mutate_number/num_offsprings))
    # print(offsprings)
    return offsprings