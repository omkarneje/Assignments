# algorithm to find to find x and y from the sequence
"""list =[10, 1, 8, 3, 6, 5, 4, 7, "x", "y" ]
variable_1= index of x
variable_2= index of y
convert variable_1 and variable_2 into strings
print variable_1 and variable_2
"""
#program to find index of x and y in the sequence
list =[10, 1, 8, 3, 6, 5, 4, 7, "x" , "y" ]
v1=str(list.index("x"))
v2=str(list.index("y"))
print("x is present at index "+ v1 +" and y is pesent at the index " + v2)
