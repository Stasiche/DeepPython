import networkx as nx
from typing import Optional
import random


def get_el_name(el):
    return str(type(el)).split('.')[-1][:-2]


class AstParser:
    def __init__(self):
        self.labels = {}
        self.color_map = []
        self.__parser_funcs = {
            'Assign': self.__parse_assign,
            'For': self.__parse_for,
            'Name': self.__parse_name,
            'Constant': self.__parse_constant,
            'List': self.__parse_list,
            'BinOp': self.__parse_binop,
            'Return': self.__parse_return,
            'Expr': self.__parse_expr
        }

    def __parse_binop(self, el):
        return f'Result of\n{get_el_name(el.op)}({el.left.id}, {el.right.id})'

    def __add_edge(self, g, src, label, color):
        dst = str(random.random())
        while self.labels.get(dst, False):
            dst = str(random.random())

        g.add_edge(src, dst)
        self.labels[dst] = label
        self.color_map.append(color)
        return dst

    def __parse_name(self, el):
        return f'varible\n{el.id}'

    def __parse_constant(self, el):
        return f'value\n{el.value}'

    def __parse_expr(self, el, root_name):
        g = nx.MultiGraph()
        list_name = self.__add_edge(g, root_name, 'Expr', 'green')
        el = el.value
        self.__add_edge(g, list_name,
                        f'{el.func.attr} {str(*[self.__parse_name(arg) for arg in el.args])} to {el.func.value.id}', 'green')
        return g

    def __parse_list(self, el, root_name):
        g = nx.MultiGraph()
        list_name = self.__add_edge(g, root_name, 'List', 'blue')
        for const in el.elts:
            self.__add_edge(g, list_name, self.__parse_constant(const), 'blue')
        return g

    def __parse_return(self, el, root_name):
        g_main = nx.MultiGraph()
        ret_name = self.__add_edge(g_main, root_name, 'Return', 'green')
        self.__add_edge(g_main, ret_name, f'{self.__parse_name(el.value)}', 'green')
        return g_main

    def __parse_for(self, root, root_name):
        g_main = nx.MultiGraph()
        for_name = self.__add_edge(g_main, root_name, 'For', 'green')
        for el in root.body:
            g = self.__parser_funcs.get(get_el_name(el))(el, for_name)
            g_main = nx.compose(g_main, g)

        return g_main

    def __parse_assign(self, el, root_name) -> nx.MultiGraph:
        g = nx.MultiGraph()
        assign_name = self.__add_edge(g, root_name, 'Assign', 'green')
        for t, v in zip(el.targets[0].dims, el.value.dims):
            v_name = get_el_name(v)
            if v_name != 'List':
                val = self.__parser_funcs.get(get_el_name(v))(v)
                self.__add_edge(g, assign_name, f'To varible\n{t.id}\nPut\n{val}', 'green')
            else:
                g_tmp = self.__parse_list(v, assign_name)
                g = nx.compose(g, g_tmp)
        return g

    def __call__(self, root) -> Optional[nx.MultiGraph]:
        g_main = nx.MultiGraph()
        root_name = get_el_name(root)
        self.labels[root_name] = root_name
        self.color_map.append('red')
        for el in root.body:
            g = self.__parser_funcs.get(get_el_name(el))
            if g is not None:
                g = g(el, root_name)
                g_main = nx.compose(g_main, g)

        return g_main
