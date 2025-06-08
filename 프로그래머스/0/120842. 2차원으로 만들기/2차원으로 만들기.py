def solution(num_list, n):
    import numpy as np

    num_arr = np.array(num_list).reshape(-1,n)

        
    return num_arr.tolist()