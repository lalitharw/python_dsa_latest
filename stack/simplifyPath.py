class SimplifyPath:

    def simplify(self,path:str) -> str:

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

        

        # return "/" + "/".join(stk) if stk else "/"

        # simplify version
        
        if(stk):
            return "/" + "/".join(stk)
        else:
            return "/"


        #    "/" + "/".join(['home', 'foo'])  # Result is "/home/foo"
        #  


path = SimplifyPath()



# If the delimiter is at the start or end of the string, or appears consecutively, you may get empty strings as part of the result:
print(path.simplify("/home//foo/"))
print(path.simplify("/../"))
print(path.simplify("/.../"))