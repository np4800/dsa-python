# -*- coding: utf-8 -*-
"""
Given a Prefix expression, convert it into a Postfix expression. 

Input :  Prefix :  *+AB-CD
Output : Postfix : AB+CD-*
Explanation : Prefix to Infix :  (A+B) * (C-D)
              Infix to Postfix :  AB+CD-*

Input :  Prefix :  *-A/BC-/AKL
Output : Postfix : ABC/-AK/L-*
Explanation : Prefix to Infix :  (A-(B/C))*((A/K)-L)
              Infix to Postfix : ABC/-AK/L-* 
"""

prefix="*-A/BC-/AKL"

# Stack for storing the operands
stack = []

# Reverse the content of prefix string
rev_prefix = prefix[::-1]
print(rev_prefix)

# Iterating through individual tokens(characters)
for ch in rev_prefix:
    if not ch.isalpha():
        a = stack.pop()
        b = stack.pop()
        temp = a + b + ch
        stack.append(temp)
        
    else:
        stack.append(ch)

print(*stack)