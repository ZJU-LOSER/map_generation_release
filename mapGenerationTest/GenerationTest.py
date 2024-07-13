import json
import pickle
import random

from Intersection_widget.intersection import Intersection
from TJunction_widget.tJunction import tJunction
from Ulane_widget.ulane import ULane
from barrier_widget.barrier import Barrier
from barrier_widget.barrierType import getMiddleType
from curve_widget.curve import Curve
from fork_widget.fork import Fork
from func.Quene import ConnectorQueue
from func.WidgetGraph import WidgetGraph
from func.printAsserts import printAsserts
from func.printAuto import printAutoInd
from func.printConnection import printConnection
from func.printObjectAssets import printObjectAsserts
from func.update import initialFirstwidget, update
from generating_algorithm.MCMC_algorithm import MCMCAlgorithm
from generation_test.build_barrier import test_barrier
from laneswitch_widget.laneswitch import LaneSwitch
from roundabout_widget.roundabout import Roundabout
from settings.connectionDict import Widget_Map
from settings.info import Info
from straigntlane_widget.straightlane import StraightLane


def RandomAlgorithm(Mfile, rrhdfile, pklfile, graphlst, widgetcount):
    rules = Info.COMPILE_RULES
    widgetlist = Info.Widgetlist
    num = Info.WidgetNumber
    parametupdateercount = 0
    widgetupdatecount = 0

    finalMfilename = Mfile
    rrhdfilename = rrhdfile
    pklfilename = pklfile
    finalMfilename = "D:\Desktop\map\Test_data\m_map\\BaseStraightLane.m"

    encodingFormat = Info.COMPILE_PREF.setdefault("M File Ecoding Format", "GBK")

    with open(finalMfilename, "w", encoding=encodingFormat) as f:
        graph = WidgetGraph()
        # 生成Asserts部分
        printAsserts(f)
        printObjectAsserts(f)
        # 随机从组件库中选择一个组件，并用rules更新参数。  设置初始点！！！！！！！
        count = 0
        totalCoveredArea = []
        widgetdict = random.choice(widgetlist)
        # #参数更新
        print('开始拼接')
        # 设置第一个组件的起点，并且随机设置其方向
        widgetdict0, parametupdateercount = initialFirstwidget(widgetdict, rules, totalCoveredArea,
                                                               parametupdateercount)
        widgetupdatecount += 1
        print('第一个组件的dict')
        print(widgetdict0)
        w0 = BuildRoad(widgetdict0)
        w0.generate_road(f)

        # 添加 barrier 应该放到地图生成后进行添加 这里仅作测试
        test_barrier(f, widgetdict0)

        count += 1
        CoveredArea = w0.get_coveredArea()
        print('该组件占用的空间为')
        print(CoveredArea)
        # 记录已经占用的位置
        totalCoveredArea += CoveredArea
        # 计数该组件使用一次
        widgetcount[json.dumps(widgetdict)] += 1
        # 将第一个点放进图
        id1 = w0.WidgetID
        type1 = widgetdict0.get('Type')
        flag1 = widgetdict0.get('Flag')
        function1 = widgetdict0.setdefault('Function', None)
        direction1 = widgetdict0.setdefault('Direction', None)
        graph.add_node(id1, type1, flag1, function1, direction1)
        ##############
        connectorqueue = ConnectorQueue()
        # 将第一个组件的可拼接点入队
        for i in w0.get_Nexts():
            connectorqueue.enqueue(i)
        del w0
        while count < num and connectorqueue.isempty() is False:
            connector = connectorqueue.dequeue()
            # 随机判断连接点是否连接新组件，flag = 1则拼接。如果是队列最后一个，则必须进行拼接。
            flag = random.randint(0, 1)
            if connectorqueue.isempty() or flag == 1:
                # 根据路口类型获取所有可以拼接的组件列表
                connectorType = connector['type']
                allwidget4connect = Widget_Map.get(connectorType)
                # 将可拼接列表随机打乱
                random.shuffle(allwidget4connect)
                availableNum = len(allwidget4connect)
                n = 0
                for wDict in allwidget4connect:
                    widgetupdatecount += 1
                    dict1 = wDict.copy()
                    dict1['Start'] = connector['endpoint']
                    dict1['K'] = connector['direction']
                    dict1, parametupdateercount = update(dict1, rules, totalCoveredArea, parametupdateercount)
                    if dict1 is not None:
                        break
                    else:
                        n += 1
                        continue
                if n == availableNum:
                    print('该路口没有可以拼接的组件')
                    continue
                else:
                    print('下一个组件的dict')
                    print(dict1)
                    # 生成下一个组件
                    w1 = BuildRoad(dict1)
                    w1.generate_road(f)
                    # 添加 barrier
                    test_barrier(f, dict1)
                    count += 1
                    CoveredArea = w1.get_coveredArea()
                    print('该组件占用的空间为')
                    print(CoveredArea)
                    # 记录已经占用的位置
                    totalCoveredArea += CoveredArea
                    # 计数该组件使用一次
                    widgetcount[json.dumps(wDict)] += 1
                    # 将第一个点放进图，将和上一个组件的边关系入图
                    id2 = w1.WidgetID
                    type2 = dict1.get('Type')
                    flag2 = dict1.get('Flag')
                    function2 = dict1.setdefault('Function', None)
                    direction2 = dict1.setdefault('Direction', None)
                    graph.add_node(id2, type2, flag2, function2, direction2)
                    graph.add_edge(connector['ID'], id2)
                    ##############
                    # 新组件可拼接点入队
                    for i in w1.get_Nexts():
                        connectorqueue.enqueue(i)
                    # 生成道路连接代码
                    if len(connector['lanes']) == len(w1.get_Currents()['CurrentLanes']):
                        printConnection(connector['lanes'], w1.get_Currents()['CurrentLanes'], connectorType, f)
                    del w1
        if count < num:
            print('该地图使用组件数未满足设定值')

        # 输出到RoadRunner场景文件夹
        printAutoInd(f, '')
        printAutoInd(f, 'plot(rrMap,ShowStaticObjects=true)')
        printAutoInd(f, 'write(rrMap,"' + Info.scFILE_DIRECTORY + rrhdfilename.split('/')[-1] + '");')
        printAutoInd(f,
                     'rrApp = roadrunner(' + '"D:\Desktop\\rr"' + ",InstallationFolder = 'D:\Development\RoadRunner R2023a\\bin\win64');")
        printAutoInd(f, 'importOptions = roadrunnerHDMapImportOptions(ImportStep="Load");')
        printAutoInd(f,
                     'importScene(rrApp,"' + Info.scFILE_DIRECTORY + rrhdfilename.split('/')[
                         -1] + '",' + '"RoadRunner HD Map",importOptions);')
        printAutoInd(f, 'buildOptions = roadrunnerHDMapBuildOptions(DetectAsphaltSurfaces=true);')
        printAutoInd(f, 'buildScene(rrApp,"RoadRunner HD Map",buildOptions)')

    print(finalMfilename + " " + "Compile successfully!")
    print('当前组件使用情况')
    print(Info.widgetcount.values())

    graphlst.append(graph)
    save_graph(graph, pklfilename)
    return parametupdateercount, widgetupdatecount


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


def load_graph(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)


def mapGenerationTest(f):
    widgetcount = Info.widgetcount
    graphlst = []
    finalMfilename = Info.mFILE_DIRECTORY + Info.mFILE_NAME + str(1) + '.m'
    rrhdfilename = Info.rFILE_DIRECTORY + Info.rFILE_NAME + str(1) + '.rrhd'
    pklfilename = Info.pFILE_DIRECTORY + Info.mFILE_NAME + str(1) + '.pkl'
    parametupdateercount, widgetupdatecount = RandomAlgorithm(finalMfilename, rrhdfilename, pklfilename,
                                                              graphlst, widgetcount)
    mcmc = MCMCAlgorithm(graphlst, Info.Widgetlist)
    parametupdateercount, widgetupdatecount = mcmc.splicing(finalMfilename, rrhdfilename, pklfilename,
                                                            graphlst, widgetcount)
    print(graphlst[0])


# 测试单个组件
def test_Widget(f):
    Intersectiondict2 = {
        'ID': 1,
        'Start': (0, 0),
        'Width': 4,
        'OuterLaneNumber': [6, 6, 6, 6],
        'InnerLaneNumber': 12,
        'BoundaryNumber': 52,
        'K': '+',
        'Type': 'intersection',
        'Flag': '六车道十字路口'
    }

    Ins = Intersection(Intersectiondict2)
    Ins.generate_road(f)
    barrier_dict = {
        'laneType': Ins.Type,
        # 'boundaryPoint': Widget.getboundarypoint(),
        'sideType': 'HighwayFence',
        'middleType': getMiddleType('HighwayFence'),
        'Flag': Ins.Flag,
    }
    barrier_dict['boundaryPoint'] = Ins.getLaneInfoList()[1]
    barrier = Barrier(barrier_dict)
    barrier.generate_barrier(f)
