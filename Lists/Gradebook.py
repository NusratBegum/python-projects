"""
1.

"""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics","calculus","poetry","history"]
print(subjects)
grades =[98,97,85,88]

print([subjects] +[grades])

gradebook = [["physics",98],["calculus",97],["poetry",85],["history",88]]

gradebook.append(["computer science",100])
gradebook.append(["visual arts", 93])
gradebook[-1] =[ "visual arts",98]
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)


full_gradebook = last_semester_gradebook + [gradebook]
print(full_gradebook)
