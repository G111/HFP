scores = []

result_f = open("C:/Users/TCIAKCIVAN/Desktop/results.txt")

for line in result_f:
    (names, score) = line.split()
    scores.append(float(score))

result_f.close()

print(scores[0])
print((scores[1]))
print(scores[2])