class Solution(object):
    def braceExpansionII(self, expression):
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    sub, i = parse(i + 1)
                else:
                    sub = {expression[i]}
                    i += 1

                current = {a + b for a in current for b in sub}

                if i < len(expression) and expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

            result.update(current)

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        ans, _ = parse(0)
        return sorted(ans)