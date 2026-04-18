class Rook(Piece):
    def __str__(self):
        #'R': nom de la tour
        return 'R'

    def isValidMove(self, newPosition, board):
        # coup valide pour la tour , mvt sur la colonne ou rangée
        dc = abs(newPosition.col_index() - self._position.col_index())
        dr = abs(newPosition.row_index() - self._position.row_index())

        if (dc == 0 and dr == 0) or (dc != 0 and dr != 0):
            return False

        # Verification  qu'aucune pièce ne bloque le chemin
        # Verif : Case d'arrivé  est bloqué  ou contient ennemie
        return (self._is_path_clear(newPosition, board) and
                self._destination_free_or_enemy(newPosition, board))