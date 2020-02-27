#Created by Gick)

import win32api

#library of virtual keys
global VK
VK={'backspace': 8, 'tab': 9, 'clear': 12, 'enter': 13, 'ctrl': 17, 'alt': 18, 'pause': 19, 'caps_lock': 20, 'esc': 27, 'spacebar': 32, 'page_up': 33, 'page_down': 34, 'end': 35, 'home': 36, 'left_arrow': 37, 'up_arrow': 38, 'right_arrow': 39, 'down_arrow': 40, 'select': 41, 'print': 42, 'execute': 43, 'print_screen': 44, 'ins': 45, 'del': 46, 'help': 47, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, 'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74, 'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90, 'numpad_0': 96, 'numpad_1': 97, 'numpad_2': 98, 'numpad_3': 99, 'numpad_4': 100, 'numpad_5': 101, 'numpad_6': 102, 'numpad_7': 103, 'numpad_8': 104, 'numpad_9': 105, 'multiply_key': 106, 'add_key': 107, 'separator_key': 108, 'subtract_key': 109, 'decimal_key': 110, 'divide_key': 111, 'F1': 112, 'F2': 113, 'F3': 114, 'F4': 115, 'F5': 116, 'F6': 117, 'F7': 118, 'F8': 119, 'F9': 120, 'F10': 121, 'F11': 122, 'F12': 123, 'F13': 124, 'F14': 125, 'F15': 126, 'F16': 127, 'F17': 128, 'F18': 129, 'F19': 130, 'F20': 131, 'F21': 132, 'F22': 133, 'F23': 134, 'F24': 135, 'num_lock': 144, 'scroll_lock': 145, 'left_shift': 160, 'right_shift ': 161, 'left_control': 162, 'right_control': 163, 'left_menu': 164, 'right_menu': 165, 'browser_back': 166, 'browser_forward': 167, 'browser_refresh': 168, 'browser_stop': 169, 'browser_search': 170, 'browser_favorites': 171, 'browser_start_and_home': 172, 'volume_mute': 173, 'volume_Down': 174, 'volume_up': 175, 'next_track': 176, 'previous_track': 177, 'stop_media': 178, 'play/pause_media': 179, 'start_mail': 180, 'select_media': 181, 'start_application_1': 182, 'start_application_2': 183, 'attn_key': 246, 'crsel_key': 247, 'exsel_key': 248, 'play_key': 250, 'zoom_key': 251, 'clear_key': 254, '+': 187, ',': 188, '-': 189, '.': 190, '/': 191, '`': 192, ';': 186, '[': 219, '\\': 220, ']': 221, "'": 222}


#check which key is pressed
def check_key_pressed():
    while True:
        for i in VK:
            if win32api.GetAsyncKeyState(VK[i]) !=0:
                return i

#take id of key from library of virtual keys
def give_vk_id(name):
	return VK[name]

if __name__=="__main__":
    print("Please press the button:")
    name_of_key=check_key_pressed()
    print("You pressed: "+ name_of_key + ", id virtual key is: "+ str(give_vk_id(name_of_key)))
