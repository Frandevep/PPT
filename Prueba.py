import random

opciones = ["piedra", "papel", "tijeras"]

print("🪨📄✂️ ¡Juguemos Piedra, Papel o Tijeras! 🪨📄✂️")

while True:
    usuario = input("Elige (piedra, papel o tijeras): ").lower()
    
    if usuario not in opciones:
        print("❌ Opción inválida. Intenta de nuevo.")
        continue
    
    computadora = random.choice(opciones)
    
    print(f"🧑 Tú elegiste: {usuario}")
    print(f"🤖 La computadora eligió: {computadora}")
    
    if usuario == computadora:
        print("🤝 ¡Empate!")
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        print("🎉 ¡Ganaste!")
    else:
        print("😢 Perdiste...")

    jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        print("¡Gracias por jugar! 👋")
        break
