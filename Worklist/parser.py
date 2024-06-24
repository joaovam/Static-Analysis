"""
This file implements a parser: a function that reads a text file, and returns
a control-flow graph of instructions plus an environment mapping variables to
integer values. The text file has the following format:

    [First line] A dictionary describing the environment
    [n-th line] The n-th instruction in our program.

As an example, the program below sums up the numbers a, b and c:

    {"a": 1, "b": 3, "c": 5}
    x = add a b
    l2 = x = add x c
"""

from lang import *


def line2env(line: str) -> Env:
    """
    Maps a string (the line) to a dictionary in python. This function will be
    useful to read the first line of the text file. This line contains the
    initial environment of the program that will be created. If you don't like
    the function, feel free to drop it off.

    Example
        >>> line2env('{"zero": 0, "one": 1, "three": 3, "iter": 9}').get('one')
        1
    """
    import json

    env_dict = json.loads(line)
    env_lang = Env()
    for k, v in env_dict.items():
        env_lang.set(k, v)
    return env_lang


def create_Bt(curr, insts):
    ops = curr.split(" ")
    b_t = ops[1].strip("\n")
    if type(insts[int(ops[2])]) != str:
        inst = Bt(b_t)
        inst.add_true_next(insts[int(ops[2])])
        inst.add_next()
    else:
        inst = create_Bt(insts[int(ops[2])], insts)
    return inst;

def file2cfg_and_env(lines):
    """
    Builds a control-flow graph representation for the strings stored in
    `lines`. The first string represents the environment. The other strings
    represent instructions.

    Example:
        >>> l0 = '{"a": 0, "b": 3}'
        >>> l1 = 'bt a 1'
        >>> l2 = 'x = add a b'
        >>> env, prog = file2cfg_and_env([l0, l1, l2])
        >>> interp(prog[0], env).get("x")
        3

        >>> l0 = '{"a": 1, "b": 3, "x": 42, "z": 0}'
        >>> l1 = 'bt a 2'
        >>> l2 = 'x = add a b'
        >>> l3 = 'x = add x z'
        >>> env, prog = file2cfg_and_env([l0, l1, l2, l3])
        >>> interp(prog[0], env).get("x")
        42

        >>> l0 = '{"a": 1, "b": 3, "c": 5}'
        >>> l1 = 'x = add a b'
        >>> l2 = 'x = add x c'
        >>> env, prog = file2cfg_and_env([l0, l1, l2])
        >>> interp(prog[0], env).get("x")
        9
    """
    # TODO: Implement this method.

    #var = add var var
    #var = Mul var var
    #var = Lth var var
    #var = Geq var var
    #Bt var offset

    operations = {"bt":Bt, "mul":Mul, "lth":Lth, "geq":Geq, "add": Add }
    
    env = line2env(lines[0])
    insts = []

    lines.pop(0)

    for l in lines:
        #print("line:", l)
        ops = l.split(" ")
        if ops[0] == "bt":
            #How to deal with jumps
            insts.append(l)

        else:
            target = ops[0].strip("\n")
            op1 = ops[3].strip("\n")
            op2 = ops[4].strip("\n")
            inst = operations[ops[2]](target, op1, op2)
            #print("INST:", inst)
            insts.append(inst)
    
    for i in range(len(insts)):
        curr = insts[i]
        #print("CURR0", curr)
        if type(curr) == str: #it is a BT waiting for connection
            #print("CURR1", curr)
            curr = create_Bt(curr, insts)
            curr.add_next(inst[i+1])
            insts[i] = curr
        #create connections
        #print("TESTE", type(curr))
        if i > 0:
            curr.add_pred(insts[i -1])
            
            
    #env.dump()
    #print("INSTS", insts)

    return (env, insts)

     # type: ignore