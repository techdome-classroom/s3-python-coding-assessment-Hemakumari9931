class Solution(object):
   def roman_to_integer(s: str) -> int:
  
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0

   
    for char in reversed(s):
        value = roman_map[char]
        
        
        if value < prev_value:
            total -= value
        else:
            total += value
            
       
        prev_value = value

    return total


if __name__ == "__main__":
    user_input = input("Enter a Roman numeral: ")
    integer_value = roman_to_integer(user_input)
    print(f"The integer value of '{user_input}' is: {integer_value}")



class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass



