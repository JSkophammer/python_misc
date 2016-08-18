import os, sys
import signal

def code_self():
    #print('Beginning process:', os.getpid())
    commands = []
    new_code = []
    while True:
        append_code = input('>>> ')
        if append_code == 'q':
            break
        elif append_code:
            new_code.append(append_code)
            append_code = '    ' + append_code
            commands.append(append_code)
        else: break
    if new_code:
        file = open('self_command.py', 'w')
        file.write('import os, signal, sys\n' + 'def new_commands():\n')
        for command in commands:
            file.write(command + '\n')
        file.close()
        file = open('self_code.py', 'a')
        for codes in new_code:
            file.write('    ' + codes + '\n')
        file.close()
        from self_command import new_commands
        new_commands()

if __name__ == '__main__':
    code_self()
#Append new code here:

    print("hello world")
