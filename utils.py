import re, names, random as r

def name():
    name = [("Seu nome Aleatório: " + names.get_full_name(gender = "male" "female"))]
    return (r.choice(name))


def password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symb = "!@#$%&*^?"
    string = lower + upper + num + symb
    length = 16 
    passwordd = "".join(r.sample(string,length))
    return("Sua nova Senha: " + passwordd)


def email():
    lower = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    mail = "@gmail.com"
    string = lower + num
    length = 15
    Email = "".join(r.sample(string,length)) 
    return ("Seu novo EMAIL: "+ Email + mail)


def numero():
    ddd = "61" ,"62" ,"64" ,"65", "66", "67", "68","96", "82", "97", "91", "93", "94", "69", "95", "63", "82", "71", "73", "74", "75", "77", "85", "88", "98", "99", "83", "81", "87", "86", "89", "84", "79", "11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "24", "27", "28", "31", "32", "33", "34", "35", "37", "38", "41", "42", "43", "44", "45", "46", "51", "53", "54", "55"
    nove = "99"
    num = "0123456789"
    string = num
    length = 7
    numeroo = "".join(r.sample(string,length))
    return("Seu número é: " + (r.choice(ddd)) + nove + numeroo)


def get_digit(cpff: str) -> int:
    len_cpf = len(cpff) + 1

    multiplication = []
    for cpf_index, multiplier in enumerate(range(len_cpf, 1, -1)):
        multiplication.append(int(cpff[cpf_index]) * multiplier)
    total_sum = sum(multiplication)
    digit = 11 - (total_sum % 11)
    return digit if digit < 10 else 0


def get_digit_one(cpff: str) -> int:
    return get_digit(cpff[:9])


def get_digit_two(cpff: str) -> int:
    return get_digit(cpff[:10])


def remove_not_numbers(cpff: str) -> str:
    return re.sub(r'\D', '', cpff)


def has_eleven_chars(value: str) -> bool:
    return len(value) == 11


def is_sequence(value: str) -> bool:
    return (value[0] * len(value)) == value


def is_valid(cpff: str) -> bool:
    clean_cpf = remove_not_numbers(cpff)

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


def cpf() -> str:
    nine_digits = ''.join([str(r.randint(0, 9)) for x in range(9)])
    digit_one = get_digit_one(nine_digits)
    digit_two = get_digit_two(f'{nine_digits}{digit_one}')
    new_cpf = f'{nine_digits}{digit_one}{digit_two}'
    return new_cpf


def formater(cpff: str) -> str:
    return f'{cpff[:3]}.{cpff[3:6]}.{cpff[6:9]}-{cpff[9:]}'


if __name__ == "__main__":

    for i in range(1):
        cpff = cpf()
        cpf_formatado = formater(cpff)
       
        print("Seu CPF é: " + cpff)
        #print(cpf, cpf_formatado)