scores = []
names = []

result_f = open("C:/Users/TCIAKCIVAN/Desktop/results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
    names.append(name)

result_f.close()

scores.sort(reverse=True)
names.sort(reverse=True)

# ...or
# scores.sort()
# scores.reverse()

print("The highest score were:")
print(names[0] + " with " + str(scores[0]))
print((names[1] + " with " + str(scores[1])))
print(names[2] + " with " + str(scores[2]))

# This code gives wrong name & score list
# The highest score were:
# Zack with 9.12
# Stacey with 8.65
# Juan with 8.45