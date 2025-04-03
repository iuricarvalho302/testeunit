def validar_cpf(cpf):
    """
    Verifica se um CPF é válido.

    Args:
        cpf (str): O CPF a ser validado (somente números).

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """

    
    cpf = ''.join(filter(str.isdigit, cpf))

    
    if len(cpf) != 11:
        return False

   
    if len(set(cpf)) == 1:
        return False

    
    cpf_9 = cpf[:9]
    soma = 0
    for i in range(9):
        soma += int(cpf_9[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0

    cpf_10 = cpf[:10]
    soma = 0
    for i in range(10):
        soma += int(cpf_10[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0

    
    if cpf[9:] == str(digito_1) + str(digito_2):
        return True
    else:
        return False
