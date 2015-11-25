class my_super_math:
    def __init__(self,my_list):
        self.my_list=my_list

    def avreage(self):
        avr=0
        for n in self.my_list:
            avr += n
        return avr /= len(self.my_list)
