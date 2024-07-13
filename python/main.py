import random
import json

from mapGenerationTest.GenerationTest import mapGenerationTest, test_Widget
from sign_widget.TestSign import signGeneration
from sign_widget.sign import Sign
from signal_widget.TrafficLight import TrafficLight
from func.CalculateSimilarity import calculatesimilarity
from func.CountBasedChoose import CountBasedChoose
from func.GraphSimilarity import GetBaseSimilarity, GraphBaseSimilarity, getMapSize
from func.GraphSimilarityV2 import GraphSimilarity, NodeSimilarityTest, EdgeExceptionCompare, \
    GetImproveSimilarity
from func.printConnection import printConnection
from func.printAuto import printAutoInd
from func.printAsserts import printAsserts
from func.printObjectAssets import printObjectAsserts
from func.widget import Widget
from settings.info import Info
from settings.connectionDict import Widget_Map

from laneswitch_widget.laneswitch import LaneSwitch
from fork_widget.fork import Fork
from straigntlane_widget.straightlane import StraightLane
from Ulane_widget.ulane import ULane
from curve_widget.curve import Curve
from roundabout_widget.roundabout import Roundabout
from Intersection_widget.intersection import Intersection
from TJunction_widget.tJunction import tJunction
from func.Quene import ConnectorQueue
from func.update import update, initialFirstwidget
from func.WidgetGraph import WidgetGraph
import pickle
from func.WidgetGraph import Node
from shapely.geometry import Polygon
from matplotlib import pyplot as plt
import time
import schedule
import generation_test
from generation_test.build_barrier import test_barrier


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


def RandomAlgorithm(Mfile, rrhdfile, pklfile, graphlst, widgetcount):
    rules = Info.COMPILE_RULES
    widgetlist = Info.Widgetlist
    num = Info.WidgetNumber
    parametupdateercount = 0
    widgetupdatecount = 0

    finalMfilename = Mfile
    rrhdfilename = rrhdfile
    pklfilename = pklfile

    encodingFormat = Info.COMPILE_PREF.setdefault("M File Ecoding Format", "GBK")

    with open(finalMfilename, "w", encoding=encodingFormat) as f:
        graph = WidgetGraph()
        # 生成Asserts部分
        printAsserts(f)
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

        printAutoInd(f, '')
        printAutoInd(f, 'plot(rrMap)')
        printAutoInd(f, 'write(rrMap,"' + rrhdfilename + '");')

    print(finalMfilename + " " + "Compile successfully!")
    print('当前组件使用情况')
    print(Info.widgetcount.values())

    graphlst.append(graph)
    save_graph(graph, pklfilename)
    return parametupdateercount, widgetupdatecount


def CountBasedAlgorithm(Mfile, rrhdfile, pklfile, graphlst, widgetcount):
    rules = Info.COMPILE_RULES
    widgetlist = Info.Widgetlist
    num = Info.WidgetNumber
    parametupdateercount = 0
    widgetupdatecount = 0

    finalMfilename = Mfile
    rrhdfilename = rrhdfile
    pklfilename = pklfile

    encodingFormat = Info.COMPILE_PREF.setdefault("M File Ecoding Format", "GBK")

    with open(finalMfilename, "w", encoding=encodingFormat) as f:
        graph = WidgetGraph()
        # 生成Asserts部分
        printAsserts(f)
        # 随机从组件库中选择一个组件，并用rules更新参数。  设置初始点！！！！！！！
        count = 0
        totalCoveredArea = []
        widgetdict = CountBasedChoose(widgetlist, widgetcount)
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
                allwidget4connect1 = Widget_Map.get(connectorType)
                allwidget4connect = allwidget4connect1.copy()
                availableNum = len(allwidget4connect)

                while availableNum > 0:
                    wDict = CountBasedChoose(allwidget4connect, widgetcount)
                    widgetupdatecount += 1
                    dict1 = wDict.copy()
                    dict1['Start'] = connector['endpoint']
                    dict1['K'] = connector['direction']
                    dict1, parametupdateercount = update(dict1, rules, totalCoveredArea, parametupdateercount)
                    if dict1 is not None:
                        break
                    else:
                        allwidget4connect.remove(wDict)
                        availableNum -= 1
                if availableNum == 0:
                    print('该路口没有可以拼接的组件')
                    continue
                else:
                    print('下一个组件的dict')
                    print(dict1)
                    # 生成下一个组件
                    w1 = BuildRoad(dict1)
                    w1.generate_road(f)
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
        printAutoInd(f, '')
        printAutoInd(f, 'plot(rrMap)')
        printAutoInd(f, 'write(rrMap,"' + rrhdfilename + '");')

    print(finalMfilename + " " + "Compile successfully!")
    print('当前组件使用情况')
    print(Info.widgetcount.values())

    graphlst.append(graph)
    save_graph(graph, pklfilename)
    return parametupdateercount, widgetupdatecount


def compile():
    graphlst = []
    global count
    count = 1
    widgetcount = Info.widgetcount
    start_time = time.time()
    # 6小时
    duration = 24 * 60 * 60

    # while count <= 2:
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= duration:
            print('运行时间已到')
            break

        finalMfilename = Info.mFILE_DIRECTORY + Info.mFILE_NAME + str(count) + '.m'
        rrhdfilename = Info.rFILE_DIRECTORY + Info.rFILE_NAME + str(count) + '.rrhd'
        pklfilename = 'python/graph/' + Info.mFILE_NAME + str(count) + '.pkl'
        parametupdateercount, widgetupdatecount = 0, 0
        try:
            parametupdateercount, widgetupdatecount = RandomAlgorithm(finalMfilename, rrhdfilename, pklfilename,
                                                                      graphlst, widgetcount)
            # parametupdateercount, widgetupdatecount = CountBasedAlgorithm(finalMfilename, rrhdfilename, pklfilename,graphlst, widgetcount)
            print('当前地图组件更新次数为：')
            print(widgetupdatecount)
            print('当前地图参数更新次数为：')
            print(parametupdateercount)
            count += 1
        except Exception as e:
            print(e)
            Widget.LaneID = 1  # 组件的起始车道id
            Widget.BoundaryID = 1  # 组件的起始车道边界id
            Widget.JunctionID = 1
            Widget.WidgetID = 1

        Widget.LaneID = 1  # 组件的起始车道id
        Widget.BoundaryID = 1  # 组件的起始车道边界id
        Widget.JunctionID = 1
        Widget.WidgetID = 1
        Info.parameterupdate += parametupdateercount
        Info.widgetupdate += widgetupdatecount
        time.sleep(0.1)

        if len([key for key, value in Info.widgetcount.items() if value == 0]) == 0:
            print('累计使用242种不同组件所耗时间为 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 42:
            print('累计使用200种不同组件所耗时间为 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 92:
            print('累计使用150种不同组件所耗时间为 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 142:
            print('累计使用100种不同组件所耗时间为 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 192:
            print('累计使用50种不同组件所耗时间为 {:.5f} s'.format(time.time() - start_time))

        print('当前已使用的不同组件数为')
        print(len([key for key, value in Info.widgetcount.items() if value != 0]))

        if 30 * 60 <= (time.time() - start_time) < 40 * 60:
            print("累计30分钟:")
            output()
        elif 60 * 60 <= (time.time() - start_time) < 70 * 60:
            print("累计1小时:")
            output()
        elif 120 * 60 <= (time.time() - start_time) < 130 * 60:
            print("累计2小时:")
            output()
        elif 180 * 60 <= (time.time() - start_time) < 190 * 60:
            print("累计3小时:")
            output()
        elif 240 * 60 <= (time.time() - start_time) < 250 * 60:
            print("累计4小时:")
            output()
        elif 300 * 60 <= (time.time() - start_time) < 310 * 60:
            print("累计5小时:")
            output()
        elif 360 * 60 <= (time.time() - start_time) < 370 * 60:
            print("累计6小时:")
            output()
        elif 420 * 60 <= (time.time() - start_time) < 430 * 60:
            print("累计7小时:")
            output()
        elif 480 * 60 <= (time.time() - start_time) < 490 * 60:
            print("累计8小时:")
            output()
        elif 540 * 60 <= (time.time() - start_time) < 550 * 60:
            print("累计9小时:")
            output()
        elif 600 * 60 <= (time.time() - start_time) < 610 * 60:
            print("累计10小时:")
            output()
        elif 660 * 60 <= (time.time() - start_time) < 670 * 60:
            print("累计11小时:")
            output()
        elif 720 * 60 <= (time.time() - start_time) < 730 * 60:
            print("累计12小时:")
            output()
        elif 780 * 60 <= (time.time() - start_time) < 790 * 60:
            print("累计13小时:")
            output()
        elif 840 * 60 <= (time.time() - start_time) < 850 * 60:
            print("累计14小时:")
            output()
        if 900 * 60 <= (time.time() - start_time) < 910 * 60:
            print("累计15小时:")
            output()
        elif 960 * 60 <= (time.time() - start_time) < 970 * 60:
            print("累计16小时:")
            output()
        elif 1020 * 60 <= (time.time() - start_time) < 1030 * 60:
            print("累计17小时:")
            output()
        elif 1080 * 60 <= (time.time() - start_time) < 1090 * 60:
            print("累计18小时:")
            output()
        elif 1140 * 60 <= (time.time() - start_time) < 1150 * 60:
            print("累计19小时:")
            output()
        elif 1200 * 60 <= (time.time() - start_time) < 1210 * 60:
            print("累计20小时:")
            output()
        elif 1260 * 60 <= (time.time() - start_time) < 1270 * 60:
            print("累计21小时:")
            output()
        elif 1320 * 60 <= (time.time() - start_time) < 1330 * 60:
            print("累计22小时:")
            output()
        elif 1380 * 60 <= (time.time() - start_time) < 1390 * 60:
            print("累计23小时:")
            output()
        elif 1440 * 60 <= (time.time() - start_time) < 1450 * 60:
            print("累计24小时:")
            output()


def output():
    print('总计组件搜索次数为')
    print(Info.widgetupdate)
    print('总计参数更新次数为')
    print(Info.parameterupdate)
    print('累计使用的不同组件数为')
    print(len([key for key, value in Info.widgetcount.items() if value != 0]))


def TestException():
    graph_dir = "./data/graph"
    file_dir1 = "graph/AGM12.pkl"
    file_dir2 = "graph/AGM12.pkl"
    # print(GraphSimilarity(file_dir1, file_dir2).NodeSimilarity())
    # print(GraphBaseSimilarity(file_dir1, file_dir2).NodeSimilarity())

    # ==============================================
    # V1相似度方法

    # GetBaseSimilarity(graph_dir,400)
    GetImproveSimilarity(graph_dir, 20)
    # GetSimilarity(graph_dir)

# 测试base拼接方法



if __name__ == '__main__':
    # finalMfilename = Info.mFILE_DIRECTORY + Info.mFILE_NAME + ".m"
    # rrhdfilename = Info.rFILE_DIRECTORY + Info.rFILE_NAME + ".rrhd"
    # RandomAlgorithm(finalMfilename, rrhdfilename)

    # generation_test()
    # compile()
    # TestException()
    # print(getMapSize("data/graph/AGM1.pkl"))
    # calculatesimilarity()
    # GetBaseSimilarity("data/1graph",30)
    # file_dir1 = "graph/AGM1.pkl"
    # file_dir2 = "graph/AGM2.pkl"
    # GraphSimilarity(file_dir1,file_dir2).EdgeSimilarity()
    finalMfilename = '.'.join((Info.mFILE_DIRECTORY + Info.mFILE_NAME).split('.')[:-1]) + ".m"
    rrhdfilename = '.'.join((Info.rFILE_DIRECTORY + Info.rFILE_NAME).split('.')[:-1]) + ".rrhd"
    path = "D:\Desktop\map\Test_data\m_map\\BaseStraightLane.m"
    encodingFormat = Info.COMPILE_PREF.setdefault("M File Ecoding Format", "GBK")
    with open(path, "w", encoding=encodingFormat) as f:
        printAsserts(f)
        printObjectAsserts(f)
        # 测试 ------
        # test_barrier(f)

        # test_Widget(f)
        # 地图拼接
        mapGenerationTest(f)


        # 测试sign
        # signGeneration(f)


        printAutoInd(f, '')
        printAutoInd(f, 'plot(rrMap,ShowStaticObjects=true)')
        printAutoInd(f, 'write(rrMap,"' + "D:\Desktop\\rr\Assets\BaseStraightLane.rrhd" + '");')
        printAutoInd(f,
                     'rrApp = roadrunner(' + '"D:\Desktop\\rr"' + ",InstallationFolder = 'D:\Development\RoadRunner R2023a\\bin\win64');")
        printAutoInd(f, 'importOptions = roadrunnerHDMapImportOptions(ImportStep="Load");')
        printAutoInd(f, 'importScene(rrApp,"D:\Desktop\\rr\Assets\BaseStraightLane.rrhd","RoadRunner HD Map",importOptions);')
        printAutoInd(f, 'buildOptions = roadrunnerHDMapBuildOptions(DetectAsphaltSurfaces=true);')
        printAutoInd(f, 'buildScene(rrApp,"RoadRunner HD Map",buildOptions)')
    print("generation_test.m" + " " + "Compile successfully!")
