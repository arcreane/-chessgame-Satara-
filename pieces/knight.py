class Knight(Piece):
    def __str__(self):
       # N : Knight
        return 'N'

    def isValidMove(self, newPosition, board):

        dc = abs(newPosition.col_index() - self._position.col_index())
        dr = abs(newPosition.row_index() - self._position.row_index())

        # mvt en L ( 2 H + 1V ou 1H ou 1 H + 2 V)
        if not ((dc == 2 and dr == 1) or (dc == 1 and dr == 2)):
            return False


        # Verif seulement de la destination arriver
        return self._destination_free_or_enemy(newPosition, board)