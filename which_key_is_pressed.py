import win32api
from lib.pywin32_keys import VK


#check which key is pressed
def check_key_pressed():
    try:
        while True:
            for i in VK:
                if win32api.GetAsyncKeyState(VK[i]) !=0:
                    return i
    except:
        print("Something went wrong while checking which key is pressed")


#take id of key from library of virtual keys
def give_vk_id(name):
    	return VK[name]


if __name__=="__main__":
    print("Please press the button:")
    name_of_key=check_key_pressed()
    print("You pressed: "+ name_of_key + ", id virtual key is: "+ str(give_vk_id(name_of_key)))
    #Also if you need to check again which key is press -> You need to wait some time -> Use time.spleep