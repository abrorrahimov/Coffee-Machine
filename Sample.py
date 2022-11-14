def romanToInt(roman_number):

    # print(roman_number)    
        
    int_number = 0

    dic = {
            "IV":"4 ", 
            "IX": "9 ",
            "XL":"40 ",
            "XC":"90 ",
            "CD":"400 ",
            "CM":"900 ",
            "I":"1 ",
            "V":"5 ",
            "X":"10 ",
            "L":"50 ",
            "C":"100 ",
            "D":"500 ",
            "M":"1000 "
            }             

    for item in dic:
        while item in roman_number:
            roman_number = roman_number.replace(item, dic[item])
            
    number_list = roman_number.split()

    while "" in number_list:
        number_list.remove("")
                
    for number in number_list:
        
        int_number += int(number) 
        
    return int_number        
         
print(romanToInt("LVIII"))
print(romanToInt("III"))
print(romanToInt("MCMXCIV"))