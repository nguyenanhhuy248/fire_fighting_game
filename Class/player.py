from game_map import *
from Class.equipment import *

class Player:
    
    def __init__(self, state):
        self.state = state
        self.mask = None
        self.extinguisher = None
        
    @staticmethod
    def check_valid_direction(val, direction):
        if val in [1,2]:
            return direction in ('left', 'right')
        elif val == 3:
            return direction in ('left', 'right', 'down')
        elif val == 4:
            return direction in ('left', 'right', 'up') 
        elif val == 5:
            return direction in ('right', 'down')     
        elif val in [6,8,9,10,11]:
            return direction in ('right', 'up', 'down')    
        elif val == 7:
            return direction in ('right', 'up')    
        elif val == 12:
            return direction in ('left', 'down') 
        elif val in [13,15,16,17,18]:
            return direction in ('left', 'up', 'down')
        elif val == 14:
            return direction in ('left', 'up')        
        else:
            return direction in ('left', 'right', 'up', 'down')
     
    def __get_next_coordinate(self, direction: str, distance: int):
        """Get the position after a move or look
        """
        row, col = self.state[0], self.state[1]
        if direction == 'up':
            if (row-distance) >= 0:
                next_coordinate = (row-distance), col
            else:
                next_coordinate = False
        elif direction == 'down':
            if (row+distance) <= 16:
                next_coordinate = (row+distance), col
            else:
                next_coordinate = False
        elif direction == 'left':
            if (col-distance) >= 0:
                next_coordinate = row, (col-distance)
            else:
                next_coordinate = False
        elif direction == 'right':
            if (col+distance) <= 18:
                next_coordinate = row, (col+distance)
            else:
                next_coordinate = False
        return next_coordinate

    def __get_valid_next_coordinate(self, direction: str, distance: int):

        row, col = self.state[0], self.state[1]
        val_in_board = matrix[row, col]

        if Player.check_valid_direction(val_in_board, direction):  # move
            next_coordinate = self.__get_next_coordinate(direction, distance)
        else:  # invalid move
            next_coordinate = False

        return next_coordinate


    def move(self, direction: str, distance: int):
        """Moving: return the position after a valid move
        """
        nextCoordinate = self.__get_valid_next_coordinate(direction, distance)
        if nextCoordinate == False:
            return False
        else: 
            self.state = nextCoordinate
            return True


    def look(self, direction: str):
        """Look: return the position right beside the current position (distance = 1)
        """
        look_position = self.__get_next_coordinate(direction, 1)
        if look_position:
            return look_position
        else:
            return False

    
    def collect(self,matrix):
        
        if matrix[self.state[0], self.state[1]] in [9,16]:
            item = Mask('oxygen mask')
            self.mask = item
            matrix[self.state[0], self.state[1]] -= 3
            print(f'You have collected an item\n{Mask.display(self.mask)}\n')
        
        elif matrix[self.state[0], self.state[1]] in [11,18]:
            item = Extinguisher('Dry powder extinguisher',5)
            self.extinguisher = item
            matrix[self.state[0], self.state[1]] -= 5
            print(f'You have collected an item\n{Extinguisher.display(item)}\n')

        elif matrix[self.state[0], self.state[1]] in [10,17]:
            item = Extinguisher('Foam extinguisher',3)
            self.extinguisher = item
            matrix[self.state[0], self.state[1]] -= 4
            print(f'You have collected an item\n{Extinguisher.display(item)}\n')

        else:
            print('No item to collect in your current position\n')
