import random;
import time;

#This is a set of pre text.
PRE_TEXT = [
    "Python is a powerful programming language",
    "Practice makes your typing speed faster",
    "Consistency is more important than perfection",
]

#Chossing random text for typing.
target_text = random.choice(PRE_TEXT)

# Interacting with the user for his input
print(target_text)
print("\nYour time starts now!")\

# Getting start time
start_time = time.time();
USER_TEXT = input("\n")

# Getting end time
end_time = time.time();

# Calculating WPM

# WPM = (len(USER_TEXT.split()) / ((end_time - start_time) / 60))
target_text_words = target_text.split()
TARGET_LENGTH_IN_WORDS = len(target_text_words)
USER_TEXT_WORDS = USER_TEXT.split()

correct_words=0
for i in range(min(TARGET_LENGTH_IN_WORDS, len(USER_TEXT_WORDS))):
        if (target_text_words[i] == USER_TEXT_WORDS[i]):

          correct_words +=1;
WPM = (correct_words) / ((end_time - start_time) / 60)
print(correct_words)

# Calculating accuracy
TARGET_LENGTH_IN_LETTERS = len(target_text)
correct_letters=0
for i in range(min(TARGET_LENGTH_IN_LETTERS, len(USER_TEXT))):
        if (target_text[i] == USER_TEXT[i]):

          correct_letters +=1;
accuracy_percentage = (correct_letters/TARGET_LENGTH_IN_LETTERS) * 100

#Displaying the output
print("Your speed!",WPM)
print("Your accuracy", accuracy_percentage)
