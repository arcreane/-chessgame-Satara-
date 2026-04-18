class Bishop(Piece):
    def __str__(self):
        return 'B'

    def isValidmove(self, newPosition, board):
        dc = abs(newPosition.col_index() - self._position.col_index())
        dr = abs(newPosition.row_index() - self._position.row_index())

        if dc == 0 or dc != dr:
            return False


        return (self._is_path_clear(newPosition, board) and
                self._destination_free_or_enemy(newPosition, board)))