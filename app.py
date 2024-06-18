import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
#       region,provincia,distrito,dni,candidato,esvalido
# 1. Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# 2. Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# 3. Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# 4. el DNI debe ser valido (8 digitos)

def imprimir_cantidad_votos_x_candidato(votosxcandidato, candidato):
    print()
    print("Imprimir cantidad de votos por candidato: ")
    for candidato in votosxcandidato:
        print('candidato: ' + candidato + ' votos validos: ' + str(votosxcandidato[candidato]))
    print()

def imprimir_candidato_ganador(ordenado, cantidad_votos_validos): # requisito 1, 2 y 3
    # print(ordenado[0][1])
    # print(ordenado[0][1][1])
    # print(ordenado[0][1])
    # print(ordenado[1][1])
    if cantidad_votos_validos == 0: # no hay votos validos
        # print(1)
        return []
    elif ordenado[0][1][1] > cantidad_votos_validos/2: # 1. hay un candidato con >50% de votos validos
        # print(2)
        return [ordenado[0][1]]
    elif ordenado[0][1][1] == ordenado[1][1][1] & ordenado[0][1][1] == cantidad_votos_validos/2:  # 3. hay empate
        # print(3)
        return [ordenado[0][1]]
    else:
        # print(4)
        return [ordenado[0][1], ordenado[1][1]] # 2. no hay un candidato con >50% de votos validos
    

def validar_dni(dni): # requisito 4
    return len(dni) == 8

def ordenar_por_cantidad_votos(votosxcandidato):
    return sorted(votosxcandidato.items(), key=lambda item:item[1][1], reverse=True)

class CalculaGanador:

    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    def calcularganador(self, data):
        votosxcandidato = {} # diccionario de candidatos y votos
        cantidad_votos = 0
        cantidad_votos_validos = 0
        for registro in data:
            cantidad_votos += 1
            if (validar_dni(registro[3])):
                if not registro[4] in votosxcandidato:
                    votosxcandidato[registro[4]] = [registro[4], 0]
                if registro[5] == '1':
                    votosxcandidato[registro[4]][1] = votosxcandidato[registro[4]][1] + 1
                    cantidad_votos_validos += 1
        
        print("Cantidad de votos: ", cantidad_votos)
        print("Cantidad de votos validos: ", cantidad_votos_validos)

        ordenado = ordenar_por_cantidad_votos(votosxcandidato)
        # print("->>>>", ordenado)
        # print(ordenado[1][1][1])

        imprimir_cantidad_votos_x_candidato(votosxcandidato, ordenado[0][0])

        return imprimir_candidato_ganador(ordenado, cantidad_votos_validos)



c = CalculaGanador()
print(c.calcularganador(c.leerdatos()))
print()
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'], # No Valido
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'] # Valido
]
print(c.calcularganador(datatest))
print()

# Test 1 Retornar el candidato con mayor cantidad de votos validos >50%
print("Test 1 Retornar el candidato con mayor cantidad de votos validos >50% -------------------------------------------------")
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '23017966', 'Aundrea Grace', '1'] # Valido
]
print(c.calcularganador(datatest))
print("Respuesta esperada: [['Aundrea Grace', 3]]")
print()

# Test 2 Retornar los dos candidatos con mayor cantidad de votos validos <50%
print("Test 2 Retornar los dos candidatos con mayor cantidad de votos validos <50% -------------------------------------------------")
datatest = [
['Áncash', 'Asunción', 'Acochaca', '10810062', 'Rafael Lopez', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '17533597', 'Rafael Lopez', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '10810063', 'Rafael Lopez', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '17533598', 'Rafael Lopez', '0'], # No Valido
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '40810063', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '57533598', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '86777323', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '23017966', 'Aundrea Grace', '1'] # Valido
]
print(c.calcularganador(datatest))
print("Respuesta esperada: [['Eddie Hinesley', 4], ['Aundrea Grace', 4]]")
print()

# Test 3 Retornar el candidato que aparece primero en el archivo
print("Test 3 Retornar el candidato que aparece primero en el archivo -------------------------------------------------")
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'] # Valido
]
print(c.calcularganador(datatest))
print("Respuesta esperada: [['Eddie Hinesley', 2]]")
print()

# Test 3.1 Retornar el candidato que aparece primero en el archivo
print("Test 3.1 Retornar el candidato que aparece primero en el archivo -------------------------------------------------")
datatest = [
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'] # Valido
]
print(c.calcularganador(datatest))
print("Respuesta esperada: [['Aundrea Grace', 2]]")
print()

# Test 4 Verificar que el DNI sea valido
print("Test 4 Verificar que el DNI sea valido -------------------------------------------------")
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'], # No Valido
['Áncash', 'Asunción', 'Acochaca', '575335', 'Eddie Hinesley', '1'], # No Valido
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], # Valido
['Áncash', 'Asunción', 'Acochaca', '230179', 'Aundrea Grace', '1'] # No Valido
]
print(c.calcularganador(datatest))
print("Respuesta esperada: [['Aundrea Grace', 1]]")
print()
