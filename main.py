class Stack:

    def __init__(self, val, position=0):
        self.empty_list = [val]
        self.position = position

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.empty_list):
            raise StopIteration
        position = self.position
        self.position += 1
        return f'{self.empty_list[position]}'

    def __repr__(self):
        return f"{self.empty_list}"

    def isempty(self):
        if len(self.empty_list) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.empty_list.append(value)

    def pop(self):
        return self.empty_list.pop()

    def peek(self):
        return self.empty_list[-1]

    def size(self):
        return len(self.empty_list)


def checking(brackets_: Stack) -> str:
    brackets_dict = {}
    close_bracket = [')', '}', ']']
    open_bracket = ['(', '{', '[']
    brackets_dict_ = dict(zip(open_bracket, close_bracket))

    for bracket in brackets_:
        if len(bracket) % 2 != 0:
            return "Несбалансированно"
        else:
            for val_, bracket_ in enumerate(bracket):
                if (bracket_ in open_bracket) and (bracket[val_ - len(bracket)] in close_bracket) and \
                        (bracket[val_ - len(bracket)] != brackets_dict_[bracket[val_]]):

                    return "Несбалансированно"

            for bracket_ in bracket:
                if bracket_ in brackets_dict:
                    brackets_dict[bracket_] += 1
                else:
                    brackets_dict[bracket_] = 1

            if brackets_dict.get('(') != brackets_dict.get(')') or brackets_dict.get('[') != brackets_dict.get(']') or\
                    brackets_dict.get('{') != brackets_dict.get('}') or (bracket[0] in close_bracket) or\
                    (bracket[-1] in open_bracket):
                return "Несбалансированно"
            else:
                return "Cбалансированно"


if __name__ == '__main__':
    example = '(((([{}]))))'
    brackets = Stack(example)
    print(checking(brackets))
