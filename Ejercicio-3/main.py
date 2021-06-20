SAMPLE_STRING = 'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'

# Separo todas las posibles combinaciones de cadenas y luego las comparo con ellas mismas dadas vuelta.
# Agrego las que son iguales a una coleccion.


def is_palindrome(word):
    return len(word) > 1 and word == word[::-1]


# Devuelve un listado de cadenas (sin repetir) que son palindromos dentro del string.
# Si se quieren repetidos puede usarse una lista.
def process(text):
    text_len = len(text)
    palindromes = set()
    for i in range(text_len):
        for j in range(i, text_len):
            word = text[i:j+1]
            if is_palindrome(word):
                palindromes.add(word)

    return palindromes


if __name__ == '__main__':
    pals = process(SAMPLE_STRING)
    string_replaced = SAMPLE_STRING
    for k in pals:
        string_replaced = string_replaced.replace(k, k.upper())
    print('\n### Palindromos encontrados:', f'({len(pals)})')
    print(pals)
    print('\n### Palindromos convertidos a mayusculas en la cadena:')
    print(string_replaced)
