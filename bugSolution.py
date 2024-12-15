def my_function(a, b):
    if b == 0:
        return 0  # Or raise a more specific exception, or return a default value 
    else:
        return a / b

result = my_function(10, 0) 
print(result) # Output: 0