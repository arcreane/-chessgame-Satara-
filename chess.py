from board import Board
from player import Player
from ai_player import AIPlayer
from position import Position


class Chess:
    """
    Classe principale gérant la partie d'échecs.

    Attributs:
        _board (Board): plateau de jeu
        _players (list): liste des 2 joueurs
        _currentPlayer (Player): joueur qui a la main
    """

    def __init__(self):
        """Initialise une partie d'échecs."""
        self._board = Board()
        self._players = []
        self._currentPlayer = None

    def initPlayers(self):
        """
        Demande les noms des joueurs et les instancie.
        Si le nom saisi est 'AI', instancie un AIPlayer.
        """
        for i, color in enumerate([0, 1]):
            name = input(f"Entrez le nom du joueur {i + 1} ({'Blanc' if color == 0 else 'Noir'}) : ")
            if name == "AI":
                self._players.append(AIPlayer(color))
            else:
                self._players.append(Player(name, color))
        self._currentPlayer = self._players[0]

    def displayBoard(self):
        """Affiche l'état actuel du plateau."""
        self._board.display()

    def isValidMove(self, move):
        """
        Vérifie si le coup saisi est valide.

        Args:
            move (str): coup saisi ex: 'Nb1 Nc3'

        Returns:
            bool: True si le coup est valide
        """
        try:
            parts = move.strip().split()
            if len(parts) != 2:
                return False

            src_str = parts[0]
            dst_str = parts[1]

            src_pos = Position(src_str[1], int(src_str[2]))
            dst_pos = Position(dst_str[1], int(dst_str[2]))

            piece = self._board.getPiece(src_pos)

            if piece is None:
                print("Aucune pièce à cette position.")
                return False

            if piece.color != self._currentPlayer.color:
                print("Ce n'est pas votre pièce.")
                return False

            return piece.isValidMove(dst_pos, self._board)

        except (IndexError, ValueError):
            print("Format invalide. Exemple : Nb1 Nc3")
            return False

    def updateBoard(self, move):
        """
        Met à jour le plateau après un coup valide.

        Args:
            move (str): coup validé ex: 'Nb1 Nc3'
        """
        parts = move.strip().split()
        src_pos = Position(parts[0][1], int(parts[0][2]))
        dst_pos = Position(parts[1][1], int(parts[1][2]))
        self._board.movePiece(src_pos, dst_pos)

    def switchPlayer(self):
        """Bascule vers l'autre joueur."""
        if self._currentPlayer == self._players[0]:
            self._currentPlayer = self._players[1]
        else:
            self._currentPlayer = self._players[0]

    def isCheckMate(self):
        """
        Vérifie si le roi adverse a été capturé
        ou si le joueur courant n'a aucun mouvement valide.

        Returns:
            bool: True si la partie est terminée
        """
        from pieces.king import King

        # Vérifie si un roi est absent du plateau
        for color in [0, 1]:
            king_found = False
            for piece in self._board._board.values():
                if isinstance(piece, King) and piece.color == color:
                    king_found = True
                    break
            if not king_found:
                winner = "Blanc" if color == 1 else "Noir"
                print(f"\n*** {winner} gagne ! Le roi adverse a été capturé ! ***")
                return True

        # Vérifie si le joueur courant a au moins un mouvement valide
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        current_color = self._currentPlayer.color
        for piece in list(self._board._board.values()):
            if piece.color == current_color:
                for col in columns:
                    for row in range(1, 9):
                        newPos = Position(col, row)
                        if piece.isValidMove(newPos, self._board):
                            return False

        print(f"\n*** Pat ou échec et mat ! Match nul ! ***")
        return True

    def save(self, filename="save.txt"):
        """
        Sauvegarde la partie dans un fichier.

        Args:
            filename (str): nom du fichier de sauvegarde
        """
        with open(filename, 'w') as f:
            for pos_str, piece in self._board._board.items():
                f.write(f"{pos_str},{str(piece)},{piece.color}\n")
        print(f"Partie sauvegardée dans {filename}")

    def load(self, filename="save.txt"):
        """
        Charge une partie depuis un fichier.

        Args:
            filename (str): nom du fichier de sauvegarde
        """
        from pieces.king import King
        from pieces.queen import Queen
        from pieces.bishop import Bishop
        from pieces.knight import Knight
        from pieces.rook import Rook
        from pieces.pawn import Pawn

        piece_map = {
            'K': King, 'Q': Queen, 'B': Bishop,
            'N': Knight, 'R': Rook, 'P': Pawn
        }

        self._board._board.clear()
        with open(filename, 'r') as f:
            for line in f:
                pos_str, piece_letter, color = line.strip().split(',')
                pos = Position(pos_str[0], int(pos_str[1]))
                piece = piece_map[piece_letter](pos, int(color))
                self._board._board[pos_str] = piece
        print(f"Partie chargée depuis {filename}")

    def play(self):
        """Démarre et gère la boucle principale de la partie."""
        self.initPlayers()

        while not self.isCheckMate():
            self.displayBoard()

            move = None
            while not move or not self.isValidMove(move):
                if isinstance(self._currentPlayer, AIPlayer):
                    move = self._currentPlayer.askMove(self._board)
                else:
                    move = self._currentPlayer.askMove()

            self.updateBoard(move)
            self.switchPlayer()


if __name__ == "__main__":
    print("Test Chess :")
    game = Chess()
    game._board.display()
    print("Tests Chess OK !")