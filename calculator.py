first_number = input('your number?')
second_number = input('second number')
result = int(second_number) + int(first_number) 
print(result)
any_coment = input('any comment?: (1 = yes) (2 = no) ')
if any_coment.lower() == 'yes' :
    question1 = input('if you need other calculation? what its operator (+, -, *, **)')
else: print('bye')    
if question1.lower() == '+' :
    number1 = input('what is first number?')
    number2 = input('what is 2 number?')
    result1 = int(number1) + int(number2)
    print(result1)
    if question1.lower() == '-' :
          minuscalculation = input('first number? :')
          minuscalculation1 = input('second number? :')
          result2 = int(minuscalculation) - int(minuscalculation1)
          print(result2)
if question1.lower() == '*' :
    oricalculation = input('first number')
    oricalculation1 = input('second number')
    result3 = int(oricalculation) * int(oricalculation1)
    print(result3)
    


   
