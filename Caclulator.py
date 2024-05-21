# warning first python project
# employer look away
problem = input("What is your problem")
problem = ''.join(problem.split())
problemSorted = ""
# removes letters and adds multiplication symbol before parenthesis
for i in range(len(problem)):
    if(problem[i].isalpha() == False):
        problemSorted = problemSorted + problem[i]
    if(problem[i].isnumeric and i != len(problem)-1) and problem[1+i] == ("(") :
        problemSorted = problemSorted + "*"
        

    
    
        
# finds all multiplication and division in symbol