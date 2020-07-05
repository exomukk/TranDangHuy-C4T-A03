open_list = ["[","{","("] 
close_list = ["]","}",")"] 

def is_balanced(selfs): 
    self.items = list(selfs)
    for i in self: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
string = "{[]{()}}"
print(string,"-", is_balanced(string)) 
