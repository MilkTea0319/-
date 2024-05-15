import os
import time
from colorama import Fore, Back, Style, just_fix_windows_console

just_fix_windows_console()

print("　　　" + Back.GREEN + Fore.WHITE + Style.BRIGHT + "╔══════════════════╗ " + Style.RESET_ALL)
print("　　　" + Back.GREEN + Fore.WHITE + Style.BRIGHT + "║ 倒數計時自動關機 ║ " + Style.RESET_ALL)
print("　　　" + Back.GREEN + Fore.WHITE + Style.BRIGHT + "╚══════════════════╝ " + Style.RESET_ALL)
print()
print("　　 " + Back.RED + Fore.WHITE + Style.BRIGHT + "單純使用Windows關機排程"+ Style.RESET_ALL)
print()
print(Back.WHITE + Fore.BLACK + "┌───────────────────────────────────┐ " + Style.RESET_ALL)
print(Back.WHITE + Fore.BLACK + "│使用說明：     　            　 　 │ " + Style.RESET_ALL)
print(Back.WHITE + Fore.BLACK + "│ 1.先輸入小時    　         　  　 │ " + Style.RESET_ALL)
print(Back.WHITE + Fore.BLACK + "│ 2.再輸入分鐘            　 　  　 │ " + Style.RESET_ALL)
print(Back.WHITE + Fore.BLACK + "│ 3.倒數時間到自動關機 　      　　 │ " + Style.RESET_ALL)
print(Back.WHITE + Fore.BLACK + "│ 4.小時與分鐘皆輸入0為取消自動關機 │ " + Style.RESET_ALL)
print(Back.WHITE + Fore.BLACK + "└───────────────────────────────────┘ " + Style.RESET_ALL)
print()

while True:
    try:
        hour = int(input('請輸入小時：'))
        if hour >= 0:
            break
        else:
            print(Fore.RED + Style.BRIGHT + "請輸入正整數！" + Style.RESET_ALL)
    except:
        print(Fore.RED + Style.BRIGHT + "只能輸入數字！請重新輸入！" + Style.RESET_ALL)
        pass

while True:
    try:
        min = int(input('請輸入分鐘：'))
        if min >= 0:
            break
        else:
            print(Fore.RED + Style.BRIGHT + "請輸入正整數！" + Style.RESET_ALL)
    except:
        print(Fore.RED + Style.BRIGHT + "只能輸入數字！請重新輸入！" + Style.RESET_ALL)
        pass

if hour == 0 and min == 0:
    os.system('shutdown -a')
    print(Back.CYAN + Fore.WHITE + '已取消自動關機' + Style.RESET_ALL)
    time.sleep(5)
else:
    sec = hour*60*60
    sec += min*60
    os.system('shutdown -s -t ' + str(sec))
    print(Back.CYAN + Fore.WHITE + '電腦將在 '+str(hour)+" 小時 "+str(min)+" 分鐘後關機" + Style.RESET_ALL)
    time.sleep(5)
