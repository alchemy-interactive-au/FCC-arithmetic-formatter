
def arithmetic_arranger(problems):

  print("this is an update")
  firstLine = []
  secondLine = []
  thirdline = []
  fourthLine = []
  placeholders = ""


  # arith = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
  arith = problems

  for i in range(len(arith)):
    
    firstNum = arith[i].split()[0]
    secondNum = arith[i].split()[2]

    operator = arith[i].split()[1]
    # print(arith[i].split()[1])

    if len(arith) > 5:
      print("Error: Too many problems.")
      break
    elif operator != "+" and operator != "-":
      # print(operator)
      print("Error: Operator must be '+' or '-'.")
      break
    elif len(firstNum) > 4 or len(secondNum) > 4:
      # print(firstNum, secondNum)
      print("Error: Numbers cannot be more than four digits.")
      break
  
    # check if (string) numbers are integers (when converted to int)
    try:
      if type(int(firstNum)) != int and type(int(secondNum)) != int:
        print(type(int(firstNum, secondNum)))
        print("Error: Numbers must only contain digits.")
    except:
        print(type(int(firstNum, secondNum)))
        print("Error: Numbers must only contain digits.arithmetic_arranger")
        break
    
    #find longest number string
    longest_string = max(arith[i].split(), key=len)
    # add len of operator & space
    colWidth = len(longest_string) + 2 
    # find gap after operator
    operatorGapLen = colWidth - len(arith[i].split()[2]) - 1 
    # print(operatorGapLen)

    # generate each line
    firstLine.append(arith[i].split()[0]) 
    secondLine.append(arith[i].split()[1] + (' ' * operatorGapLen) + arith[i].split()[2])
    thirdline.append("-" * colWidth) # print a character n times

    #calculate answer - catch non intergers being passed
    try:
      answer = eval(arith[i]) #int
    except:
      print("Error: Numbers must only contain digits.")
      break

    # put answer in string
    arith[i] = arith[i] + " " + str(answer) 
    fourthLine.append(str(answer)) #list

    #generate each sum's width + 4 space col gap
    #eg {: >4} {: >6} {: >5}
    placeholders = placeholders + "{:>" + str(colWidth) + "}    " 

  # print(placeholders) #string
  # print(arith)
  # print(firstLine)
  # print(secondLine)
  # print(thirdline)
  # print(fourthLine)

  tableData = [firstLine, secondLine, thirdline, fourthLine]
  #print(tableData)

  ## print directly
  # for row in tableData:
  #   #print(placeholders)
  #   print(placeholders.format(*row))

  ## print to variable
  arranged_problems = ""
  for row in tableData:
    #print(placeholders)
    arranged_problems = arranged_problems + (placeholders.format(*row)) + "\n"

  # print(arranged_problems)
  return arranged_problems  

#-----Test cases---All passing!----
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
# print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
# print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))


