import json
import pickle
import random

from Intersection_widget.intersection import Intersection
from TJunction_widget.tJunction import tJunction
from Ulane_widget.ulane import ULane
from curve_widget.curve import Curve
from fork_widget.fork import Fork
from func.Quene import ConnectorQueue
from func.WidgetGraph import WidgetGraph
from func.printAsserts import printAsserts
from func.printAuto import printAutoInd
from func.printConnection import printConnection
from func.update import initialFirstwidget, update
from generating_algorithm.data_structure import str_dic_mapping
from generating_algorithm.diversity_assessment import calculate_average_edit_distance
from laneswitch_widget.laneswitch import LaneSwitch
from roundabout_widget.roundabout import Roundabout
from settings.connectionDict import Widget_Map
from settings.info import Info
from collections import defaultdict, Counter

from straigntlane_widget.straightlane import StraightLane


def BuildRoad(widgetdict):
    type = widgetdict.get('Type')
    w = None
    if type == 'straightlane':
        w = StraightLane(widgetdict)
    elif type == 'ulane':
        w = ULane(widgetdict)
    elif type == 'curve':
        w = Curve(widgetdict)
    elif type == 'fork':
        w = Fork(widgetdict)
    elif type == 'laneswitch':
        w = LaneSwitch(widgetdict)
    elif type == 'intersection':
        w = Intersection(widgetdict)
    elif type == 'tJunction':
        w = tJunction(widgetdict)
    elif type == 'roundabout':
        w = Roundabout(widgetdict)
    return w


def save_graph(graph, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(graph, file)


class MCMCAlgorithm:
    history_maps = []  # 历史地图数据
    count_matrix = defaultdict(Counter)  # 计数矩阵
    transition_matrix = defaultdict(Counter)  # 概率转移矩阵
    widget_num = Info.WidgetNumber
    batch = 50  #
    encodingFormat = 0
    widgetlist = Info.Widgetlist
    rules = Info.COMPILE_RULES
    parametupdateercount = 0  # 参数更新次数
    widgetupdatecount = 0  # 组件更新次数

    # 初始化
    def __init__(self, history_maps, Widgetlist):
        self.encodingFormat = Info.COMPILE_PREF.setdefault("M File Ecoding Format", "GBK")
        self.history_maps = history_maps
        # for widget in Widgetlist:
        #     widget_info = widget.get('Type') + '_' + widget.get('Flag')
        #     # 获得此时的flag，寻找对应拼接组件的列表
        #     widget_flag = widget.get('Flag')
        #     print('widget_flag = ')
        #     print(widget_flag)
        #     connect_list = Widget_Map.get(widget_flag)
        #     for next_widget in connect_list:
        #         next_widget_info = next_widget.get('Type') + '_' + next_widget.get('Flag')
        #         self.count_matrix[widget_info][next_widget_info] = 0  # 初始化组件转移次数矩阵
        #         self.transition_matrix[widget_info][next_widget_info] = 0  # 初始化概率转移矩阵
        for widget in Widgetlist:
            Widget = BuildRoad(widget)
            widget_info = widget.get('Type') + '_' + widget.get('Flag')
            next_list = Widget.get_Nexts()
            # 获得此时的flag，寻找对应拼接组件的列表
            widget_flag = widget.get('Flag')
            # print('widget_flag = ')
            # print(widget_flag)
            next_type_set = set()
            for next_info in next_list:
                next_type = next_info.get('type')
                if next_type not in next_type_set:
                    next_type_set.add(next_info.get('type'))
                    connect_list = Widget_Map.get(next_type)
                    for next_widget in connect_list:
                        next_widget_info = next_widget.get('Type') + '_' + next_widget.get('Flag')
                        self.count_matrix[widget_info][next_widget_info] = 0  # 初始化组件转移次数矩阵
                        self.transition_matrix[widget_info][next_widget_info] = 0  # 初始化概率转移矩阵

    # 更新概率转移矩阵和转移次数矩阵
    def count_matrix_time(self):
        for graph in self.history_maps:
            for node in graph.get_nodes():
                current_component = f"{node.type}_{node.flag}"
                for edge in graph.graph.edges[node]:
                    next_component = f"{edge[0].type}_{edge[0].flag}"
                    self.count_matrix[current_component][next_component] += 1

        # 计算转移的概率
        for current_component, next_components in self.count_matrix.items():
            total_transitions = sum(next_components.values())
            for next_component in next_components:
                self.transition_matrix[current_component][next_component] = int(
                    self.count_matrix[current_component][next_component] / total_transitions)

    # 每生成一定批次的地图，更新对应的矩阵信息

    def choose_new_component(self, current_component, current_state, history_states, rejected_components):
        print("current_component = ", current_component)
        next_components = self.transition_matrix[current_component]
        print("next_components = ", next_components)
        # 分离下一个可能拼接的组件与对应的概率
        components, probabilities = zip(*next_components.items())
        # 过滤之前选择过的
        filtered_components = []
        filtered_probabilities = []
        for component, probability in zip(components, probabilities):
            if component not in rejected_components:
                filtered_components.append(component)
                filtered_probabilities.append(probability)
        if len(filtered_components) == 0:
            return 'empty'
        # 计算逆转移概率
        inverse_probabilities = [1 - prob for prob in filtered_probabilities]
        # 计算编辑距离奖励
        diversity_rewards = []
        for component in filtered_components:
            new_component_type, new_component_flag = component.split('_')
            new_component_id = len(current_state.get_nodes()) + 1
            # 初始化新的地图 构建候选态
            new_state = WidgetGraph()
            new_state.nodes = current_state.nodes.copy()
            new_state.edges = current_state.edges.copy()
            new_state.add_node(new_component_id, new_component_type, new_component_flag, 'function', 'direction')
            diversity_reward = calculate_average_edit_distance(new_state, history_states)
            diversity_rewards.append(diversity_reward)

        # 归一化
        max_diversity_reward = max(diversity_rewards)
        normalized_diversity_rewards = [reward / max_diversity_reward for reward in diversity_rewards]

        # 结合逆转移概率和编辑距离奖励
        combined_scores = [inv_prob * diversity_reward for inv_prob, diversity_reward in
                           zip(inverse_probabilities, normalized_diversity_rewards)]

        # 加权随机选择
        next_component = random.choices(filtered_components, weights=combined_scores)[0]

        return next_component

    def getDictByStr(self, component_str):
        # 通过组件类型字符串找到对应的字典
        component_type = component_str.split('_')[0]
        component_flag = component_str.split('_')[1]
        ret_dict = str_dic_mapping.get(component_type).get(component_flag)
        print("匹配到的组件字典为:", ret_dict)
        return ret_dict

        # 循环选择组件直到拼接成功，并在失败时更新拒绝列表

    def propose_new_state_with_retries(self, current_state, current_component, transition_matrix, history_states,
                                       connectorList, rules, totalCoveredArea, parametupdateercount):
        global new_component_dict
        global connector
        current_component = current_component
        rejected_components = set()
        flag = True
        while True:
            new_component_str = self.choose_new_component(current_component, current_state, self.history_maps,
                                                          rejected_components)
            if new_component_str == 'empty':
                print('该路口没有可以拼接的组件')
                flag = False
                break
            print("mcmc选中的下一个组件类型为{}".format(new_component_str))
            new_component_type = new_component_str.split('_')[0]
            new_component_flag = new_component_str.split('_')[1]
            new_component_dict = self.getDictByStr(new_component_str).copy()
            # 确定选出来的组件可以拼在哪个拼接点上
            if len(connectorList) == 1:
                connector = connectorList[0]
            else:
                for conn in connectorList:
                    connectorType = conn['type']
                    allwidget4connect = Widget_Map.get(connectorType)
                    if new_component_dict in allwidget4connect:
                        connector = conn
                        break
                    else:
                        continue
            new_component_dict['Start'] = connector['endpoint']
            new_component_dict['K'] = connector['direction']
            new_component_dict, parametupdateercount = update(new_component_dict, rules, totalCoveredArea,
                                                              parametupdateercount)
            if new_component_dict is not None:
                break
            else:
                rejected_components.add(new_component_str)
                continue
        return new_component_dict, flag, connector['type']

    def splicing(self, Mfile, rrhdfile, pklfile, graphlst, widgetcount):
        with open(Mfile, "w", encoding=self.encodingFormat) as f:
            print("======================= 开始mcmc拼接 =======================")
            # 初始化当前的地图，默认初始化为空
            graph = WidgetGraph()
            # 生成Assert部分
            printAsserts(f)
            # 随机从组件库中选择一个组件，并用rules更新参数。  设置初始点！！！！！！！
            count = 0
            totalCoveredArea = []
            widgetdict = random.choice(self.widgetlist)
            print('开始拼接')
            # 设置第一个组件的起点，并且随机设置其方向
            widgetdict0, parametupdateercount = initialFirstwidget(widgetdict, self.rules, totalCoveredArea,
                                                                   self.parametupdateercount)
            self.widgetupdatecount += 1  # 组件更新次数+1
            print("第一个组件的dict")
            print(widgetdict0)
            w0 = BuildRoad(widgetdict0)
            w0.generate_road(f)
            count += 1
            CoveredArea = w0.get_coveredArea()
            print('该组件占用的空间为')
            print(CoveredArea)
            # 记录已经占用的位置
            totalCoveredArea += CoveredArea
            # 计数该组件使用一次
            # widgetcount[json.dumps(widgetdict)] += 1
            # 将第一个点放进图
            id1 = w0.WidgetID
            type1 = widgetdict0.get('Type')
            flag1 = widgetdict0.get('Flag')
            function1 = widgetdict0.setdefault('Function', None)
            direction1 = widgetdict0.setdefault('Direction', None)
            graph.add_node(id1, type1, flag1, function1, direction1)
            current_component = type1 + '_' + flag1  # 记录当前拼接的最后一个组件
            connectorqueue = ConnectorQueue()
            # 将第一个组件的可拼接点入队
            # for i in w0.get_Nexts():
            #     connectorqueue.enqueue(i)
            connectorqueue.enqueue(w0.get_Nexts())
            del w0
            while count < self.widget_num and connectorqueue.isempty() is False:
                connectorList = connectorqueue.dequeue()  # 取出上一个组件可拼接点列表
                # connectorType = connector['type']
                # allwidget4connect = Widget_Map.get(connectorType)
                # availableNum = len(allwidget4connect)
                next_component_dict, flag, connectorType = self.propose_new_state_with_retries(graph, current_component,
                                                                                               self.transition_matrix,
                                                                                               self.history_maps,
                                                                                               connectorList,
                                                                                               self.rules,
                                                                                               totalCoveredArea,
                                                                                               parametupdateercount)
                if flag is False:
                    print('该路口没有可以拼接的组件')
                    continue
                else:
                    print('下一个组件的dict')
                    print(next_component_dict)
                    # 生成下一个组件
                    w1 = BuildRoad(next_component_dict)
                    w1.generate_road(f)
                    count += 1  # 已拼接组件数+1
                    CoveredArea = w1.get_coveredArea()
                    print('该组件占用的空间为')
                    print(CoveredArea)
                    # 记录已经占用的位置
                    totalCoveredArea += CoveredArea
                    id2 = w1.WidgetID
                    type2 = next_component_dict.get('Type')
                    flag2 = next_component_dict.get('Flag')
                    current_component = type2 + '_' + flag2
                    function2 = next_component_dict.setdefault('Function', None)
                    direction2 = next_component_dict.setdefault('Direction', None)
                    graph.add_node(id2, type2, flag2, function2, direction2)
                    graph.add_edge(connector['ID'], id2)
                    ##############
                    # 新组件可拼接点入队
                    # for i in w1.get_Nexts():
                    #     connectorqueue.enqueue(i)
                    connectorqueue.enqueue(w1.get_Nexts())
                    # 生成道路连接代码
                    if len(connector['lanes']) == len(w1.get_Currents()['CurrentLanes']):
                        printConnection(connector['lanes'], w1.get_Currents()['CurrentLanes'], connectorType, f)
                    del w1

            if count < self.widget_num:
                print('该地图使用组件数未满足设定值')
            printAutoInd(f, '')
            printAutoInd(f, 'plot(rrMap)')
            printAutoInd(f, 'write(rrMap,"' + rrhdfile + '");')
        print(Mfile + " " + "Compile successfully!")
        print('当前组件使用情况')
        print(Info.widgetcount.values())
        graphlst.append(graph)
        save_graph(graph, pklfile)
        return 1, 1


print(len(Info.Widgetlist))
