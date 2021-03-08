def read_instance(file):
    
    problem_name=file.readline()[15:].strip()
    knapsack_data_type=file.readline()[20:].strip()
    dimension_cities=int(file.readline()[11:].strip())
    number_of_items=int(file.readline()[17:].strip())
    capacity_bag=float(file.readline()[22:].strip())
    min_speed=float(file.readline()[12:].strip())
    max_speed=float(file.readline()[12:].strip())
    renting_r=float(file.readline()[15:].strip())
    edge_weight_t=file.readline()[18:].strip()
    file.readline()
    index_cities=[]
    coords_cities=[]
    for x in range (int(dimension_cities)):
            line=file.readline()
            data = line.split()
            index_cities.append(data[0])
            coords_cities.append((data[1],data[2]))
    file.readline()
    index_items=[]
    profit=[]
    weight=[]
    assigned_node=[]
    for x in range (int(number_of_items)):
            line=file.readline()
            data = line.split()
            index_items.append(data[0])
            profit.append(float(data[1]))
            weight.append(float(data[2]))
            assigned_node.append(int(data[3]))
    dic={
        "problem name":problem_name,
        "knapsack data type":knapsack_data_type,
        "number cities":dimension_cities,
        "number of items":number_of_items,
        "capacity of bag":capacity_bag,
        "min speed":min_speed,
        "max speed":max_speed,
        "renting rate":renting_r,
        "edge weight type":edge_weight_t,
        "index citites":index_cities,
        "coords citites":coords_cities,
        "index items":index_items,
        "profit":profit,
        "weight":weight,
        "assigned node":assigned_node

    }
    #coords x,y
    return dic