import math

try:
    
    id = input("your id: ")

    rule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rule2 = ['10', '11',  '12', '13', '14', '15', '16', '17', '34', '18', '19', '20', '21', '22',
        '35', '23', '24', '25', '26', '27', '28', '29', '32' ,'30', '31','33']
    
    for i in range(0, len(rule)):
        if id[0] == rule[i]:
            first = int(rule2[i])
            break
        
    
    sum = (first % 10) * 9 + math.floor((first / 10))

    
    mul = 8
    for i in range(1, len(id) - 1):
        sum += mul * int(id[i])
        mul -= 1

    leave = sum % 10
    if leave == 0:
        if int(id[len(id) - 1]) == 0:
            print('True')
        else:
            print('False')
    else:

        if (10 - leave) == int(id[len(id) - 1]):
            print('True')
            
        else:
            print('False')

except:
    print('error!')    
    

