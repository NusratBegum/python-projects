"""
1. Create a list called subjects and fill it with the classes you are taking:

"physics"
"calculus"
"poetry"
"history"

2.Create a list called grades and fill it with your scores:
98
97
85
88

3. Manually (without any methods) create a two-dimensional list to combine subjects and grades.Assign the value into a variable called gradebook.Then,Print gradebook.

5.Your grade for your computer science class just came in! You got a perfect score, 100!By using list method we made two dimensional list of gradebook.

6. we are rewarding an extra 5 points for our visual arts class.Access the index of the grade for your visual arts class and modify it to be 5 points greater.

7.Decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.Find the grade value in your gradebook for the poetry class.

8. Now, added a new "Pass" value to the sublist where your poetry class is located.

9.You also have your grades from last semester, stored in last_semester_gradebook.Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook.then print full_gradebook to see the completed list.

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
