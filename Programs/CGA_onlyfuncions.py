import numpy as np
import random
from random import randint

# Las funciones del algoritmo genetico celular comienzan aqui cambiadas para servir en el ttp


def crossover(fitness,population,d1,d2,mr,bina,fixa):
    #this function choses the best fitness of the neighbors and then convines both parents
    #if it is viable it will replace the individual being tested
    new_population=np.zeros(np.shape(population))
    assert new_population.shape == population.shape
    for k in range(np.shape(population)[0]): 
        for z in range(np.shape(population)[1]):
            parent_1=population[k,z,:].copy()
            #l5 neighbors
            l=np.array([fitness[k,(z-1)%d2],fitness[(k-1)%d1,z],fitness[k,(z+1)%d2],fitness[(k+1)%d1,z]]) 
            selector=np.random.choice(np.arange(4), size=2, replace=False)
            s_v=np.array([selector[0],selector[1]])
            fit=[l[selector[0]],l[selector[1]]]
            index=np.where(fit==np.max(fit))
            index=list(zip(*index))[0]
            winner=s_v[index]
            #print(parent_1,"parent1")
            if winner==0:
                parent_2=population[k,(z-1)%d2,:].copy()
            elif winner==1:    
                parent_2=population[(k-1)%d1,z,:].copy()
            elif winner==2:
                parent_2=population[k,(z+1)%d2,:].copy()
            elif winner==3:
                parent_2=population[(k+1)%d1,z,:].copy()                
            prepop=offspring_op(parent_2,parent_1,population)  
            #print(parent_1,parent_2,prepop)
            if fixa:
                prepop=fix_func(prepop)
            
            if bina:
                prepop=mutation_bin(prepop,mr)
            else:
                prepop=mutation_swap(prepop,mr)
            new_population[k,z,:]=prepop
    
            #print(new_population[k,z,:],"fianl")  
            #print("----------------------")              
    return new_population




def offspring_op(parent_2,parent_1,population):
    rnd=np.random.uniform(low=0, high=1)
    max_crosover =np.uint8(np.shape(population)[2])
    crossover_point=np.random.randint(low=1,high=max_crosover-1)
    if rnd >.5:
        offspring = parent_1[0:crossover_point]
        offspring = np.concatenate((offspring,parent_2[crossover_point:]),0)
    else:
        offspring = parent_2[0:crossover_point]
        offspring = np.concatenate((offspring,parent_1[crossover_point:]),0)    
    return offspring



def mutation_bin(population,mr): 
    if np.random.uniform(low=0, high=1)<=mr:
                #print(k,z,"mutation")
                # The random bin to be changed in the genome.
        random_number = np.random.randint(low=0, high=2)
        cromo = randint(0, np.shape(population)[0]-1)               
        gene=population.copy()               
        gene[cromo]=random_number              
        population=gene                                                     
    return population

def mutation_swap(population,mr): 
    if np.random.uniform(low=0, high=1)<=mr:
                #print(k,z,"mutation")
                # The random bin to be changed in the genome.
        cromo = randint(0, np.shape(population)[0]-1)    
        cromo2 = randint(0, np.shape(population)[0]-1) 
        gene=population.copy() 
        unop=gene[cromo]
        dosp=gene[cromo2]
        gene[cromo]=dosp
        gene[cromo2]=unop
        population=gene                                                     
    return population

def fix_func(pop):
    number=np.shape(pop)[0]
    #print(pop.shape)
    pop_list=list(pop)
    numb_cit=list(range(2,number+2))
    missing=[]
    duplicate=[]
    for x in numb_cit:
        if x not in pop:
            missing.append(x)
        if np.count_nonzero(pop == x )>1 :
            duplicate.append(x)
    #print(x)
    new_list=[]
    count=0
    for l in (duplicate):
        #print(l)
        where=list(zip(*np.where(pop==l)))
        #print(where)
        sub=np.random.randint(low=0, high=2)
        #print(sub)
        substitute=where[sub]
        pop[substitute]=missing[count]
        count=count+1
    return pop

# Las funciones del algoritmo genetico celular terminan aqui