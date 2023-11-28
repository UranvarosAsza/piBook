#include "USB.h"
#include "USBHIDKeyboard.h"
#include <Arduino.h>
#define LAYOUT LAYOUT_HUN
USBHIDKeyboard Keyboard;

//ESP32 S2 Mini pins:
int MyPinsInOrder[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 21, 33, 34, 35, 36, 37, 38, 39, 40};
int total = 27;

void makeInputFromPin(int pin) // "go_z" in the original
{
  pinMode(pin, INPUT_PULLUP);
  digitalWrite(pin, HIGH);
}

void makeOutputFromPin(int pin)
{
  pinMode(pin, OUTPUT);
  digitalWrite(pin, LOW);
}

void readPinNumber(int button_num) {  // "usb_num" in the original
  switch (button_num) {
    case 1:
      Keyboard.press('1');
      Keyboard.write(KEY_TAB);
      break;
    case 2:
      Keyboard.press('2');
      Keyboard.write(KEY_TAB);
      break;
    case 3:
      Keyboard.press('3');
      Keyboard.write(KEY_TAB);
      break;
    case 4:
      Keyboard.press('4');
      Keyboard.write(KEY_TAB);
      break;
    case 5:
      Keyboard.press('5');
      Keyboard.write(KEY_TAB);
      break;
    case 6:
      Keyboard.press('6');
      Keyboard.write(KEY_TAB);
      break;
    case 7:
      Keyboard.press('7');
      Keyboard.write(KEY_TAB);
      break;
    case 8:
      Keyboard.press('8');
      Keyboard.write(KEY_TAB);
      break;
    case 9:
      Keyboard.press('9');
      Keyboard.write(KEY_TAB);
      break;
    case 10:
      Keyboard.press('1');
      Keyboard.press('0');
      Keyboard.write(KEY_TAB);
      break;
    case 11:
      Keyboard.press('1');
      Keyboard.press('1');
      Keyboard.write(KEY_TAB);
      break;
    case 12:
      Keyboard.press('1');
      Keyboard.press('2');
      Keyboard.write(KEY_TAB);
      break;
    case 13:
      Keyboard.press('1');
      Keyboard.press('3');
      Keyboard.write(KEY_TAB);
      break;
    case 14:
      Keyboard.press('1');
      Keyboard.press('4');
      Keyboard.write(KEY_TAB);
      break;
    case 15:
      Keyboard.press('1');
      Keyboard.press('5');
      Keyboard.write(KEY_TAB);
      break;
    case 16:
      Keyboard.press('1');
      Keyboard.press('6');
      Keyboard.write(KEY_TAB);
      break;
    case 17:
      Keyboard.press('1');
      Keyboard.press('7');
      Keyboard.write(KEY_TAB);
      break;
    case 18:
      Keyboard.press('1');
      Keyboard.press('8');
      Keyboard.write(KEY_TAB);
      break;
    case 21:
      Keyboard.press('1');
      Keyboard.press('9');
      Keyboard.write(KEY_TAB);
      break;
    case 33:
      Keyboard.press('2');
      Keyboard.press('0');
      Keyboard.write(KEY_TAB);
      break;
    case 34:
      Keyboard.press('2');
      Keyboard.press('1');
      Keyboard.write(KEY_TAB);
      break;

    case 35:
      Keyboard.press('2');
      Keyboard.press('2');
      Keyboard.write(KEY_TAB);
      break;
    case 36:
      Keyboard.press('2');
      Keyboard.press('3');
      Keyboard.write(KEY_TAB);
      break;
    case 37:
      Keyboard.press('2');
      Keyboard.press('4');
      Keyboard.write(KEY_TAB);
      break;
    case 38:
      Keyboard.press('2');
      Keyboard.press('5');
      Keyboard.write(KEY_TAB);
      break;
    case 39:
      Keyboard.press('2');
      Keyboard.press('6');
      Keyboard.write(KEY_TAB);
      break;
    case 40:
      Keyboard.press('2');
      Keyboard.press('7');
      Keyboard.write(KEY_TAB);
      break;

    default:
      Keyboard.press('H');
      Keyboard.press('I');
      Keyboard.press('B');
      Keyboard.press('A');
  }
}
void down_arrow(void) {
  Keyboard.write(KEY_DOWN_ARROW); // send a down arrow
  delay(20); 
  
}

void setup() {

  for (int k = 0; k < total; k++) {  // loop thru all row-column pins
    makeInputFromPin(MyPinsInOrder[k]); // set each pin as an input with a pullup
  }

  Keyboard.begin();
  USB.begin();
}

void loop() {

  for (int i = 0; i < total - 1; i++) { // outer loop index
    makeOutputFromPin(MyPinsInOrder[i]); // make the outer loop pin an output and send this pin low
    for (int j = i + 1; j < total; j++) { // inner loop index
      delayMicroseconds(10); // give time to let the signals settle out
      if (!digitalRead(MyPinsInOrder[j])) {  // check for connection between inner and outer pins
        readPinNumber(MyPinsInOrder[i]); // send outer loop I/O number over usb
        readPinNumber(MyPinsInOrder[j]); // send inner loop I/O number over usb
        down_arrow(); // send a down arrow over usb
        while (!digitalRead(MyPinsInOrder[j])) { // wait until key is released
          ;                              // if 2 pins are shorted, the code will hang here
        }
      }
    }
    makeInputFromPin(MyPinsInOrder[i]); // return the outer loop pin to float with pullup
  }
  delay(25);
}
