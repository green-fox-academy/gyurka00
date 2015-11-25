class my_super_string:
    def __init__(self,my_str):
        self.my_str = my_str
    def reverse(self):
        tmp=''
#commentid code with some example just for me
        '''i=0
        while i < len(self.my_str):
            tmp = self.my_str[i] + tmp
            i+=1
        for n in self.my_str:
            tmp = n + tmp
        i=len(self.my_str)-1
        while i >= 0:
            tmp += self.my_str[i]
            i -= 1'''
        n=len(self.my_str)
        for i in range(n-1, -1, -1):
            tmp += self.my_str[i]
        return (tmp)

    def count(self, char_elem):
        counter = 0
        for chr in self.my_str:
            if char_elem == chr:
                counter += 1
        return (counter)

    def no_space(self):
        no_space =''
#commentid code with some example just for me
        '''i=0
        while i < len(self.my_str):
            if self.my_str[i] == ' ':
                no_space += '_'
            else:
                no_space += self.my_str[i]
            i +=1'''
        for i in self.my_str:
            if i == ' ':
                no_space += '_'
            else:
                no_space += i
        return no_space
