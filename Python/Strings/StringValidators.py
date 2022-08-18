
s = input()

# The any() function returns True if any item in an iterable are true, otherwise it returns False.
print(any(a.isalnum() for a in s) )
print(any(a.isalpha() for a in s) )
print(any(a.isdigit() for a in s) )
print(any(a.islower() for a in s) )
print(any(a.isupper() for a in s) )    
        
       