# Ruben
# 1
def financialCrisis(roadRegister):
    return_val = []
    for i in range(len(roadRegister)):
        zipp = list(zip(*roadRegister))
        zipp.pop(i)
        for j in range(len(zipp)):
            zipp[j] = list(zipp[j])
            zipp[j].pop(i)
        return_val.append(list(zip(*zipp)))
    return return_val


# 2
def namingRoads(roads):
    names = dict()
    for i in range(len(roads)):
        names[roads[i][-1]] = set(roads[i][:-1])
    for i in range(1,len(names)):
        if len(names[i-1].union(names[i])) <= 3:
            return False
    return True