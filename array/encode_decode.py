class Solution:

    def encode(self,strs) -> str:
        list_to_str = ""

        for str in strs:
            list_to_str += f"${len(str)}{str}"

        return list_to_str            


    def decode(self,str:str) -> list:
        str_to_list = []
        i=0
        while(i < len(str)):
            if(str[i] == "$"):
                j = i + 1

                if(str[j].isdigit()):
                    length_str = str[j]

                    length = int(length_str)

                    j += 1

                    start_index = j
                    end_index = length + start_index
                    str_to_list.append(str[start_index:end_index])

                i = end_index

        return str_to_list



            



s = Solution()

s_encode = s.encode(["neet","code","love","you"])
print(s.decode(s_encode))
