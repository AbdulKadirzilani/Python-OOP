# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
s= "{[]{()}}"
stack = []
for i in s:

        if i in open_list:
            stack.append(i)

        elif i in close_list:
            pos = close_list.index(i)
            print(pos)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                print("Unbalanced")
if len(stack) == 0:
        print("Balanced")



