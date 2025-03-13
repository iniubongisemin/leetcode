"""
1. Formatted Twinkle Poem
Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

def poem():
    print("""Twinkle, twinkle, little star,\n\t
	How I wonder what you are!\n\t\t 
		Up above the world so high\n\t\t   		
		Like a diamond in the sky.\n
Twinkle, twinkle, little star,\n\t 
	How I wonder what you are""")
	
# poem()

"""
2. Write a  Python program to find out what version of Python you are using.
"""
def python_version():
    import sys
    print("PYTHON VERSION", sys.version)
    
python_version()


"""
3. Write a Python program to display the current date and time.
Sample Output:
Current date and time:
2014-07-05 14:34:14"""
def current_date():
    from datetime import datetime
    print("Current date and time:\n", datetime.now().replace(microsecond=0))
current_date()

