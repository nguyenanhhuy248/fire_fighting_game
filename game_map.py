import numpy as np
import pandas as pd
import random

A = [5,6,6,8,9,6,6,10,6,6,6,11,6,6,6,6,7]
B = [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
C = D = E = F = G = H = I = K = L = M = N = O = P = Q = R = B
J = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4]
S = [12,13,13,15,16,13,13,17,13,13,13,18,13,15,16,13,14]


matrix = np.array([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S]).T

column_list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 
    'O', 'P', 'Q', 'R', 'S'
    ]

def displayed_map (nparray):
    displayed_map = pd.DataFrame(nparray, columns=column_list)
    displayed_map.replace({
                    0: '', 1: '=', 2: '', 3: '', 4:'', 
                    5: '', 6: '', 7: '', 8: '|¬|', 9: 'm',
                    10: 'f', 11: 'p', 12: '', 13: '', 14: '',
                    15: '|¬|', 16: 'm', 17: 'f', 18: 'p'
                    }, inplace=True)
    return displayed_map

init_i = random.choice(
    list(range(1,3))+ list(range(4,8))+list(range(9,13))+list(range(14,16)))

init_j = random.choice(
    list(range(1,9))+list(range(10,17)))

init_a = random.choice(
    list(range(1,3))+ list(range(4,8))+list(range(9,13))+list(range(14,16)))

init_b = random.choice(
    list(range(1,9))+list(range(10,17)))

if __name__ == "__main__":
    print(displayed_map(matrix))

