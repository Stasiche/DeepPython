from typing import List
import os


def generate_latex(data: List[List[str]]) -> str:
    intro = '\\documentclass{article}\n\\begin{document}\n\\begin{center}\n'
    outro = '\\end{center}\n\\end{document}'
    return intro + generate_latex_table(data) + outro


def generate_latex_table(data: List[List[str]]) -> str:
    return '\\begin{tabular}{' + f'{" c " * len(data[0])}' + '}\n' +\
           '\n\\\\\n'.join(map(lambda x: ' & '.join(x), data)) + '\n\\end{tabular}\n'


if __name__ == '__main__':
    os.makedirs('artifacts', exist_ok=True)
    inp = [['l', 'ine', 'one'],
           ['long', 'line', 'second'],
           ['super duper long', 'third', 'line']]
    with open('artifacts/easy.tex', 'w') as f:
        f.write(generate_latex(inp))
