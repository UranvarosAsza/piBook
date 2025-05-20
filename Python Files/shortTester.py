import board
import digitalio
import time

# Lista a vizsgálandó GPIO-król
pins_in_use = [
    board.IO39, board.IO40, board.IO37, board.IO38,
    board.IO35, board.IO36, board.IO33, board.IO34,
    board.IO18, board.IO21, board.IO16, board.IO17,
    board.IO15, board.IO14, board.IO13, board.IO11,
    board.IO8,  board.IO9,  board.IO6,  board.IO7,
    board.IO4,  board.IO5,  board.IO2,  board.IO3
]


inputs = []
for pin in pins_in_use:
    dio = digitalio.DigitalInOut(pin)
    dio.direction = digitalio.Direction.INPUT
    dio.pull = digitalio.Pull.DOWN  # VAGY PULL.UP a billentyűzet függvényében
    inputs.append(dio)

# Előző állapot
last_state = [False] * len(inputs)

print("Figyelés elindítva...\n")

while True:
    current_state = [dio.value for dio in inputs]

    if current_state != last_state:
        print("GPIO változás:")
        for i, state in enumerate(current_state):
            if state:
                print(f" - GPIO {i + 1} (pin: {pins_in_use[i]}): HIGH")
        print("---")
        last_state = current_state[:]

    time.sleep(0.0001)