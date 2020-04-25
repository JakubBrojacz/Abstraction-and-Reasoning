class Operation:
    @classmethod
    def run_operation(cls, board, elements, args):
        pass

    @classmethod
    def run(cls, board, args):
        board_copy = board.copy()
        board_copy = cls.run_operation(board_copy,
                                       board_copy.element_group,
                                       args)
        if board_copy is None:
            return None
        return board_copy.redraw()

    @classmethod
    def gen_args(cls, board, elements):
        pass

    @classmethod
    def try_run(cls, board):
        for args in cls.gen_args(board, board.element_group):
            yield cls.run(board, args), args
