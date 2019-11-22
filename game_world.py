
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[]]


def add_object(o, layer):
    objects[layer].append(o)


<<<<<<< HEAD
def add_objects(l, layer):
    objects[layer] += l


=======
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8
def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


<<<<<<< HEAD


=======
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8
def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()

def destroy():
    clear()
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

