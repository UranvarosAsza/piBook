import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.led import LED
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.international import International

keyboard = KMKKeyboard()
locks = LockStatus()

keyboard.extensions.append(International())    ##ISO kisoztás,  az "Í" billentyű nem szerepel az ANSI-ban, a "KC.NONUS_BSLASH vagy KC.NUBS" kell a helyére
keyboard.extensions.append(locks)

leds = LED(led_pin=[board.IO12, board.IO1,board.IO10, ])         ##leds = LED(led_pin=[board.IO12, board.IO10, board.IO1])

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_caps_lock():
            leds.set_brightness(50, leds=[2])
            print("caps lock is on")
        else:
            leds.set_brightness(0, leds=[2])
            print("caps lock is off")

        if self.get_num_lock():
            leds.set_brightness(50, leds=[0])
            print("num lock is on")
        else:
            leds.set_brightness(0, leds=[0])
            print(" lock is off")

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            print("led status updated")
            self.set_lock_leds()

keyboard.extensions.append(leds)
keyboard.extensions.append(LEDLockStatus())

# .---------------------------------------------------------------.
# | FPC Pin |     GPIO       |     Function / Description         |
# |---------+----------------+------------------------------------|
# |   1     |  board.IO39    |     Keyboard COL 1                 |
# |   2     |  board.IO40    |     Keyboard COL 2                 |
# |   3     |  board.IO37    |     Keyboard COL 3                 |
# |   4     |  board.IO38    |     Keyboard COL 4                 |
# |   5     |  board.IO35    |     Keyboard COL 5                 |
# |   6     |  board.IO36    |     Keyboard COL 6                 |
# |   7     |  board.IO33    |     Keyboard COL 7                 |
# |   8     |  board.IO34    |     Keyboard COL 8                 |
# |   9     |  board.IO18    |     Keyboard COL 9                 |
# |   10    |  board.IO21    |     Keyboard ROW 1                 |
# |   11    |  board.IO16    |     Keyboard ROW 2                 |
# |   12    |  board.IO17    |     Keyboard ROW 3                 |
# |   13    |  board.IO15    |     Keyboard ROW 4                 |
# |   14    |  board.IO14    |     Keyboard ROW 5                 |
# |   15    |  board.IO13    |     Keyboard ROW 6                 |
# |   16    |  board.IO12    |     Scroll Lock LED                |
# |   17    |  board.IO10    |     LED common Ground              |
# |   18    |  board.IO11    |     Keyboard ROW 7                 |
# |   19    |  board.IO8     |     Keyboard ROW 8                 |
# |   20    |  board.IO9     |     Keyboard ROW 9                 |
# |   21    |  board.IO6     |     Keyboard ROW 10                |
# |   22    |  board.IO7     |     Keyboard ROW 11                |
# |   23    |  board.IO4     |     Keyboard ROW 12                |
# |   24    |  board.IO5     |     Keyboard ROW 13                |
# |   25    |  board.IO2     |     Keyboard ROW 14                |
# |   26    |  board.IO3     |     Keyboard ROW 15                |
# |   27    |  board.IO1     |     Caps Lock LED                  |
# |   28    |       -        |                                    |
# |   29    |       -        |                                    |
# |   30    |       -        |                                    |
# '---------------------------------------------------------------'



## Keyboardmatrix kép alapján az alsó táblázat, 1-9 x 10-26 pinek
##      PCB-pins:       1           2           3           4           5           6           7           8           9
keyboard.col_pins = (board.IO39, board.IO40, board.IO37, board.IO38, board.IO35, board.IO36, board.IO33, board.IO34, board.IO18, )
##      PCB-pins:        10         11          12          13          14            15        18          19          20          21        22        23          24          25      26  
keyboard.row_pins = (board.IO21, board.IO16, board.IO17, board.IO15, board.IO14, board.IO13, board.IO11, board.IO8, board.IO9, board.IO6, board.IO7, board.IO4, board.IO5, board.IO2, board.IO3,)

keyboard.diode_orientation = DiodeOrientation.ROW2COL   ##ez valszeg nálunk mindegyis, mert nincs dióda egyedül a LED miatt

##A korábban bescannelt billentyűmátrix alapján épül fel a keymap ( ha saját gyártású lenne a bill, akkor olvashatóbb lenne )
## Az "olvashatóság" miatt a mátrixba magyar billentyű kódokkal hivatkoztam rájuk, de mivel OS szinten dönti el hogy milyen kimenetet
#  ad az ANSI bill adott karaktereinek ezért ezeknek az ANSI helyén lévő nagol bill nevet kell adni-> ki lett szervezve külön  

#FN billentyű nem lézetik -> helyette modifyer key, és layerek hozzáadhatóak, minden layer egy mátrix a layering pedig kmk modul

FN = KC.NUMLOCK 
##ideiglenesen ide majd jön a fn- media layer / lehet hogy a Ctrl kéne a helyére mert idóta pozícióban van és akkor meg két Ctrl lenne amíg nincs layering

##magyar karakterek:

KC.Á = KC.QUOT      ##Jó
KC.É = KC.SCLN      ##Jó
KC.Í = KC.NUBS      ##Jó
KC.Ó = KC.EQUAL     ##Jó
KC.Ö = KC.LBRACKET  ##Jó
KC.Ő = KC.LBRC      ##Jó
KC.Ú = KC.RBRC      ##Jó
KC.Ü = KC.MINUS     ##Jó
KC.Ű = KC.BSLASH    ##Jó

keyboard.keymap = [

     
    #nem a valós map, csak a layerek / debug miatt kell.
    # ,---------------------------------------------------------------------------------------------.
    # |  esc  |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |  F7  |  F8  |  F9  |  F10  |  F11  | F12  |
    # |---------------------------------------------------------------------------------------------|
    # |  0  |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |  9 |  Ö  |  Ü | Ó | Backspace |
    # |---------------------------------------------------------------------------------------------|
    # | tab     |  Q  |  W  |  E  |  R  |  T |  Z  |  U |  I |  O |  P |  Ő |   Ú  |   return       |
    # |--------------------------------------------------------------------------------             |
    # | caps       |  A |  S |  D  |  F  |  G  |  H  |  J  |  K  |  L  |  É  |  Á  | Ű |            |
    # |---------------------------------------------------------------------------------------------|
    # | shift  | Í |  Z |  X |  C |  V |  B |  N |  M |  , |  . |  - |     |  ↑  |    shift         |
    # |---------------------------------------------------------------------------------------------|
    # | fn  | ctrl | opt | cmd |         space           | cmd | opt | ←   |  ↓  |  →               |
    # `---------------------------------------------------------------------------------------------'

  
    [KC.Ú,  KC.Ó, KC.NO, KC.ENTER, KC.SLSH, KC.É, KC.P, KC.N0, KC.F10,
   
    KC.DOWN, KC.UP, KC.NO, KC.Ű, KC.DOT, KC.L, KC.O, KC.N9, KC.F9,
   
    KC.LEFT, KC.RIGHT, KC.NO, KC.RCTL, KC.COMM, KC.K, KC.I, KC.N8, KC.F8,

    KC.NO, KC.NO, KC.NO, KC.NO, KC.M, KC.J, KC.U, KC.N7, KC.F7,
 
    KC.SPACE, KC.NO, KC.NO, KC.NO, KC.N, KC.H, KC.Y, KC.N6, KC.F6,
 
    KC.Á, KC.Ő, KC.NO, KC.Ü, KC.B, KC.G, KC.T, KC.N5, KC.F5,
 
    KC.NO, KC.CAPS_LOCK, KC.NO, KC.NO, KC.V, KC.F, KC.R, KC.N4, KC.F4,
    
    KC.NO, KC.GRV, KC.NO, KC.NO, KC.C, KC.D, KC.E, KC.N3, KC.F3,
    
    KC.TAB, KC.Í, KC.NO, KC.ESC, KC.X, KC.S, KC.W, KC.N2, KC.F2,
    
    KC.BSPC, KC.F12, KC.NO, KC.F11, KC.Z, KC.A, KC.Q, KC.N1, KC.F1,
    
    KC.NO, KC.NO, KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.Ö, KC.NO,
    
    KC.NO, KC.NO, KC.LALT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    
    KC.NO, KC.NO, KC.RGUI, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    
    KC.NO, KC.NO, KC.LCTRL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    
    KC.NO, KC.NO, FN, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],
    
]

if __name__ == '__main__':
    keyboard.go()