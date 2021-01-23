import pickle
import pandas as pd

contador = 1
criaturas = 0
tierras = 0
instantaneos = 0
conjuros = 0
planeswalker = 0
artefactos = 0
encantamientos = 0
creatures = ["Creature", "Legendary Creature", "Artifact Creature", "Land Creature"]
lands = ["Land", "Land Creature", "Legendary Land", "Basic Snow Land", "Basic Land", "Artifact Land", "Legendary Sorcery"]
artifacts = ["Artifact Creature", "Artifact", "Artifact Land", "Legendary Artifact"]
enchantments = ["Enchantment", "Enchantment Creature", "Legendary Enchantment Creature"]
respuesta = []

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

df = pd.read_excel("..\Datos\Decklists.xlsx")

for e in df.columns:
    print(f"Opcion{contador}: " + f"{e}" + "\n")
    respuesta.append(e)
    contador += 1
entrada = int(input("Elije decklist: "))
entrada -= 1
df2 = df[f"{respuesta[entrada]}"]

resultados = []
for e in df2:
    if e.strip() in b.keys():
        resultados.append(b[e.strip()])
tipos_de_carta = []
for e in resultados:
    if e[0][1] == "{":
        tipos_de_carta.append(e[1][2:])
    else:
        tipos_de_carta.append(e[0][1:])

for e in tipos_de_carta:
    if e.split("—")[0].strip().split("—")[0] in creatures:
        criaturas += 1
    elif e.split("—")[0].strip().split("—")[0] in lands:
        tierras += 1
    elif e.split("—")[0].strip().split("—")[0] in artifacts:
        artefactos += 1
    elif e.split("—")[0].strip().split("—")[0] in enchantments:
        encantamientos += 1
    elif e.split("—")[0].strip() == "Legendary Planeswalker":
        planeswalker += 1
    elif e.split("—")[0].strip() == "Instant":
        instantaneos += 1
    elif e.split("—")[0].strip() == "Sorcery":
        conjuros += 1
    else:
        print(e)
total = criaturas + tierras + instantaneos + conjuros + planeswalker + artefactos + encantamientos

print(f"{respuesta[entrada]}:  " + "\n" +
       f"Criaturas: {criaturas}" + "\n" +
       f"Tierras: {tierras}" + "\n" +
       f"Instantaneos: {instantaneos}" + "\n" +
       f"Conjuros: {conjuros}" + "\n" +
       f"Artefactos: {artefactos}" + "\n" +
       f"Encantamientos: {encantamientos}" + "\n" +
       f"Planeswalker: {planeswalker}" + "\n" +
       f"Total: {total}")

input("Pulsa una tecla para cerrar")