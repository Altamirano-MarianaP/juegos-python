# juegos-python
Juegos en Python hechos en la facultad
# Juegos de azar y lógica en Python

Programa de consola con un menú principal que reúne cuatro juegos y un reporte de estadísticas por jugador. Desarrollado como trabajo práctico de la facultad (Ingeniería en Sistemas, UTN).

## Juegos

**A. Mayor o menor**
Se muestra un número del 1 al 1000 y hay que adivinar si el siguiente será mayor o menor. Cada acierto suma a la racha y la ronda termina al fallar. El programa guarda la mejor racha de cada jugador.

**B. Número secreto**
Hay que adivinar un número entre 1 y 100 en 6 intentos. Después de cada intento se indica si el número secreto es mayor o menor. Se puede salir en cualquier momento y se registran las partidas ganadas y perdidas.

**C. Blackjack**
Partida contra la banca con un mazo de 52 cartas sin repetir. El jugador elige pedir carta o plantarse, y la banca juega hasta llegar a 17. El As vale 11 o 1 según convenga. Se registran partidas, victorias y derrotas.

**D. Par o impar**
Se lanzan dos dados y hay que adivinar si la suma es par o impar, apostando créditos (cada jugador empieza con 1000). Los créditos se acumulan entre partidas y el jugador no puede apostar más de lo que tiene.

## Características

- Hasta 10 jugadores por juego, con nombre validado.
- Opción de reporte con las estadísticas de todos los juegos.
- Validación de las entradas del usuario en cada juego.
- Interfaz de texto con colores y cuadros dibujados en la terminal.

## Conceptos aplicados

Variables, condicionales (`if`), ciclos (`while`, `for`), listas, funciones y las bibliotecas nativas `random`, `time` y `os`.

## Cómo ejecutarlo

Requiere Python 3 y una terminal de Windows (usa comandos como `cls`).

```
python TP_AltamiranoMariana.py
```
