import sys


class FirstOnlyStrategy:
    def solve(self, task, operations, remaining_result_boards):
        return self.get_paths_for_input_output_by_operations(
            task['train'][0]['input'],
            task['train'][0]['output'],
            operations, remaining_result_boards)

    def get_paths_for_input_output_by_operations(self,
                                                 input_board,
                                                 output_board,
                                                 operations,
                                                 max_matches=sys.maxsize):
        '''
        input: input and output boards, list of operations,
            maximum number of paths returned
        output: list of no more than max_matches paths that transform
            input board to output
        '''
        paths = []
        matches = 0
        for op1 in operations:
            for result1, args1 in op1.try_run(input_board):
                if result1.equals(output_board):
                    paths.append([
                        (op1, args1)
                    ])
                    matches += 1
                    if matches >= max_matches:
                        return paths
                for op2 in operations:
                    if op1 == op2:
                        continue
                    for result2, args2 in op2.try_run(result1):
                        if result2.equals(output_board):
                            paths.append([
                                (op1, args1),
                                (op2, args2)
                            ])
                            matches += 1
                            if matches >= max_matches:
                                return paths
        return paths
