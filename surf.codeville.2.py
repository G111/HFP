highest_score = 0

result_f = open("C:/Users/TCIAKCIVAN/Desktop/results.txt")

for line in result_f:
    (name, score) = line.split()
    print(score)
    if float(score) > highest_score:
        highest_score = float(score)


result_f.close()
print("The highest score was:")
print(highest_score)