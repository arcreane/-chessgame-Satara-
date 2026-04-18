class King(Piece):
    def __str__(self):
        return 'K'

    def isValidMove(self, newPosition, board):
        # Calcul de la distance parcourue
        dc = abs(newPosition.col_index() - self._position.col_index())
        dr = abs(newPosition.row_index() - self._position.row_index())

        # Le roi bouge de max 1 case
        if dc > 1 or dr > 1 or (dc == 0 and dr == 0):
            return False

        return self._destination_free_or_enemy(newPosition, board)