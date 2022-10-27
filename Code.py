import string
import names
import re
import random as r
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 

name = [("Seu nome Aleatório: " + names.get_full_name(gender = "male" "female"))]

#female = [("A Female Random Name:" + names.get_full_name(gender = "female"))]

#print("\n")#
#("A Male Random Name:" + names.get_full_name(gender = "male"))
#("\nA Female Random Name:" + names.get_full_name(gender = "female"))
#print("\n")

print('\n')
print(r.choice(name))
print('\n')

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symb = "!@#$%&*^?"
mail = "@gmail.com"

string = lower + upper + num + symb
length = 16 
passwaord = "".join(r.sample(string,length))
print("Sua nova Senha: " + passwaord)
print('\n')

string = lower + num
length = 15
email = "".join(r.sample(string,length)) 
print("Seu novo EMAIL: "+ email + mail) 
print('\n')

ddd = "61" ,"62" ,"64" ,"65", "66", "67", "68","96", "82", "97", "91", "93", "94", "69", "95", "63", "82", "71", "73", "74", "75", "77", "85", "88", "98", "99", "83", "81", "87", "86", "89", "84", "79", "11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "24", "27", "28", "31", "32", "33", "34", "35", "37", "38", "41", "42", "43", "44", "45", "46", "51", "53", "54", "55"
nove = "99"

string = num
length = 7
numero = "".join(r.sample(string,length))
print("Seu número é: " + (r.choice(ddd)) + nove + numero)
print("\n")

dia = "01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"
mes = "01","02","03","04","05","06","07","08","09","10","11","12"

string = mes
length = 1
data = "".join(r.sample(string,length))
print("Sua data de Nascimento é: " + (r.choice(dia)) + data + "1987")
print("\n")

def get_digit(cpf: str) -> int:
    len_cpf = len(cpf) + 1

    multiplication = []
    for cpf_index, multiplier in enumerate(range(len_cpf, 1, -1)):
        multiplication.append(int(cpf[cpf_index]) * multiplier)
    total_sum = sum(multiplication)
    digit = 11 - (total_sum % 11)
    return digit if digit < 10 else 0


def get_digit_one(cpf: str) -> int:
    return get_digit(cpf[:9])


def get_digit_two(cpf: str) -> int:
    return get_digit(cpf[:10])


def remove_not_numbers(cpf: str) -> str:
    return re.sub(r'\D', '', cpf)


def has_eleven_chars(value: str) -> bool:
    return len(value) == 11


def is_sequence(value: str) -> bool:
    return (value[0] * len(value)) == value


def is_valid(cpf: str) -> bool:
    clean_cpf = remove_not_numbers(cpf)

    if not has_eleven_chars(clean_cpf):
        return False

    if is_sequence(clean_cpf):
        return False

    digit_one = get_digit_one(clean_cpf)
    digit_two = get_digit_two(clean_cpf)

    new_cpf = f'{clean_cpf[:9]}{digit_one}{digit_two}'

    if new_cpf == clean_cpf:
        return True
    return False


def generate() -> str:
    nine_digits = ''.join([str(r.randint(0, 9)) for x in range(9)])
    digit_one = get_digit_one(nine_digits)
    digit_two = get_digit_two(f'{nine_digits}{digit_one}')
    new_cpf = f'{nine_digits}{digit_one}{digit_two}'
    return new_cpf


def formater(cpf: str) -> str:
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


if __name__ == "__main__":

    for i in range(1):
        cpf = generate()
        cpf_formatado = formater(cpf)
       
        print("Seu CPF é: " + cpf)
        #print(cpf, cpf_formatado)
        print("\n")
