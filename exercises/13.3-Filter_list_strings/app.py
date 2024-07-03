names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia','Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail','Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia','Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria','Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']

# Your code here
def filter_str(nombre):
    for i in range(0,len(nombre)-1,1):
        if (nombre[i]+nombre[i+1])=='am' or (nombre[i]+nombre[i+1])=='Am':
            return True
    return False

new_list=list(filter(filter_str,names))
print(new_list)