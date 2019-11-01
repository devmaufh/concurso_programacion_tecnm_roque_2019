alfabeto = {
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--.."
}

f = open("file.txt", "r")
salida = ""
for x in f:
  for letra in x.lower():
    if( letra in alfabeto):
      salida = salida+" " + alfabeto[letra]

archivo = open("salida.txt", "w+")
archivo.write(salida)
archivo.close()