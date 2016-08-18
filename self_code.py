"""
Type any command at the prompt to execute immediately
and to add that command to this program to be executed
whenever it is run in the future
"""


def code_self():
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
        else:
            break
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
    # Append new code here:

    print("hello world!")
