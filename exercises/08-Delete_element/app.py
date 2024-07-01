people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    updated_people = []
    for i in people:
        if i==person_name:
            updated_people=updated_people
        else:
            updated_people.append(i)
    
    
    return updated_people

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
