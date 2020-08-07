
class SudukoSolver:

    def printGrid(self, arr):
        """
        This method prints the suduko grid in required manner.
        """
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=' ')
            print()

    def checkEmptyPos(self, arr, l):
        """
        This method checks if there is any empty position in the grid and
        returns the first empty position.
        """
        for row in range(9):
            for col in range(9):
                if arr[row][col] == 0:
                    l[0] = row
                    l[1] = col
                    return True
        return False

    def isSafeRow(self, arr, row, num):
        """
        This method ensures the number is not present in the entire row.
        """
        for i in range(9):
            if arr[row][i] == num:
                return False
        return True

    def isSafeCol(self, arr, col, num):
        """
        This method ensures the number is not present in the entire column.
        """
        for i in range(9):
            if arr[i][col] == num:
                return False
        return True

    def isSafeBox(self, arr, row, col, num):
        """
        This method ensures the number is not present in particular box.
        """
        def assignCol(col):
            if col<3:
                return 0
            elif col<6:
                return 3
            else:
                return  6

        if row<3:
            rowStart = 0
            colStart = assignCol(col)
        elif row<6:
            rowStart = 3
            colStart = assignCol(col)
        else:
            rowStart = 6
            colStart = assignCol(col)

        for i in range(rowStart, rowStart+3):
            for j in range(colStart, colStart+3):
                if arr[i][j] == num:
                    return False
        return True

    def isSafeNum(self, arr, row, col, num):
        """
        This method ensures that the number is safe to use.
        """

        if ( self.isSafeRow(arr, row, num) and self.isSafeCol(arr, col, num) and
            self.isSafeBox(arr, row, col, num) ):
            return True
        return False 

    def solver(self, arr):

        l = [0,0]
        if not self.checkEmptyPos(arr, l):
            return True

        row = l[0]
        col = l[1]

        for num in range(1,10):

            if self.isSafeNum(arr, row, col, num):
                arr[row][col] = num

                if self.solver(arr):
                    return True
                
                arr[row][col] = 0

        return False


if __name__=="__main__": 
      
    grid =[[0 for x in range(9)]for y in range(9)] 
        
    grid =[[0, 0, 0, 0, 4, 0, 0, 0, 0], 
            [0, 6, 0, 0, 2, 0, 8, 0, 0], 
            [4, 2, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 6, 2, 4], 
            [0, 0, 0, 3, 0, 0, 0, 5, 0], 
            [0, 0, 0, 5, 9, 0, 0, 8, 0], 
            [5, 0, 0, 0, 0, 0, 7, 0, 0], 
            [0, 0, 9, 1, 0, 7, 0, 0, 0], 
            [0, 0, 8, 0, 0, 0, 0, 0, 6]] 

    obj = SudukoSolver()

    if obj.solver(grid):
        obj.printGrid(grid)
    else:
        print("No solution exists")
