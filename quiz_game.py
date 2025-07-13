print("Welcome to my computer Quiz game!")

entry = input("Do you want to play? Yes/No : ")

if entry.lower() != "yes":
    quit()

count = 0

quiz = input("what does GPU stands for? ")
if quiz.lower() == "graphics processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

quiz = input("what does CPU stands for? ")
if quiz.lower() == "control processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

quiz = input("what does RAM stands for? ")
if quiz.lower() == "random access memory":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

quiz = input("what does ROM stands for? ")
if quiz.lower() == "read only memory":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")


quiz = input("what does GUI stands for? ")
if quiz.lower() == "graphical user interfce":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

print("you got " + str(count) + " questions correct!")
print("you got " + str((count / 5) * 100) + " %.")
