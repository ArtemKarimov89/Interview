from Stack import Stack

if __name__ == '__main__':
    brackets_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']

    for sub_brackets in brackets_list:
        stack = Stack()
        for item in sub_brackets:
            stack.push(item)
            stack.new_item_correct()
            if stack.SUBSEQUENCE_STATE == 'Несбалансированно':
                break
        stack.sub_is_correct()
        print(stack)
