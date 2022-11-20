class List:
    def remove_(self, integer_list, values_list):
        #your code here
        return list(filter(lambda x: x not in values_list, integer_list))
