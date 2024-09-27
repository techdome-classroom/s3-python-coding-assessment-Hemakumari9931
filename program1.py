def is_valid_parentheses(s: str) -> bool:
    
    stack = []
    
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
       
        if char in bracket_map:
           
            top_element = stack.pop() if stack else '#'
           
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)


    return not stack


if __name__ == "__main__":
    user_input = input("Enter a string of parentheses: ")
    if is_valid_parentheses(user_input):
        print("The input string is valid.")
    else:
        print("The input string is invalid.")







    



  

