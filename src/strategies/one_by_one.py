class OneByOneStrategy:
    def solve(self, task, operations, remaining_result_boards):
        self.max_matches = remaining_result_boards
        sets = [(training_case['input'],
                 training_case['output']) for training_case in task['train']]
        return self.get_paths_for_input_output_set_by_operations(
            sets, operations)

    def get_paths_for_input_output_set_by_operations(self, sets, operations):
        '''
        input: sets of input and output boards, list of operations,
            maximum number of paths returned
        output: list of no more than max_matches paths that transform
            each input from set to its output
        remark: first one path is created, then checked for all input-outputs
            in the set
        '''
        paths = []
        self.matches = 0
        for op1 in operations:
            for result1, args1 in op1.try_run(sets[0][0]):
                if result1 is None:
                    continue
                if result1.equals(sets[0][1]):
                    path = [
                        (op1, args1)
                    ]
                    if self.enough_matches(sets, paths, path):
                        return paths

                for op2 in operations:
                    #if op1 == op2:
                    #    continue
                    for result2, args2 in op2.try_run(result1):
                        if result2 is None:
                            continue
                        if result2.equals(sets[0][1]):
                            path = [
                                (op1, args1),
                                (op2, args2)
                            ]
                            if self.enough_matches(sets, paths, path):
                                return paths
        return paths

    def enough_matches(self, sets, paths, path):
        matched = True
        for i in range(1, len(sets)):
            if not self.is_path_transforming_input_to_output(
                    sets[i][0], sets[i][1], path):
                matched = False
                break
        if matched:
            paths.append(path)
            self.matches += 1
            if self.matches >= self.max_matches:
                return paths

    def is_path_transforming_input_to_output(self, input_board,
                                             output_board, path):
        '''
        input: input board, output board, path for calculation
        output: boolean value stating whether output was achieved from input
            via specified path
        '''
        processed_board = input_board.copy()
        for operation, args in path:
            processed_board = operation.run(processed_board, args)
        if processed_board.equals(output_board):
            return True
        return False
