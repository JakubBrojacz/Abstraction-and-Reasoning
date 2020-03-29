class Operation:
    @classmethod
    def run(cls, board, args):
        pass

    @classmethod
    def gen_args(cls, board):
        pass

    @classmethod
    def try_run(cls, board):
        for args in cls.gen_args(board):
            yield cls.run(board, args), args
