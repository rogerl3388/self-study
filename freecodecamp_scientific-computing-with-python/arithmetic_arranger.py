def arithmetic_arranger(problems: list, show_answers=False) -> str:
    #   Takes a list of strings with basic arithmetic functions (ex. "3 + 5634", "2 - 4")
    #   and formats it into a vertical arrangement. Second input is boolean for if answers should be shown
    big_list = ["","",""]

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        
        if '+' in problem:
            operator = '+'
        else:
            operator = '-'
        problem_parts = problem_splitter(problem, operator =' '+operator+' ')
        # I could technically use .strip() method to account for whether spaces
        # are used in input for 'problem', but decided not to for now

        if max(len(problem_parts[0]), len(problem_parts[1])) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif not (problem_parts[0].isdigit() and problem_parts[1].isdigit()):
            return 'Error: Numbers must only contain digits.'

        extra_space = " " * abs(len(problem_parts[0]) - len(problem_parts[1]))
        if len(problem_parts[0]) > len(problem_parts[1]):
            problem_parts[1] = extra_space + problem_parts[1]
        elif len(problem_parts[0]) < len(problem_parts[1]):
            problem_parts[0] = extra_space + problem_parts[0]
        
        big_list[0] += '  ' + problem_parts[0]
        big_list[1] += operator + ' ' + problem_parts[1]
        
        for _ in range(2 + max(len(problem_parts[0]),len(problem_parts[1]))):
            big_list[2] += '-'

        if show_answers:
            big_list.append("")
            big_list[3] += ' ' * (max(len(problem_parts[0]),len(problem_parts[1])) + 2 - len(str(eval(problem))))
            big_list[3] += str(eval(problem))

        if problem is problems[-1]:
            big_list[0] += '\n'
            big_list[1] += '\n'
            if show_answers:
                big_list[2] += '\n'
        else:
            big_list[0] += '    '
            big_list[1] += '    '
            big_list[2] += '    '
            if show_answers:
                big_list[3] += '    '

    return ''.join(big_list)

def problem_splitter(problem: str, operator: str) -> list:
    return problem.split(operator)

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],show_answers = True)}')