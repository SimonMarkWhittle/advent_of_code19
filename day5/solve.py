
from tkinter import E


def get_param_mode(command, param_i):

    strcomm = str(command)
    mode_i = 2 + param_i

    if mode_i > len(strcomm):
        return 0
    else:
        return int(strcomm[-mode_i])


def isolate_command(command):

    strcomm = str(command)
    return int(strcomm[-2:])


def get_params(command_index, num_params, memory):

    command = memory[command_index]

    params = []
    for param_num in range(1, num_params+1):
        param_mode = get_param_mode(command, param_num)

        param_i = command_index + param_num
        param = memory[param_i]

        if param_mode:
            params.append(param)
        else:
            params.append(memory[param])

    return params


def add(command_index, memory):

    arg1, arg2 = get_params(command_index, 2, memory)

    resi = memory[command_index + 3]
    memory[resi] = arg1 + arg2

    return command_index + 4


def mult(command_index, memory):

    arg1, arg2 = get_params(command_index, 2, memory)
    resi = memory[command_index + 3]

    memory[resi] = arg1 * arg2

    return command_index + 4


def get_in(command_index, memory):

    outi = memory[command_index + 1]

    good_arg = False
    
    while not good_arg:
        try:
            print("Please input a number.")
            arg = input()
            arg = int(arg)

            good_arg = True
        except:
            print("Bad input!\nPlease try again.")
            pass

    memory[outi] = arg

    return command_index + 2


def out(command_index, memory):

    out = get_params(command_index, 1, memory)

    print(out)
    
    return command_index + 2


def jump_true(command_index, memory):
    
    arg1, jump_pos = get_params(command_index, 2, memory)

    if arg1:
        return jump_pos
    else:
        return command_index + 3


def jump_false(command_index, memory):
    arg1, jump_pos = get_params(command_index, 2, memory)

    if arg1:
        return command_index + 3
    else:
        return jump_pos


def less_than(command_index, memory):
    arg1, arg2 = get_params(command_index, 2, memory)
    resi = memory[command_index + 3]

    memory[resi] = int(arg1 < arg2)

    return command_index + 4


def equals(command_index, memory):
    arg1, arg2 = get_params(command_index, 2, memory)
    resi = memory[command_index + 3]

    memory[resi] = int(arg1 == arg2)

    return command_index + 4


command_to_func = {
    1: add,
    2: mult,
    3: get_in,
    4: out,
    5: jump_true,
    6: jump_false,
    7: less_than,
    8: equals,
}

def run_program(memory):

    command_index = 0

    count = 0
    while True:

        command = memory[command_index]
        opcode = isolate_command(command)

        if command == 99:
            break
        else:
            func = command_to_func[opcode]

        command_index = func(command_index, memory)

        if count > 10000:
            break
        else:
            count += 1
    
    if count > 10000:
        print("Halted from count!")
        print(f"Command index: {command_index}")


def run_with_mods(noun, verb, initial_memory):
    memory = initial_memory.copy()

    memory[1] = noun
    memory[2] = verb

    run_program(memory)

    return memory[0]


if __name__ == "__main__":

    print("loading program...")
    with open("input.txt") as file:
        intext = file.read()
    
    splittext = intext.split(",")
    memory = [ int(command) for command in splittext ]

    # memory = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    print("running program...")
    run_program(memory)
    