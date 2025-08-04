class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        i = 0
        total_res = 0
        my_dict_index = dict()
        for j in range(len(fruits)):
            type_f = fruits[j]
            my_dict_index[type_f] = j
            if len(my_dict_index) > 2:
                total_res = max(total_res, j - i)
                while i<j and my_dict_index[fruits[i]] != i:
                    i+=1
                to_del = my_dict_index[fruits[i]]
                del my_dict_index[fruits[i]]
                i+=1
            
        return max(total_res, j-i + 1)