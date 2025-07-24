print("### CONTADOR DE NOTAS ###")

def string_to_note(string, semitone):

    scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    tuning = {
        1: 4,  # E
        2: 9,  # A
        3: 2,  # D
        4: 7,  # G
        5: 11, # B
        6: 4,  # E
    }
    
    nota=(tuning[string]+semitone)
    letra = scale[nota % 12]
    return letra
while True:
    print("insira a nota e a corda")
    string = int(input("Corda:"))
    semitone = int(input("Casa:"))
    print(string_to_note(string,semitone))
