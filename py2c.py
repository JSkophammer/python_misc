import sys
import os


# create an executable C program to run any Python program

def make_c(python_file):
    filename = python_file.split('.')[0]
    c_filename = filename + '.c'
    c_file = open(c_filename, 'w')

    c_prog = """
    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        system("python %s");
        return 0;
    }
    """ % python_file

    c_file.write(c_prog)
    c_file.close()

    # compile C program with GCC
    os.system('gcc %s -o %s' % (c_filename, filename))


# Accepts Python program as argument if run from command line interface
if __name__ == '__main__':
    py_file = sys.argv[1]
    make_c(py_file)
    fname = py_file.split('.')[0]
    run = input("Run program ('y' or 'n')? ")
    if run == 'y':
        os.system('./%s' % fname)
    else:
        sys.exit()
