# -*- coding: utf-8 -*-

import sys
from __builtin__ import str

def main():
    number1 = raw_input("Enter first number : ")
    number2 = raw_input("Enter second number : ")

    operator = raw_input("Enter  operation (+, -, *, /) : ")
    
    while operator not in ["+", "-", "*", "/", ":"]:
        print ("Enter  operation (+, -, *, /) :")
        operator = raw_input("Enter  operation (+, -, *, /) : ")

    if (operator == '+'):
        print (number1 , " + " , number2 , " = " , (int(number1)+int(number2)))
    if (operator == '-'):
        print (number1 , " + " , number2 , " = " , (int(number1)-int(number2)))
    if (operator == '*'):
        print (number1 , " + " , number2 , " = " , (int(number1)*int(number2)))
    if (operator == '/' or operator == ":"):
        print (number1 , " + " , number2 , " = " , (int(number1)/int(number2)))

if __name__ == "__main__":
    main()