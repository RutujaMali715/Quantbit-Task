############## Reverse a string without using built-in methods ##################
N = "hello"
string = ""

for i in N:
    string = i + string
print("Reversed string:",string)