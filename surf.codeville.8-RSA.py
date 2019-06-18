line = "101;Jhonny 'wave-boy' Jones;USA;8.32;Fish;21"

s = {}

(s['id'],s['name'],s['country'],s['average'],s['board'],s['age']) = line.split(";")

print("ID:          " + s['id'])
print("Name:        " + s['name'])
print("Country:     " + s['country'])
print("Average:     " + s['average'])
print("Board Type:  " + s['board'])
print("Age:         " + s['age'])