def last_paren(string):
    index = 0
    last_par = 0
    count = 0
    while index != -1:
        index = string.find('(')
        string_dif = len(string) - len(string[index + 1:])
        string = string[index + 1:]
        last_par += string_dif
        count += 1
    return last_par - 1


def outfn(string):
    space = string.find(' ')
    fn = string[1:space]
    return fn


def find_arg1(string):
    s1 = string.find(' ') + 1
    str_part = string[s1:]
    if str_part[0] == '(':
        end = str_part.find(')') + 1
        arg1 = str_part[:end]
    else:
        s2 = str_part.find(' ') + s1
        arg1 = string[s1:s2]
    return arg1


def next_arg(string):
    arg1 = string.find(find_arg1(string))
    next = string[arg1 + len(find_arg1(string)):]
    end = next.find(')')
    n_arg = next[:end]
    return n_arg


def inner_fn(string):
    lin = last_paren(string)
    str_part = string[lin:]
    fout = str_part.find(')')
    in_fn = str_part[:fout + 1]
    return in_fn


def eval_infn(string):
    equ = ' '.join([find_arg1(inner_fn(string)), outfn(inner_fn(string)), next_arg(inner_fn(string))])
    val = eval(equ)
    return val


def lisp(string):
    print(string)
    while last_paren(string) != 0:
        x = str(eval_infn(inner_fn(string)))
        string = string.replace(inner_fn(string), x)
        print(string)
    return eval_infn(string)


if __name__ == '__main__':
    while True:
        exp = input('LISP> ')
        if exp != 'q':
            print(lisp(exp), '\n')
        else:
            break
