import networkx as nx


# widget_graph 转为networkx图
def widget_graph_to_networkx(widget_graph):
    g = nx.Graph()
    for node in widget_graph.get_nodes():
        g.add_node(node.id, type=node.type, flag=node.flag, function=node.function, direction=node.direction)
    for node, edges in widget_graph.edges.items():
        for edge in edges:
            g.add_edge(node.id, edge[0].id)
    return g


# 地图组件节点匹配规则 type + flag
def node_match(n1, n2):
    return n1['type'] == n2['type'] and n1['flag'] == n2['flag']


# 地图边匹配 不做要求
def edge_match(e1, e2):
    return True


def calculate_graph_edit_distance(G1, G2):
    g1 = widget_graph_to_networkx(G1)
    g2 = widget_graph_to_networkx(G2)
    return nx.graph_edit_distance(g1, g2, node_match=node_match, edge_match=edge_match)


# 计算
def calculate_average_edit_distance(cur_graph, history_graphs):
    global length
    length = len(history_graphs)
    edit_distance = 0
    for history_graph in history_graphs:
        edit_distance += calculate_graph_edit_distance(cur_graph, history_graph)
    return edit_distance / length
