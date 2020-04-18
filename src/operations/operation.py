class Operation:
    @classmethod
    def run_operation(cls, board, args):
        pass

    @classmethod
    def run(cls, board, args):
        board_copy = board.copy()
        board_copy = cls.run_operation(board_copy, args)
        return board_copy.redraw()

    @classmethod
    def gen_args(cls, board):
        pass

    @classmethod
    def try_run(cls, board):
        for args in cls.gen_args(board):
            yield cls.run(board, args), args
