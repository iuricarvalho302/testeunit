def validar_cpf(cpf):
    """
    Verifica se um CPF é válido.

    Args:
        cpf (str): O CPF a ser validado (somente números).

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """

    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if len(set(cpf)) == 1:
        return False

    # Calcula os dígitos verificadores
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

    # Verifica se os dígitos verificadores calculados são iguais aos do CPF
    if cpf[9:] == str(digito_1) + str(digito_2):
        return True
    else:
        return False