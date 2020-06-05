# Задание 2.
# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from operator import itemgetter

class MyNode:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def walk(self, code, value, data=None):
        if self.data != None:
            code[self.data] = ''.join(value)
        else:
            self.left.walk(code, value + ['0'])
            self.right.walk(code, value + ['1'])

def huffman_encode(mytext):
    chars = {}
    for k, v in dict(Counter(mytext)).items():
        chars[MyNode(data=k)] = v
    leaves = list(chars.items())
    while len(leaves) > 1:
        leaves.sort(key=itemgetter(1), reverse=True)
        left_leaf = leaves.pop()
        right_leaf = leaves.pop()
        new_node = left_leaf[1] + right_leaf[1]
        leaves.append((MyNode(left=left_leaf[0], right=right_leaf[0]), new_node))
    node = leaves.pop()[0]
    code = {}
    node.walk(code, [])
    #print(code)
    encryption = []
    for i in mytext:
        encryption.append(code[i])
    return encryption, code

s = 'substract subclass remembers'
encrypt,code = huffman_encode(s)
str_code = ' '.join(encrypt)
print(f'Для строки\n{s}\nкод = {str_code}\nТаблица соотвествия:\n{code}')
