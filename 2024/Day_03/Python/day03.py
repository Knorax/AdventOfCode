MUL_STR = "mul("
DO_STR = "do()"
DONT_STR = "don\'t()"
MAX_PARAM_SIZE = 7
MIN_PARAM_SIZE = 3

MAX_INT32 = (2**31) - 1

def main():
    filename = "input.txt"
    memory = ""

    with open(filename) as file:
        memory = file.read()

    print("Part 1 answer:")
    part1_getMultiplificationCommands(memory)

    print("Part 2 answer:")
    part2_getMultiplyCommandWithEnables(memory)

def part1_getMultiplificationCommands(memory: str):
    token = 0 
    sum = 0

    while token != -1:
        token = memory.find(MUL_STR, token + 1)

        closing_bracket = memory.find(")", token + 1)
        next_mul_token = memory.find(MUL_STR, token + 1)

        if next_mul_token != -1 and closing_bracket > next_mul_token:
            continue
        elif (closing_bracket - token) > len(MUL_STR) + MAX_PARAM_SIZE:
            continue
        elif (closing_bracket - token) < len(MUL_STR) + MIN_PARAM_SIZE:
            continue
        elif not "," in memory[token + len(MUL_STR) : closing_bracket - 1]:
            continue

        left, right = memory[token + len(MUL_STR) : closing_bracket].split(",", 1)

        if len(left) > 3 or len(left) == 0 or len(right) > 3 or len(right) == 0: 
            continue

        left_nb = 0
        right_nb = 0
        try:
            left_nb = int(left)
            right_nb = int(right)

        except Exception:
            continue

        sum = sum + left_nb * right_nb

    print(sum)

def part2_getMultiplyCommandWithEnables(memory: str):
    token = 0 
    enable = True 
    sum = 0

    while token != -1:
        token_mul = memory.find(MUL_STR, token + 1)
        token_do = memory.find(DO_STR, token + 1)
        token_dont = memory.find(DONT_STR, token + 1)

        token_do = token_do if token_do != -1 else MAX_INT32
        token_dont = token_dont if token_dont != -1 else MAX_INT32

        token = min([token_mul, token_do, token_dont])

        if token == token_do:
            enable = True 
            continue
        elif token == token_dont:
            enable = False
            continue
        elif not enable or token == -1:
            continue

        closing_bracket = memory.find(")", token + 1)
        next_mul_token = memory.find(MUL_STR, token + 1)

        if next_mul_token != -1 and closing_bracket > next_mul_token:
            continue
        elif (closing_bracket - token) > len(MUL_STR) + MAX_PARAM_SIZE:
            continue
        elif (closing_bracket - token) < len(MUL_STR) + MIN_PARAM_SIZE:
            continue
        elif not "," in memory[token + len(MUL_STR) : closing_bracket - 1]:
            continue

        left, right = memory[token + len(MUL_STR) : closing_bracket].split(",", 1)

        if len(left) > 3 or len(left) == 0 or len(right) > 3 or len(right) == 0: 
            continue

        left_nb = 0
        right_nb = 0
        try:
            left_nb = int(left)
            right_nb = int(right)

        except Exception:
            continue

        sum = sum + left_nb * right_nb

    print(sum)
    ...

        
def test_part1_getMultiplificationCommands():
    memory_test_cases = [
        "xmul(1,2)",
        # one character placed at different spots
        "xmul(1,2)",
        "xmxul(1,2)",
        "xmulx(1,2)",
        "xmul(x1,2)",
        "xmul(1x,2)",
        "xmul(1,x2)",
        "xmul(1,2x)",
        "xmul(1,2)x",
        # Different number format
        "xmul(11,2)",
        "xmul(111,2)",
        "xmul(1111,2)",
        "xmul(1,22)",
        "xmul(1,222)",
        "xmul(1,2222)",
        "xmul(1)",
        "xmul(12)",
        "xmul(123)",
        # Different token
        "xmul[1,2)",
        "xmul[1,2]",
        "xmul(1,2]",
        # Adding commas
        "xmul(1,2,22)",
        # Multiple mul command after the other
        "xmul(1,2)mul(2,3)",
        "xmul(1,2mul(2,3)",
    ]

    for i, memory in enumerate(memory_test_cases):
        print(f"TEST {i}")
        print(memory)
        part1_getMultiplificationCommands(memory)


def test_part2_getMultiplyCommandWithEnables():
    memory_test_cases = [
        "xmul(1,2)",
        # one character placed at different spots
        "xmul(1,2)",
        "xmxul(1,2)",
        "xmulx(1,2)",
        "xmul(x1,2)",
        "xmul(1x,2)",
        "xmul(1,x2)",
        "xmul(1,2x)",
        "xmul(1,2)x",
        # Different number format
        "xmul(11,2)",
        "xmul(111,2)",
        "xmul(1111,2)",
        "xmul(1,22)",
        "xmul(1,222)",
        "xmul(1,2222)",
        "xmul(1)",
        "xmul(12)",
        "xmul(123)",
        # Different token
        "xmul[1,2)",
        "xmul[1,2]",
        "xmul(1,2]",
        # Adding commas
        "xmul(1,2,22)",
        # Multiple mul command after the other
        "xmul(1,2)mul(2,3)",
        "xmul(1,2mul(2,3)",
        "xdo()mul(1,2mul(2,3)",
        "xdon't()mul(1,2mul(2,3)",
        "xdon't()mul(1,2do()mul(2,3)",
        "xdo()mul(1,2do()mul(2,3)",
        "xdon't()mul(1,2don't()mul(2,3)",
        "xdo()mul(1,2don't()mul(2,3)",
        "xdo()don't()mul(1,2do()mul(2,3)",
    ]

    for i, memory in enumerate(memory_test_cases):
        print(f"TEST {i}")
        print(memory)
        part2_getMultiplyCommandWithEnables(memory)

if __name__ == "__main__":
    main()
    #test_part1_getMultiplificationCommands()
    #test_part2_getMultiplyCommandWithEnables()
