# 108291492
BASE = 10
START_OF_SEQUENCE = "["
END_OF_SEQUENCE = "]"
DIGIT_RANGE = range(ord('0'), ord('9') + 1)



def decode_instructions(encoded_instructions: str) -> str:
    """
    Декодирует закодированную инструкцию и возвращает раскодированную строку.

    Аргументы:
    encoded_instructions (str): Закодированная инструкция, содержащая цифры, скобки и символы.

    Возвращает:
    str: Раскодированная строка на основе закодированной инструкции.

    Пример использования:
    encoded_instructions = "3[a]2[bc]"
    decoded_instructions = decode_instructions(encoded_instructions)
    print(decoded_instructions)
    "aaabcbc"
    """

    stack: list = []  # Список для хранения элементов стека
    num: int = 0
    temp_str: str = ""
    for char in encoded_instructions:
        if ord(char) in DIGIT_RANGE:
            num = num * BASE + int(char)
        elif char == START_OF_SEQUENCE:
            stack.append((temp_str, num))
            temp_str = ""
            num = 0
        elif char == END_OF_SEQUENCE:
            prev_str, repeat_times = stack.pop()
            temp_str = prev_str + temp_str * repeat_times
        else:
            temp_str += char

    return temp_str


if __name__ == "__main__":
    encoded_instructions = input()
    decoded_instructions = decode_instructions(encoded_instructions)
    print(decoded_instructions)

