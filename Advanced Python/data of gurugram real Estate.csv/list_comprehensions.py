#square the numbers using normal for loop method.

numbers = [1,2,3,4,5,6,7,8,9]
squared_number = []

for num in numbers:
    squared_number.append(num*num);

print(squared_number)

#square the numbers using list comprehension method

numbers = [1,2,3,4,5,6,7,8,9]
squared_number = [num * num for num in numbers]

print(squared_number);

#print only even numbers using list comprehension

numbers = [1,2,3,4,5,6,7,8,9,10];
even_numbers = [num for num in numbers if num%2==0];
print(even_numbers);

# Tranforming Text Data using walrus assignment operator in List Comprehension

names = [" Ali ", "Sara ", " JOHN"];
cleaned_data = [(n := name.strip().lower())[:1].upper() + n[1:] for name in names];
print(cleaned_data)

# Tranforming Text Data using capitalize in List Comprehension

names = [" Ali ", "Sara ", " JOHN"];
cleaned_data = [name.strip().lower().capitalize() for name in names];
print(cleaned_data)




