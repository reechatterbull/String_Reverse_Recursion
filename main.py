""" THIS IS A CODE TO REVERSE A STRING USING RECURSION """
"""----------------------------------------------------"""

def reverse_recur(s:str):
  #Define base case (termination condition)
  #Base case: 
  if len(s) == 1: #If input string is of length 1
    return s
    
  #Define recursion condition
  else:
    return reverse_recur(s[1:])+s[0]
       
if __name__ == '__main__':
  str = input("Enter string to be reversed:\n")
  print(f"Reversed string is \n {reverse_recur(str)}")
  
    