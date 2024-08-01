score = 0
def questionsmachine(question, option1, option2, option3, option4):
    a = f"""
{question}
****************************************

1.{option1}          2.{option2}
3.{option3}          4.{option4}

****************************************
Give Your Answer By 1,2,3,4: 
"""
    return a
answer1 = int(input(questionsmachine("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome")))
if answer1 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer2 = int(input(questionsmachine("Who wrote the play \"Romeo and Juliet\"?", "Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy")))
if answer2 == 2:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer3 = int(input(questionsmachine("Which planet is known as the Red Planet?", "Earth", "Jupiter", "Mars", "Venus")))
if answer3 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer4 = int(input(questionsmachine("What is the largest mammal in the world?", "Elephant", "Giraffe", "Blue Whale", "Hippopotamus")))
if answer4 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer5 = int(input(questionsmachine("Who was the first President of the United States?", "Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams")))
if answer5 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

# Additional 10 questions
answer6 = int(input(questionsmachine("Which element has the chemical symbol 'O'?", "Gold", "Hydrogen", "Oxygen", "Carbon")))
if answer6 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer7 = int(input(questionsmachine("Which is the smallest prime number?", "1", "0", "2", "3")))
if answer7 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer8 = int(input(questionsmachine("Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean")))
if answer8 == 4:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer9 = int(input(questionsmachine("In which year did World War II end?", "1945", "1939", "1918", "1963")))
if answer9 == 1:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer10 = int(input(questionsmachine("Which country is known as the Land of the Rising Sun?", "China", "India", "Japan", "Thailand")))
if answer10 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer11 = int(input(questionsmachine("What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum")))
if answer11 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer12 = int(input(questionsmachine("Which is the longest river in the world?", "Nile", "Amazon", "Yangtze", "Mississippi")))
if answer12 == 2:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer13 = int(input(questionsmachine("What is the chemical symbol for water?", "H2O", "CO2", "O2", "NaCl")))
if answer13 == 1:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer14 = int(input(questionsmachine("Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo")))
if answer14 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer15 = int(input(questionsmachine("Which country hosted the 2016 Summer Olympics?", "China", "Brazil", "United Kingdom", "Greece")))
if answer15 == 2:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer16 = int(input(questionsmachine("What is the most abundant gas in Earth's atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Helium")))
if answer16 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer17 = int(input(questionsmachine("Which animal is known as the King of the Jungle?", "Tiger", "Elephant", "Lion", "Cheetah")))
if answer17 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer18 = int(input(questionsmachine("Who discovered penicillin?", "Alexander Fleming", "Marie Curie", "Isaac Newton", "Albert Einstein")))
if answer18 == 1:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer19 = int(input(questionsmachine("Which continent is the largest by land area?", "Africa", "Asia", "North America", "Europe")))
if answer19 == 2:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

answer20 = int(input(questionsmachine("How many continents are there on Earth?", "5", "6", "7", "8")))
if answer20 == 3:
    print("Congrats! Correct Answer!")
    score += 1
else:
    print("Nope! Not Correct Answer.")

if(score == 15):
    print("You are a genius Bro! U Got All 15 Right!")
elif(score < 15 and 10 > score):
    print("Not That Bad You Got", score, "Out of 15")
elif(score < 10 and 5 > score):
    print("Not the Worst But Bro U Have To Study More! Cause U Got", score, "Out Of 15")
elif(score < 5 and 0 > score):
    print("U Are Dumb! Cause U Got", score, "Out Of 15")