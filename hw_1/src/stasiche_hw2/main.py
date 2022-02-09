import ast
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import os
from .utils import fib
from .utils import hierarchy_pos
from .ast_parser import AstParser

os.makedirs('artifacts', exist_ok=True)
p = AstParser()
g = p(ast.parse(inspect.getsource(fib)).body[0])

fig, ax = plt.subplots(figsize=(12, 8))
pos = hierarchy_pos(g, 'FunctionDef')
# color_map = ['red' if node == 'FunctionDef' else 'green' for node in g]
nx.draw(g, ax=ax, pos=pos, with_labels=True, labels=p.labels, node_color=p.color_map, font_size=10)

# fig.show()
fig.savefig('artifacts/res.png')


