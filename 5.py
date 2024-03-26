def inverte_string(string):
    string_list = list(string)
    tamanho = len(string_list)
    metade = tamanho // 2
    for i in range(metade):
        tmp = string_list[i]
        string_list[i] = string_list[tamanho - 1 - i]
        string_list[tamanho - 1 - i] = tmp

    return ''.join(string_list)

def main():
    input_string = input("Digite a String a ser Invertida: ")
    print(inverte_string(input_string))

main()