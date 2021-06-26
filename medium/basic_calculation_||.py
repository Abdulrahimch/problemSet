class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        oper = '+'
        cache = ''
        # '33+771*5+1'
        for i in s + '+':
            if i in '*-+/':
                if oper == '+':
                    if cache != '':
                        stack.append(+int(cache))

                if oper == '-':
                    if cache != '':
                        stack.append(-int(cache))

                if oper == '*':
                    stack.append(int(cache) * stack.pop())


                if oper == '/':
                    stack.append(int(stack.pop() / int(cache)))


                oper = i
                cache = ''


            else:
                cache += i
            # "33+7*5+1-49/7+7-5+100*2/3"
        return int(sum(stack))

