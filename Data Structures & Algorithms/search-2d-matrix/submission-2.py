class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len=len(matrix)
        column_len=len(matrix[0])
        l, r = 0, row_len-1 
        while l < r:
            mid_row = l+(r-l)//2
            
            if matrix[mid_row][column_len-1]>=target:
                r=mid_row #Target could be in this row as well
            else:
                l=mid_row+1
        
        target_row=l
        l, r= 0, column_len-1
        while l<=r:
            mid=l+(r-l)//2
            
            if matrix[target_row][mid]==target:
                return True
            elif matrix[target_row][mid]>target:
                r=mid-1
            else:
                l=mid+1
        
        return False
            




