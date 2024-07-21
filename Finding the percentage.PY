n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average_score = sum(student_marks[query_name]) / len(student_marks[query_name])

print("{:.2f}".format(average_score))

#Input: 2
#       A 45 67 89
#       B 56 90 23


#Output: 56.33