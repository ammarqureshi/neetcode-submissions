class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])


        l, r = 0, ROWS*COLS - 1


        while l<=r: 

            m = l + (r-l) // 2
            '''
            Think of COLS = 4 as four seats per row.
            1. How many full groups of 4 fit into 6?
            2. After taking away that full group of 4, how many positions are left?
            // = how many complete rows did I pass?
            % = how far into the current row am I?
            '''
            row, col = m//COLS, m%COLS

            if target > matrix[row][col]: 
                l = m + 1
            elif target < matrix[row][col]: 
                r = m - 1
            else: 
                return True

        return False