
class Stack:
    """
    Стек — абстрактный тип данных, представляющий список элементов, организованных по принципу LIFO (англ. last in —
    first out, «последним пришёл — первым вышел»). Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы
    взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии: стрельба начнётся с патрона,
    заряженного последним.

    Нужно реализовать класс Stack со следующими методами:
    is_empty — проверка стека на пустоту. Метод возвращает True или False;
    push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
    pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
    peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
    size — возвращает количество элементов в стеке.
    """

    BRACKET_COUNT = 0
    BLOCK_BRACKET_COUNT = 0
    FIGURE_BRACKET_COUNT = 0
    SUBSEQUENCE_STATE = ""

    def __init__(self):
        self.data = []

    def __str__(self):
        return self.SUBSEQUENCE_STATE

    def is_empty(self):
        return len(self.data) == 0

    def push(self, new_bracket):
        self.data.append(new_bracket)
        self.bracket_count(new_bracket)

    def pop(self):
        del_item = self.data.pop(self.size() - 1)
        return del_item

    def peek(self):
        last_elem = self.data[self.size() - 1]
        return last_elem

    def size(self):
        return len(self.data)

    def bracket_count(self, new_bracket):
        if new_bracket == '(':
            self.BRACKET_COUNT += 1
        elif new_bracket == '[':
            self.BLOCK_BRACKET_COUNT += 1
        elif new_bracket == '{':
            self.FIGURE_BRACKET_COUNT += 1
        elif new_bracket == ')':
            self.BRACKET_COUNT -= 1
        elif new_bracket == ']':
            self.BLOCK_BRACKET_COUNT -= 1
        elif new_bracket == '}':
            self.FIGURE_BRACKET_COUNT -= 1

    def new_item_correct(self):
        if self.SUBSEQUENCE_STATE == "Несбалансированно":
            return

        new_bracket = self.pop()
        new_bracket_direction = self.define_item(new_bracket)

        if self.size() == 0:
            if new_bracket_direction == 'reversed':
                self.SUBSEQUENCE_STATE = "Несбалансированно"
            self.push(new_bracket)
            return

        last_bracket = self.peek()
        last_bracket_direction = self.define_item(last_bracket)

        if (new_bracket_direction == 'reversed' and last_bracket_direction == 'straight'
                and not self.brackets_correct(last_bracket, new_bracket)):
            self.SUBSEQUENCE_STATE = "Несбалансированно"

        self.push(new_bracket)

    def brackets_correct(self, open_bracket, close_bracket):
        if ((open_bracket == '(' and close_bracket == ')')
                or (open_bracket == '[' and close_bracket == ']') or (open_bracket == '{' and close_bracket == '}')):
            is_correct = True
        else:
            is_correct = False
        return is_correct

    def sub_is_correct(self):
        if self.SUBSEQUENCE_STATE == "Несбалансированно":
            return
        elif self.BRACKET_COUNT == 0 and self.BLOCK_BRACKET_COUNT == 0 and self.FIGURE_BRACKET_COUNT == 0:
            self.SUBSEQUENCE_STATE = 'Сбалансированно'
        else:
            self.SUBSEQUENCE_STATE = "Несбалансированно"

    def define_item(self, item):
        if item == '(' or item == '[' or item == '{':
            return 'straight'
        else:
            return 'reversed'