import sys
import todo

from lang import interp

if __name__ == "__main__":
    #lines = []
    #with open("tests/small_branch.txt", 'r') as file:
    #    lines = file.readlines()
        #file2cfg_and_env(lines)
    lines = sys.stdin.readlines()
    env, program = todo.file2cfg_and_env(lines)
    final_env = interp(program[0], env)
    final_env.dump()
