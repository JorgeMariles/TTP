#takes the dic, the order of cites, and a binary vector to see if an item is picked or not. returns the obj funcion val
def obj_func(dic,order_cities,item_pick):
    import numpy as np
    weight_ac_city=0
    value_ac_total=0
    node=np.array(dic["assigned node"])
    weight=np.array(dic['weight'])
    value_p=np.array(dic["profit"])
    item_pick=np.array(item_pick)
    last_city=1
    v_const=(dic["max speed"]-dic["min speed"])/dic["capacity of bag"]
    print(v_const)
    v_max=dic["max speed"]
    #distance de la primera city 
    point1p=dic['coords citites'][0]
    point2p=dic['coords citites'][order_cities[0]-1]
    
    point1=np.array((int(point1p[0]),int(point1p[1])))
    point2=np.array((int(point2p[0]),int(point2p[1])))
    distance=np.linalg.norm(point1 - point2)
    #because at this point w=0 the dividen is just vmax
    sum_part=(distance/(v_max))
    #print(sum_part,"sum part")

    for l in range(len(order_cities)):
        x=order_cities[l]
        #print(x,"x")
        items_node=list(zip(*np.where(node==x)))
        value_ac_city=0
        
        #items de la ciudad
        for o in items_node:   
            if ((weight_ac_city+(weight[o]*item_pick[o]))<=dic["capacity of bag"]):
                
                weight_ac_city=weight_ac_city+(weight[o]*item_pick[o])
                value_ac_city=value_ac_city+(value_p[o]*item_pick[o])
                #print(weight_ac_city,"wight total")
                #print(value_ac_city,"value of citie")
       #value and weight calculation
        value_ac_total=value_ac_total+value_ac_city

        distance
        if l <(len(order_cities)-1):

            point1p=dic['coords citites'][x-1]
            point2p=dic['coords citites'][(order_cities[l+1])-1]
            

        else:
            point1p=dic['coords citites'][x-1]
            point2p=dic['coords citites'][0]

        point1=np.array((int(point1p[0]),int(point1p[1])))
        point2=np.array((int(point2p[0]),int(point2p[1])))
        #print(point1,point2)

        distance=np.linalg.norm(point1 - point2)

        sum_part=sum_part+(distance/(v_max-(v_const*weight_ac_city)))
        #print(sum_part,"sum part")
    #print(value_ac_total,"value total")
    obj_func_val=value_ac_total-(dic["renting rate"]*sum_part)

    return obj_func_val