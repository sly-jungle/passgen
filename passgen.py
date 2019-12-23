import string, random, re
import time
from termcolor import colored
print(colored('                   ','yellow'))
print(colored('                    ▄▀▀▄','yellow'))
print(colored('             █▀█▀▀▀▀█  █','yellow'))
print(colored('             ▀ ▀     ▀▀','yellow'))

print(colored('   _ __   __ _ ___ ___  __ _  ___ _ __  ','cyan'))
print(colored('  |  _ \ / _` / __/ __|/ _` |/ _ \  _ \ ','cyan'))
print(colored('  | |_) | (_| \__ \__ \ (_| |  __/ | | |','cyan'))
print(colored('  | .__/ \__,_|___/___/\__, |\___|_| |_|','cyan'))
print(colored('  | |                   __/ |           ','cyan'))
print(colored('  |_|                  |___/            ','cyan'))
print(colored('            By sly-jungle'))
time.sleep(2)
print('')
print('')
print('')
N = int(input(colored('/Choose a password length between 8 and 32 : ','magenta'))) 
if N < 8: N = 8
if N > 32: N = 32
password_symbols=string.digits,string.punctuation,string.ascii_uppercase,string.ascii_lowercase
pasgen=''.join(random.choice(''.join(password_symbols)) for _ in range(N))
print('')
print('')
print('_________________________________________________________')
print('')
print(colored(pasgen,'green'))
print('_________________________________________________________')
