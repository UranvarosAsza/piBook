# piBook

## For my Raspberry Pi - iBook conversion

    My hobby project in witch I install a raspberry pi in an iBook G4.

## Main Files:

### keyboard_scanner.cpp:

- Using Arduino
- Acts as a keyboard
- Reads the input pins from the FPC connector
- Writes the pin-info for every pressed key on the keyboard

### code.py

- Using Circuitpython and the kmk lib:
  [KMK Github](https://github.com/KMKfw)
  [S2 Mini .Bin files](https://circuitpython.org/board/lolin_s2_mini/)
  [Circuitpython install](https://www.wemos.cc/en/latest/tutorials/s2/get_started_with_circuitpython_s2.html)
- Keyboard file using the kmk lib
