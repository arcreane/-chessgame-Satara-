class Pawn(Piece):
    def __str__(self):
        return 'P'

    def isValidMove(self, newPosition, board):
        # Blanc (0) monte (+1), Noir (1) descend (-1)
        direction = 1 if self._color == 0 else -1
        # départ: 1 pour Blancs , 6 pour Noir
        start_row = 1 if self._color == 0 else 6

        c1, r1 = self._position.col_index(), self._position.row_index()
        c2, r2 = newPosition.col_index(), newPosition.row_index()

        dc = c2 - c1
        dr = r2 - r1

        target = board.getPiece(newPosition)

        # mvt du pion  tout droit sur la meme colonne/ la case doit être vide

        if dc == 0 and dr == direction:
            return target is None

        # Premier coup peut  avance de deux cases
        # Doit être sur la rangée de départ pour avancer de 2, et les deux cases devant doivent être vides
        if dc == 0 and dr == 2 * direction and r1 == start_row:
            inter = Position.from_indices(c1, r1 + direction)
            return target is None and board.getPiece(inter) is None

        # 3. Capture en diagonale
        # Doit bouger d'une colonne et d'une ligne, et il doit y avoir un ennemi
        if abs(dc) == 1 and dr == direction:
            return target is not None and target.color != self._color

        return False