class SimplifyPath:

    def simplify(self,path:str) -> list:

        path_array = path.split("/")
        stk = []
        for p in path_array:
            if p == "..":
                if stk:
                    stk.pop()
            elif p == "." or p == "":
                continue
            
            else:
                stk.append(p)

        

        return "/" + "/".join(stk) if stk else "/"


path = SimplifyPath()



# If the delimiter is at the start or end of the string, or appears consecutively, you may get empty strings as part of the result:
print(path.simplify("/home//foo/"))
print(path.simplify("/../"))
print(path.simplify("/.../"))