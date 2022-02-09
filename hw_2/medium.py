from stasiche_hw2 import main
from pdflatex import PDFLaTeX
from easy import generate_latex_table
from typing import List
import os
import shutil

def create_image_tabel_latex(image_name: str, data: List[List[str]]):
    intro = '\\documentclass{article}\n\\usepackage{graphicx}\n\\graphicspath{ {./artifacts/} }' \
            '\n\\begin{document}\n\\begin{center}\n'
    table = generate_latex_table(data)
    image = '\\includegraphics[width=\\textwidth]{' + image_name + '}'
    outro = '\\end{center}\n\\end{document}'

    return intro + table + image + outro


if __name__ == '__main__':
    os.makedirs('artifacts', exist_ok=True)
    inp = [['l', 'ine', 'one'],
           ['long', 'line', 'second'],
           ['super duper long', 'third', 'line']]
    with open('artifacts/medium.tex', 'w') as f:
        f.write(create_image_tabel_latex('res.png', inp))
    pdfl = PDFLaTeX.from_texfile('artifacts/medium.tex')
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True)
    os.remove('artifacts/medium.tex')
    os.remove('artifacts/res.png')
    shutil.move('medium.pdf', 'artifacts/medium.pdf')
