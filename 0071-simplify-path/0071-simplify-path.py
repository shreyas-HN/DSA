class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""

        for ch in path:
            if ch == "/":
                if current == "..":
                    if stack:
                        stack.pop()
                elif current != "" and current != ".":
                    stack.append(current)

                current = ""

            else:
                current += ch

        # Process the last component if path doesn't end with "/"
        if current == "..":
            if stack:
                stack.pop()
        elif current != "" and current != ".":
            stack.append(current)

        return "/" + "/".join(stack)


            