# For each example below, predict what will be printed. Then, run the code and confirm your prediction.

a = 0
while a< 100:
	print a
"""
Prediction: I predict that it will print numbers that I less than 100.
Observation: After running this, it printed 0's many times and I had to stop it because after I saw the 'Too much output to process' comment, I stopped running it because at any moment my computer could've blown up and destroyed the classroom.
 """

a = 0
while a < 100:
	a = a + 1
	print a
"""
Prediction: I predict that it will print numbers that are less than 100 while adding 1 to the integer.
Observation: After running this code, I saw that it printed literally all the numbers that are less than 100. Also, it printed 100 because it's not less, but equal.
 """

a = raw_input("Would you like to quit: ")
while a != "y":
	a = raw_input("Would you like to quit: ")
"""
Prediction: I predict that it will first ask me the question and for the answer I put in, I will still get the same question.
Observation: I was right in some parts. I realized that the function has 'while a != 'y''. I answered the question with the word 'yes' which is why the question kept coming up. There is no 'else' in this function which is also another reason about why the computer kept asking me the question after I finished answering. Once I decided to answer with the letter 'y', the computer stopped printing the question. 
 """
