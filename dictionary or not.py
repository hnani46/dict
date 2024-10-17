......
 The program takes a dictionary and checks if a given key exists in a dictionary or not. 
Problem Solution:
1. Declare and initialize a dictionary to have some key-value pairs.{'A':1,'B':2,'C':3}
2. Take a key from the user and store it in a variable.
3. Using an if statement and the in operator, check if the key is present in the dictionary using the dictionary.keys() method.
4. If it is present, print the value of the key.
5. If it isn’t present, display that the key isn’t present in the dictionary.
6. Exit.
Sample Input :
Enter key to check : A
Sample Output :
Key is present and value of the key is: 1
......
ANS:
d={"A":1,"B":2,"C":3}
print("Enter key to check:")
key=input()
if key in d.keys():
    print("Key is present and value of the key is:",d[key])
else:
    print("Key isn't present!")
......
code:
......

my_dict = {'A': 1, 'B': 2, 'C': 3}

key_to_check = input("Enter key to check: ")


if key_to_check in my_dict.keys():
    
    print(f"Key is present and value of the key is: {my_dict[key_to_check]}")
else:
    
    print("Key is not present in the dictionary.")
.......
output:
.......
Enter key to check: A
Key is present and value of the key is: 1

=== Code Execution Successful ===
