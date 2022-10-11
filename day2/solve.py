
def op_1(command_index, memory):

    arg1i = memory[command_index + 1]
    arg2i = memory[command_index + 2]
    resi = memory[command_index + 3]

    memory[resi] = memory[arg1i] + memory[arg2i]

    return command_index + 4


def op_2(command_index, memory):

    arg1i = memory[command_index + 1]
    arg2i = memory[command_index + 2]
    resi = memory[command_index + 3]

    memory[resi] = memory[arg1i] * memory[arg2i]

    return command_index + 4


command_to_func = {
    1: op_1,
    2: op_2,
}

def run_program(memory):

    command_index = 0

    while True:

        command = memory[command_index]

        if command == 99:
            break
        else:
            func = command_to_func[command]

        command_index = func(command_index, memory)


def run_with_mods(noun, verb, initial_memory):
    memory = initial_memory.copy()

    memory[1] = noun
    memory[2] = verb

    run_program(memory)

    return memory[0]


if __name__ == "__main__":

    with open("input.txt") as file:
        intext = file.read()
    
    splittext = intext.split(",")
    memory = [ int(command) for command in splittext ]

    successful_params = None

    for noun in range(0,100):
        for verb in range(0,100):

            result = run_with_mods(noun, verb, memory)

            if result == 19690720:
                successful_params = (noun, verb)
                break

        if successful_params is not None:
            break

    success_noun, success_verb = successful_params
    success_num = (100 * success_noun) + success_verb
    print(success_num)
    