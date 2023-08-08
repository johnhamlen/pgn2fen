import chess.pgn
import argparse

# Define the script version
VERSION = "1.0.0"

def pgn_to_fen(pgn_file_path, fen_file_path):
    """
    Convert PGN file to a FEN file.

    :param pgn_file_path: Path to the PGN file.
    :param fen_file_path: Path to the output FEN file.
    """

    with open(pgn_file_path, 'r') as pgn_file:
        # Open output file for writing
        with open(fen_file_path, 'w') as fen_file:
            # Parse games from the PGN file
            while True:
                game = chess.pgn.read_game(pgn_file)
                if game is None:  # end of file
                    break
                
                board = game.board()
                for move in game.mainline_moves():
                    fen_file.write(board.fen() + '\n')
                    board.push(move)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert PGN to FEN')
    
    parser.add_argument('pgn_path', type=str, help='Path to the PGN file')
    parser.add_argument('fen_path', type=str, help='Path to the output FEN file')
    parser.add_argument('-V', '--version', action='version', version=f"%(prog)s {VERSION}")
    
    args = parser.parse_args()

    pgn_to_fen(args.pgn_path, args.fen_path)