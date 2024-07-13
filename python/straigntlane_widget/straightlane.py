# 直线行道路的输入是一个字典{Start,LW,StartLaneID,LaneNumber,TravelDirection,LaneAssetType,K,Function,Flag}
# 以斜率方向最左侧车道为基准


# 为了方便拼接 后续可以在组件类中集成一个返回该组件结束位置的方法。

from func.printAuto import printAutoInd
from func.widget import Widget
import math


class StraightLane(Widget):
    WidgetID = 1
    Start = (0, 0)  # 道路起始点的坐标
    LW = (10, 3.5)  # (道路的长度，每个车道的宽度)
    StartLaneID = 1  # 组件的起始车道id
    StartBoundaryID = 1  # 组件的起始车道边界id
    LaneNumber = 1  # 该组件一共有多少车道
    BoundaryNumber = 1
    LaneAssetType = {}  # 字典，保存每个车道的车道线种类{BoundaryID:'SSW',...} SW白色实线, DW白色虚线, DSW白色虚实线, SDW白色双实线, SY黄色实线, DY黄色虚线, DSY黄色虚实线, SDY黄色双实线.
    k = '+0'  # 指定该道路的方向。k表示直线的斜率。+0表示水平向右，-0表示水平向左，+表示竖直向上，-表示竖直向下。
    LaneType = 'Driving'  # 默认道路类型都是driving
    Flag = ''  # 组件标记符

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.Start = dict1.get('Start')
        self.LW = dict1.get('LW')
        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.LaneNumber = dict1.get('LaneNumber')
        self.BoundaryNumber = dict1.get('BoundaryNumber')
        self.LaneAssetType = Widget.get_self_LaneAssetType(dict1.get('LaneAssetType'))
        self.k = dict1.get('K')
        self.Flag = dict1.get('Flag')
        self.Type = dict1.get('Type')

    def get_Currents(self):
        Currents_info = {}
        CurrentFlag = self.Flag
        Currents_info["CurrentLanes"] = []  # 初始化返回的CurrentLanes列表
        Currents_info["Flag"] = CurrentFlag  # 设置返回的Flag信息
        if self.BoundaryNumber == 2:  # 只有一条车道，直接返回初始的StartLaneID
            Currents_info["CurrentLanes"].append(self.StartLaneID)
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 3:  # 有两条车道，返回两个LaneID信息
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1])
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 4:  # 有三条车道，返回三个LaneID信息
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self
                                                 .StartLaneID + 2])
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 5:  # 有四条车道，返回三个LaneID信息
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self
                                                 .StartLaneID + 2, self.StartLaneID + 3])
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 7:  # 有六条车道，返回六个LaneID信息
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self
                                                 .StartLaneID + 2, self.StartLaneID + 3, self.StartLaneID + 4,
                                                  self.StartLaneID + 5])
            Currents_info["Type"] = self.Flag
        return Currents_info

    def get_Nexts(self):
        #  返回是哪几条道路参与拼接。

        Nexts = []
        endpoint = (self.Start[0] + self.LW[0], self.Start[1])
        Next = dict()
        Next['direction'] = self.k
        Next['endpoint'] = self.roate_endpoints(endpoint)
        Next['type'] = self.Flag
        Next['lanes'] = list(range(self.StartLaneID, self.StartLaneID + self.LaneNumber))
        Next['current'] = self.Flag + '_' + self.Type
        Next['ID'] = self.WidgetID
        Nexts.append(Next)
        return Nexts

    # 靠近组件起点的左下角顶点开始，逆时针旋转，保存外接矩形的四个点，return [[]]
    def get_coveredArea(self):
        result = []
        point1 = (self.Start[0], self.Start[1] - self.LW[1] * (self.LaneNumber - 1) - self.LW[1] / 2)
        point2 = (self.Start[0] + self.LW[0], self.Start[1] - self.LW[1] * (self.LaneNumber - 1) - self.LW[1] / 2)
        point3 = (self.Start[0] + self.LW[0], self.Start[1] + self.LW[1] / 2)
        point4 = (self.Start[0], self.Start[1] + self.LW[1] / 2)
        result.append(point1)
        result.append(point2)
        result.append(point3)
        result.append(point4)

        tmp = [result]
        finalResult = self.rotation(tmp)
        return (finalResult)

    def roate_endpoints(self, point):
        if self.k == '+0':
            return point
        if self.k == '-':  # 绕start顺时针旋转90度
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi / 2)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi / 2)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi / 2)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi / 2)) + self.Start[1]))
            return x, y
        if self.k == '-0':  # 绕start顺时针旋转180度
            x = float(
                '{:.3f}'.format((point[0] - self.Start[0]) * int(math.cos(math.pi)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi)) + self.Start[0]))
            y = float(
                '{:.3f}'.format((point[1] - self.Start[1]) * int(math.cos(math.pi)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi)) + self.Start[1]))
            return x, y
        if self.k == '+':  # 绕start顺时针旋转270度
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi * 1.5)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi * 1.5)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi * 1.5)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi * 1.5)) + self.Start[1]))
            return x, y

    def rotation(self, pointlist):
        if self.k == '+0':
            return pointlist
        if self.k == '-':  # 绕start顺时针旋转90度
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float('{:.3f}'.format(
                        (j[0] - self.Start[0]) * int(math.cos(math.pi / 2)) + (j[1] - self.Start[1]) * int(
                            math.sin(math.pi / 2)) + self.Start[0]))
                    y = float('{:.3f}'.format(
                        (j[1] - self.Start[1]) * int(math.cos(math.pi / 2)) - (j[0] - self.Start[0]) * int(
                            math.sin(math.pi / 2)) + self.Start[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == '-0':  # 绕start顺时针旋转180度
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float(
                        '{:.3f}'.format((j[0] - self.Start[0]) * int(math.cos(math.pi)) + (j[1] - self.Start[1]) * int(
                            math.sin(math.pi)) + self.Start[0]))
                    y = float(
                        '{:.3f}'.format((j[1] - self.Start[1]) * int(math.cos(math.pi)) - (j[0] - self.Start[0]) * int(
                            math.sin(math.pi)) + self.Start[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == '+':  # 绕start顺时针旋转270度
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float('{:.3f}'.format(
                        (j[0] - self.Start[0]) * int(math.cos(math.pi * 1.5)) + (j[1] - self.Start[1]) * int(
                            math.sin(math.pi * 1.5)) + self.Start[0]))
                    y = float('{:.3f}'.format(
                        (j[1] - self.Start[1]) * int(math.cos(math.pi * 1.5)) - (j[0] - self.Start[0]) * int(
                            math.sin(math.pi * 1.5)) + self.Start[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        else:
            print('The function is wrong')

    def getlanepoint(self):
        pointlist = []
        flag = self.Flag

        point1 = self.Start
        point2 = (self.Start[0] + self.LW[0] / 2, self.Start[1])
        point3 = (self.Start[0] + self.LW[0], self.Start[1])
        lane1 = [point1, point2, point3]
        pointlist.append(lane1)
        for i in range(self.LaneNumber - 1):
            point1 = (point1[0], point1[1] - self.LW[1])
            point2 = (point2[0], point2[1] - self.LW[1])
            point3 = (point3[0], point3[1] - self.LW[1])
            lane = [point1, point2, point3]
            pointlist.append(lane)
        pointlist = self.rotation(pointlist)

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线线双行道':
            pointlist = pointlist
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            pointlist[0].reverse()
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            pointlist[0].reverse()
        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()

        return pointlist

    def generate_barrier(self, f):
        # 获取boundaries的坐标，生成护栏
        BoundariesPoints = self.getboundarypoint()
        BoundariesNumber = len(BoundariesPoints)
        printAutoInd(f, "% Here is Barrier")
        printAutoInd(f, 'rrMap.Barriers(' + str(BoundariesNumber) + ',1) = roadrunner.hdmap.Barrier;')  # 定义护栏的个数
        for i in range(1, BoundariesNumber + 1):
            if i != 1 and i != BoundariesNumber:
                continue
            printAutoInd(f, 'rrMap.Barriers(' + str(
                i) + ').BarrierTypeReference = roadrunner.hdmap.Reference(ID="FShapeBarrier");')
            printAutoInd(f, 'rrMap.Barriers(' + str(i) + ").ID = strcat('Barrier',num2str(" + str(i) + "));")
            printAutoInd(f, 'rrMap.Barriers(' + str(i) + ').Geometry = ' + self.PointtoString(BoundariesPoints).split(',')[i - 1] +';')
        return

    def getboundarypoint(self):
        pointlist = []
        flag = self.Flag

        point1 = (self.Start[0], self.Start[1] + self.LW[1] / 2)
        point2 = (self.Start[0] + self.LW[0] / 2, self.Start[1] + self.LW[1] / 2)
        point3 = (self.Start[0] + self.LW[0], self.Start[1] + self.LW[1] / 2)
        lane1 = [point1, point2, point3]
        pointlist.append(lane1)
        for i in range(self.LaneNumber):  # 直线道路组件车道边界数=车道数+1
            point1 = (point1[0], point1[1] - self.LW[1])
            point2 = (point2[0], point2[1] - self.LW[1])
            point3 = (point3[0], point3[1] - self.LW[1])
            lane = [point1, point2, point3]
            pointlist.append(lane)

        pointlist = self.rotation(pointlist)

        if flag == '单行道' or flag == '单向双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道':
            pointlist = pointlist
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            pointlist[0].reverse()
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            pointlist[0].reverse()
        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()

        return pointlist

    def PointtoString(self, lst):
        # [[(-1.5, 0), (-1.5, 5.0), (-1.5, 10)], [(1.5, 0), (1.5, 5.0), (1.5, 10)]] 变成 [-1.5 0;-1.5 5.0;-1.5 10],[1.5 0;1.5 5.0;1.5 10]的字符串
        lst = [str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string

    def generate_road(self, f):
        Widget.LaneID += self.LaneNumber
        Widget.BoundaryID += self.BoundaryNumber
        Widget.WidgetID += 1

        flag = self.Flag
        # lane
        lanes = str(self.StartLaneID) + ':' + str(self.StartLaneID + self.LaneNumber - 1)  # 当前直线路段组件涉及到的lane
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a StraightRoad widget.')
        printAutoInd(f, '% Set the lanes.')
        for lane in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
            printAutoInd(f, 'rrMap.Lanes(' + str(lane) + ') = roadrunner.hdmap.Lane();')
        laneidlist = []
        for i in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
            laneidlist.append('Lane' + str(i))
        laneid = ','.join(['"' + i + '"' for i in laneidlist])
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').ID] = deal(' + laneid + ');')
        lanepointlist = self.getlanepoint()
        lanepointstring = self.PointtoString(lanepointlist)
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').Geometry] = deal(' + lanepointstring + ');')
        # 获取每个lane的行驶方向 依旧是以最左侧车道为基准
        # traveldirectionlist=[]
        # for lane in laneidlist:
        #     s = self.TravelDirection.setdefault(lane,'Bidirectional') # 默认车道是双向行驶的
        #     traveldirectionlist.append(s)
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').TravelDirection] = deal("Forward");')
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').LaneType] = deal("Driving");')
        # boundary
        boundaries = str(self.StartBoundaryID) + ':' + str(self.StartBoundaryID + self.LaneNumber)  # 直线道路组件车道边界数=车道数+1
        printAutoInd(f, '% Set the lane boundaries.')
        for boundary in range(self.StartBoundaryID, self.StartBoundaryID + self.LaneNumber + 1):
            printAutoInd(f, 'rrMap.LaneBoundaries(' + str(boundary) + ') = roadrunner.hdmap.LaneBoundary();')
        laneboundaryidlist = []
        for i in range(self.StartBoundaryID, self.StartBoundaryID + self.LaneNumber + 1):
            laneboundaryidlist.append('Boundary' + str(i))
        boundaryid = ','.join(['"' + i + '"' for i in laneboundaryidlist])
        printAutoInd(f, '[rrMap.LaneBoundaries(' + boundaries + ').ID] = deal(' + boundaryid + ');')
        boundarypointlist = self.getboundarypoint()
        boundarypointstring = self.PointtoString(boundarypointlist)
        printAutoInd(f, '[rrMap.LaneBoundaries(' + boundaries + ').Geometry] = deal(' + boundarypointstring + ');')
        # 设置车道边界线的类型
        parametricattributelist = []
        for laneboundary in laneboundaryidlist:
            s = self.LaneAssetType.setdefault(laneboundary, 'SW')
            parametricattributelist.append(s)
        laneassetlist = []
        for i in parametricattributelist:
            if i == 'SW':
                laneassetlist.append('markingAttribSW')
            if i == 'SY':
                laneassetlist.append('markingAttribSY')
            if i == 'DW':
                laneassetlist.append('markingAttribDW')
            if i == 'DY':
                laneassetlist.append('markingAttribDY')
            if i == 'DSW':
                laneassetlist.append('markingAttribDSW')
            if i == 'DSY':
                laneassetlist.append('markingAttribDSY')
            if i == 'SDW':
                laneassetlist.append('markingAttribSDW')
            if i == 'SDY':
                laneassetlist.append('markingAttribSDY')
        laneasset = ','.join(laneassetlist)
        printAutoInd(f, '[rrMap.LaneBoundaries(' + boundaries + ').ParametricAttributes] = deal(' + laneasset + ');')
        # 关联lane 与lane boundaries
        printAutoInd(f, '% Associate lanes and lane boundaries.')
        k = 0  # 用来计数boundary

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线线双行道' or flag == '单向实线双行道':
            for i in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
                printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k] + '",Alignment="Forward");')
                printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k + 1] + '",Alignment="Forward");')
                k = k + 1
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')

        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')

        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')

        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')

        printAutoInd(f, '% End of this widget')

        # 生成barrier
        # self.generate_barrier(f)
