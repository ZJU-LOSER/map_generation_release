from func.Object import Object
from func.printAuto import printAutoInd


class Barrier(Object):
    laneType = 'straightlane'
    barrierType = ''
    sideType = '' # 两侧barrier类型
    middleType = '' # 道路中央barrier类型
    barrierPointList = []
    boundaryPointList = []
    optionDict = {
        'Side': '1',
        'Middle': '1',
        'other': []
    }
    laneFlag = "" # 定义车道类型
    special_barrier = [] # 针对Tjunction

    def __init__(self, dict):
        self.laneType = dict.get('laneType')
        # self.barrierType = dict.get('barrierType')
        self.middleType = dict.get('middleType')
        self.sideType = dict.get('sideType')
        self.laneFlag = dict.get('Flag')
        self.boundaryPointList = dict.get('boundaryPoint')
        if self.laneType == 'tJunction':
            self.special_barrier = dict.get('specialBarrier')


    def getID(self):
        global ID
        ID = Object.Barrier
        Object.Barrier += 1
        return ID

    def PointtoString(self, lst):
        # [[(-1.5, 0), (-1.5, 5.0), (-1.5, 10)], [(1.5, 0), (1.5, 5.0), (1.5, 10)]] 变成 [-1.5 0;-1.5 5.0;-1.5 10],[1.5 0;1.5 5.0;1.5 10]的字符串
        lst = [str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string

    def toStr(self, lst):
        #  [(-1.5, 0), (-1.5, 5.0), (-1.5, 10)] 变成 [-1.5 0;-1.5 5.0;-1.5 10]
        lst = [str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ';'.join(lst)
        return '[' + string + ']'

    def baseBarrier(self, f, Geometry, Type, FlipLaterally):
        # 根据坐标和护栏类型，添加一段护栏
        nowID = self.getID()
        printAutoInd(f, 'rrMap.Barriers(' + str(nowID) + ') = roadrunner.hdmap.Barrier;')
        printAutoInd(f, 'rrMap.Barriers(' + str(nowID) + ').BarrierTypeReference = ' + str(
            Type) + '_Ref;')
        printAutoInd(f,
                     'rrMap.Barriers(' + str(nowID) + ').ID = strcat("Barrier",num2str(' + str(nowID) + '));')
        printAutoInd(f, 'rrMap.Barriers(' + str(nowID) + ').Geometry = ' + self.toStr(Geometry) + ';')
        if FlipLaterally == True:
            printAutoInd(f, 'rrMap.Barriers(' + str(nowID) + ').FlipLaterally = true;')
        if not FlipLaterally:
            printAutoInd(f, 'rrMap.Barriers(' + str(nowID) + ').FlipLaterally = false;')

    def generate_barrier(self, f):
        printAutoInd(f, "% generate Barrier...")
        # 如果是直线道路和曲线道路，则可选择在两侧或者中间边界处添加护栏
        if self.laneType == 'straightlane' or self.laneType == 'curve':
            leftboundary = self.boundaryPointList[0]
            rightboundary = self.boundaryPointList[-1]

            if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                if self.laneFlag in ['单行道','单向虚线双行道','单向实线双行道','单向虚实线双行道','单向双实线双行道']:
                    # 左侧护栏
                    self.baseBarrier(f, leftboundary, self.sideType, True)
                    # 右侧护栏
                    self.baseBarrier(f, rightboundary, self.sideType, False)
                else:
                # if self.laneFlag in ['双向虚线双行道','双向实线双行道','双向虚实线双行道','双向双实线双行道','一前行虚白线虚黄线三行道']:
                    # 左侧护栏
                    self.baseBarrier(f, leftboundary, self.sideType, False)
                    # 右侧护栏
                    self.baseBarrier(f, rightboundary, self.sideType, False)

                if self.optionDict.get('Middle') == '1':  # 需要添加护栏
                    if self.laneFlag == '双向实线双行道' or self.laneFlag == '双向双实线双行道':
                        middleboundary = self.boundaryPointList[1]
                        self.baseBarrier(f, middleboundary, self.middleType, False)
                    if self.laneFlag in ['双黄实线虚虚四车道','双黄实线实实四车道','双黄实线虚实四车道','双黄实线实虚四车道']:
                        middleboundary = self.boundaryPointList[2]
                        self.baseBarrier(f, middleboundary, self.middleType, False)
                    if self.laneFlag in ['双实线虚虚虚虚六车道','双实线实实实实六车道','双实线虚虚实实六车道']:
                        middleboundary = self.boundaryPointList[3]
                        self.baseBarrier(f, middleboundary, self.middleType, False)



            # if self.optionDict.get('Middle') == '1': # 需要添加护栏
            #     if self.laneFlag == '双向实线双行道':
            #         middleboundary = self.boundaryPointList[0]
            #         self.baseBarrier(f, middleboundary, self.barrierType, False)

            # if self.optionDict.get('Middle') == '1':  # 添加中间的护栏
            #     self.baseBarrier(f, middleboundary, self.barrierType, True)

            # 有额外的护栏需要添加如下....

        # U型道路添加护栏
        if self.laneType == 'ulane':
            if "单行道" in self.laneFlag:
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[2]
                leftboundary3 = self.boundaryPointList[4]
                rightboundary1 = self.boundaryPointList[1]
                rightboundary2 = self.boundaryPointList[3]
                rightboundary3 = self.boundaryPointList[5]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f,leftboundary1,self.sideType,True)
                    self.baseBarrier(f, leftboundary2, self.sideType, True)
                    self.baseBarrier(f, leftboundary3, self.sideType, True)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)

            if "双行道" in self.laneFlag:
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[3]
                leftboundary3 = self.boundaryPointList[6]
                rightboundary1 = self.boundaryPointList[2]
                rightboundary2 = self.boundaryPointList[5]
                rightboundary3 = self.boundaryPointList[8]
                middleboundary1 = self.boundaryPointList[1]
                middleboundary2 = self.boundaryPointList[4]
                middleboundary3 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, True)
                    self.baseBarrier(f, leftboundary2, self.sideType, True)
                    self.baseBarrier(f, leftboundary3, self.sideType, True)

                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)

                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

            if "三行道" in self.laneFlag:
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[4]
                leftboundary3 = self.boundaryPointList[8]
                rightboundary1 = self.boundaryPointList[3]
                rightboundary2 = self.boundaryPointList[7]
                rightboundary3 = self.boundaryPointList[11]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f,leftboundary1,self.sideType,False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)

            if "四车道" in self.laneFlag:
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[5]
                leftboundary3 = self.boundaryPointList[10]
                rightboundary1 = self.boundaryPointList[4]
                rightboundary2 = self.boundaryPointList[9]
                rightboundary3 = self.boundaryPointList[14]
                middleboundary1 = self.boundaryPointList[2]
                middleboundary2 = self.boundaryPointList[7]
                middleboundary3 = self.boundaryPointList[12]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f,leftboundary1,self.sideType,False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)

                if self.optionDict.get('Middle') == '1': # 添加中间边界护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

            if "六车道" in self.laneFlag:
                leftboundary1 = self.boundaryPointList[6]
                leftboundary2 = self.boundaryPointList[13]
                leftboundary3 = self.boundaryPointList[20]
                rightboundary1 = self.boundaryPointList[0]
                rightboundary2 = self.boundaryPointList[7]
                rightboundary3 = self.boundaryPointList[14]
                middleboundary1 = self.boundaryPointList[3]
                middleboundary2 = self.boundaryPointList[10]
                middleboundary3 = self.boundaryPointList[17]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f,leftboundary1,self.sideType,False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)

                if self.optionDict.get('Middle') == '1': # 添加中间边界护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)
        # Laneswitch型道路添加护栏
        if self.laneType == 'laneswitch':
            if self.laneFlag == '1*2左' or self.laneFlag == '1*2右':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[2]
                leftboundary3 = self.boundaryPointList[5]
                rightboundary1 = self.boundaryPointList[1]
                rightboundary2 = self.boundaryPointList[4]
                rightboundary3 = self.boundaryPointList[7]
                middleboundary1 = self.boundaryPointList[6]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, True)
                    self.baseBarrier(f, leftboundary2, self.sideType, True)
                    self.baseBarrier(f, leftboundary3, self.sideType, True)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1': # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f,middleboundary1,self.middleType,True)

            if self.laneFlag == '2*1左' or self.laneFlag == '2*1右':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[3]
                leftboundary3 = self.boundaryPointList[6]
                rightboundary1 = self.boundaryPointList[2]
                rightboundary2 = self.boundaryPointList[5]
                rightboundary3 = self.boundaryPointList[7]
                middleboundary1 = self.boundaryPointList[1]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, True)
                    self.baseBarrier(f, leftboundary2, self.sideType, True)
                    self.baseBarrier(f, leftboundary3, self.sideType, True)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1': # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f,middleboundary1,self.middleType,True)

            if self.laneFlag == '2*3左' or self.laneFlag == '2*3右':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[3]
                leftboundary3 = self.boundaryPointList[7]
                rightboundary1 = self.boundaryPointList[2]
                rightboundary2 = self.boundaryPointList[6]
                rightboundary3 = self.boundaryPointList[10]
                if self.laneFlag == "2*3左":
                    middleboundary1 = self.boundaryPointList[1]
                    middleboundary2 = self.boundaryPointList[5]
                    middleboundary3 = self.boundaryPointList[9]
                else:
                    middleboundary1 = self.boundaryPointList[1]
                    middleboundary2 = self.boundaryPointList[4]
                    middleboundary3 = self.boundaryPointList[8]

                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1':  # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

            if self.laneFlag == '3*2左' or self.laneFlag == '3*2右':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[4]
                leftboundary3 = self.boundaryPointList[8]
                rightboundary1 = self.boundaryPointList[3]
                rightboundary2 = self.boundaryPointList[7]
                rightboundary3 = self.boundaryPointList[10]
                if self.laneFlag == "3*2左":
                    middleboundary1 = self.boundaryPointList[2]
                    middleboundary2 = self.boundaryPointList[6]
                    middleboundary3 = self.boundaryPointList[9]
                else:
                    middleboundary1 = self.boundaryPointList[1]
                    middleboundary2 = self.boundaryPointList[5]
                    middleboundary3 = self.boundaryPointList[9]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1':  # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

            if self.laneFlag == '3*4右' or self.laneFlag == '3*4左':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[4]
                leftboundary3 = self.boundaryPointList[9]
                rightboundary1 = self.boundaryPointList[3]
                rightboundary2 = self.boundaryPointList[8]
                rightboundary3 = self.boundaryPointList[13]
                if self.laneFlag == '3*4右':
                    middleboundary1 = self.boundaryPointList[2]
                    middleboundary2 = self.boundaryPointList[6]
                    middleboundary3 = self.boundaryPointList[11]
                else:
                    middleboundary1 = self.boundaryPointList[1]
                    middleboundary2 = self.boundaryPointList[6]
                    middleboundary3 = self.boundaryPointList[11]

                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1':  # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

            if self.laneFlag == '4*3左' or self.laneFlag == '4*3右':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[5]
                leftboundary3 = self.boundaryPointList[10]
                rightboundary1 = self.boundaryPointList[4]
                rightboundary2 = self.boundaryPointList[9]
                rightboundary3 = self.boundaryPointList[13]
                if self.laneFlag == "4*3左":
                    middleboundary1 = self.boundaryPointList[2]
                    middleboundary2 = self.boundaryPointList[7]
                    middleboundary3 = self.boundaryPointList[11]
                else:
                    middleboundary1 = self.boundaryPointList[2]
                    middleboundary2 = self.boundaryPointList[7]
                    middleboundary3 = self.boundaryPointList[12]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1':  # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

            if self.laneFlag == '4*6':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[5]
                leftboundary3 = self.boundaryPointList[12]
                rightboundary1 = self.boundaryPointList[4]
                rightboundary2 = self.boundaryPointList[11]
                rightboundary3 = self.boundaryPointList[18]
                middleboundary1 = self.boundaryPointList[2]
                middleboundary2 = self.boundaryPointList[8]
                middleboundary3 = self.boundaryPointList[15]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1':  # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

            if self.laneFlag == '6*4':
                leftboundary1 = self.boundaryPointList[0]
                leftboundary2 = self.boundaryPointList[7]
                leftboundary3 = self.boundaryPointList[14]
                rightboundary1 = self.boundaryPointList[6]
                rightboundary2 = self.boundaryPointList[13]
                rightboundary3 = self.boundaryPointList[18]
                middleboundary1 = self.boundaryPointList[3]
                middleboundary2 = self.boundaryPointList[10]
                middleboundary3 = self.boundaryPointList[16]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, leftboundary1, self.sideType, False)
                    self.baseBarrier(f, leftboundary2, self.sideType, False)
                    self.baseBarrier(f, leftboundary3, self.sideType, False)
                    # 添加右侧护栏
                    self.baseBarrier(f, rightboundary1, self.sideType, False)
                    self.baseBarrier(f, rightboundary2, self.sideType, False)
                    self.baseBarrier(f, rightboundary3, self.sideType, False)
                if self.optionDict.get('Middle') == '1':  # 添加中间边界护栏
                    # 添加中间护栏
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)
                    self.baseBarrier(f, middleboundary3, self.middleType, True)

        if self.laneType == 'fork':
            if self.laneFlag == '单车道右弯曲并入单向双车道' or self.laneFlag == '单车道右弯曲并入双向双车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[1]
                sideboundary3 = self.boundaryPointList[2]
                sideboundary4 = self.boundaryPointList[5]
                sideboundary5 = self.boundaryPointList[6]
                sideboundary6 = self.boundaryPointList[4]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, True)

            if self.laneFlag == '单车道右弯曲并入二前行三车道' or self.laneFlag == '单车道右弯曲并入一前行三车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[1]
                sideboundary3 = self.boundaryPointList[2]
                sideboundary4 = self.boundaryPointList[5]
                sideboundary5 = self.boundaryPointList[8]
                sideboundary6 = self.boundaryPointList[6]
                if self.laneFlag == '单车道右弯曲并入二前行三车道':
                    middleboundary1 = self.boundaryPointList[4]
                    middleboundary2 = self.boundaryPointList[7]
                else:
                    middleboundary1 = self.boundaryPointList[3]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    # 添加中间护栏
                    if self.laneFlag == '单车道右弯曲并入二前行三车道':
                        self.baseBarrier(f, middleboundary1, self.middleType, True)
                        self.baseBarrier(f, middleboundary2, self.middleType, True)
                    if self.laneFlag == '单车道右弯曲并入一前行三车道':
                        self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '单车道右弯曲并入四车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[1]
                sideboundary3 = self.boundaryPointList[2]
                sideboundary4 = self.boundaryPointList[6]
                sideboundary5 = self.boundaryPointList[10]
                sideboundary6 = self.boundaryPointList[7]
                middleboundary1 = self.boundaryPointList[4]
                middleboundary2 = self.boundaryPointList[8]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '单车道左弯曲并入单向双车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[1]
                sideboundary3 = self.boundaryPointList[2]
                sideboundary4 = self.boundaryPointList[4]
                sideboundary5 = self.boundaryPointList[5]
                sideboundary6 = self.boundaryPointList[6]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, True)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)

            if self.laneFlag == '单向双车道右弯曲并入二前行三车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[2]
                sideboundary3 = self.boundaryPointList[3]
                sideboundary4 = self.boundaryPointList[6]
                sideboundary5 = self.boundaryPointList[8]
                sideboundary6 = self.boundaryPointList[7]
                middleboundary1 = self.boundaryPointList[5]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '双向双车道右弯曲并入一前行三车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[2]
                sideboundary3 = self.boundaryPointList[3]
                sideboundary4 = self.boundaryPointList[6]
                sideboundary5 = self.boundaryPointList[8]
                sideboundary6 = self.boundaryPointList[7]
                middleboundary1 = self.boundaryPointList[1]
                middleboundary2 = self.boundaryPointList[4]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '单向双车道右弯曲并入四车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[2]
                sideboundary3 = self.boundaryPointList[3]
                sideboundary4 = self.boundaryPointList[7]
                sideboundary5 = self.boundaryPointList[10]
                sideboundary6 = self.boundaryPointList[8]
                middleboundary1 = self.boundaryPointList[5]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '双向双车道左弯曲并入二前行三车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[2]
                sideboundary3 = self.boundaryPointList[3]
                sideboundary4 = self.boundaryPointList[6]
                sideboundary5 = self.boundaryPointList[8]
                sideboundary6 = self.boundaryPointList[7]
                middleboundary1 = self.boundaryPointList[1]
                middleboundary2 = self.boundaryPointList[4]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, True)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, True)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '二前行三车道右弯曲并入四车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[3]
                sideboundary3 = self.boundaryPointList[4]
                sideboundary4 = self.boundaryPointList[8]
                sideboundary5 = self.boundaryPointList[10]
                sideboundary6 = self.boundaryPointList[9]
                middleboundary1 = self.boundaryPointList[1]
                middleboundary2 = self.boundaryPointList[6]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '一前行三车道左弯曲并入四车道':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[3]
                sideboundary3 = self.boundaryPointList[4]
                sideboundary4 = self.boundaryPointList[8]
                sideboundary5 = self.boundaryPointList[10]
                sideboundary6 = self.boundaryPointList[9]
                middleboundary1 = self.boundaryPointList[2]
                middleboundary2 = self.boundaryPointList[6]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, True)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, True)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '单向双车道右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[3]
                sideboundary3 = self.boundaryPointList[4]
                sideboundary4 = self.boundaryPointList[5]
                sideboundary5 = self.boundaryPointList[6]
                sideboundary6 = self.boundaryPointList[2]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)

            if self.laneFlag == '一前行三车道右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[4]
                sideboundary3 = self.boundaryPointList[6]
                sideboundary4 = self.boundaryPointList[7]
                sideboundary5 = self.boundaryPointList[8]
                sideboundary6 = self.boundaryPointList[3]
                middleboundary1 = self.boundaryPointList[2]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '二前行三车道一右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[4]
                sideboundary3 = self.boundaryPointList[6]
                sideboundary4 = self.boundaryPointList[7]
                sideboundary5 = self.boundaryPointList[8]
                sideboundary6 = self.boundaryPointList[3]
                middleboundary1 = self.boundaryPointList[1]
                middleboundary2 = self.boundaryPointList[5]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '二前行三车道二右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[4]
                sideboundary3 = self.boundaryPointList[5]
                sideboundary4 = self.boundaryPointList[6]
                sideboundary5 = self.boundaryPointList[8]
                sideboundary6 = self.boundaryPointList[3]
                middleboundary1 = self.boundaryPointList[1]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '一前行三车道左右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[4]
                sideboundary3 = self.boundaryPointList[5]
                sideboundary4 = self.boundaryPointList[6]
                sideboundary5 = self.boundaryPointList[7]
                sideboundary6 = self.boundaryPointList[8]
                sideboundary7 = self.boundaryPointList[9]
                sideboundary8 = self.boundaryPointList[3]
                middleboundary1 = self.boundaryPointList[2]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, True)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    if self.optionDict.get('Middle') == '1':
                        self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '二前行三车道左右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[4]
                sideboundary3 = self.boundaryPointList[5]
                sideboundary4 = self.boundaryPointList[6]
                sideboundary5 = self.boundaryPointList[7]
                sideboundary6 = self.boundaryPointList[8]
                sideboundary7 = self.boundaryPointList[9]
                sideboundary8 = self.boundaryPointList[3]
                middleboundary1 = self.boundaryPointList[1]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, True)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    if self.optionDict.get('Middle') == '1':
                        self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '四车道一右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[5]
                sideboundary3 = self.boundaryPointList[8]
                sideboundary4 = self.boundaryPointList[9]
                sideboundary5 = self.boundaryPointList[10]
                sideboundary6 = self.boundaryPointList[4]
                middleboundary1 = self.boundaryPointList[2]
                middleboundary2 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '四车道二右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[5]
                sideboundary3 = self.boundaryPointList[7]
                sideboundary4 = self.boundaryPointList[8]
                sideboundary5 = self.boundaryPointList[10]
                sideboundary6 = self.boundaryPointList[4]
                middleboundary1 = self.boundaryPointList[2]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)

            if self.laneFlag == '四车道左右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[5]
                sideboundary3 = self.boundaryPointList[6]
                sideboundary4 = self.boundaryPointList[7]
                sideboundary5 = self.boundaryPointList[9]
                sideboundary6 = self.boundaryPointList[10]
                sideboundary7 = self.boundaryPointList[11]
                sideboundary8 = self.boundaryPointList[4]
                middleboundary1 = self.boundaryPointList[2]
                middleboundary2 = self.boundaryPointList[8]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, True)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    if self.optionDict.get('Middle') == '1':
                        self.baseBarrier(f, middleboundary1, self.middleType, True)
                        self.baseBarrier(f, middleboundary2, self.middleType, True)

            if self.laneFlag == '双向双车道右弯曲岔路':
                sideboundary1 = self.boundaryPointList[0]
                sideboundary2 = self.boundaryPointList[3]
                sideboundary3 = self.boundaryPointList[4]
                sideboundary4 = self.boundaryPointList[5]
                sideboundary5 = self.boundaryPointList[6]
                sideboundary6 = self.boundaryPointList[2]
                middleboundary1 = self.boundaryPointList[1]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加侧边
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, True)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, True)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    self.baseBarrier(f, middleboundary1, self.middleType, True)

        if self.laneType == 'tJunction':

            if self.laneFlag == '单向车道转双向双车道':
                sideboundary1 = self.boundaryPointList[7]
                sideboundary2 = self.boundaryPointList[8]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[10]
                sideboundary5 = self.boundaryPointList[11]
                sideboundary6 = self.boundaryPointList[6]
                sideboundary7 = self.boundaryPointList[12]
                sideboundary8 = self.boundaryPointList[14]
                sideboundary9 = self.special_barrier
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, True)

            if self.laneFlag == '单向车道转双向三车道一' or self.laneFlag == '单向车道转双向三车道二':
                sideboundary1 = self.boundaryPointList[8]
                sideboundary2 = self.boundaryPointList[9]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[11]
                sideboundary5 = self.boundaryPointList[13]
                sideboundary6 = self.boundaryPointList[7]
                sideboundary7 = self.boundaryPointList[14]
                sideboundary8 = self.boundaryPointList[17]
                sideboundary9 = self.special_barrier
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, True)

            if self.laneFlag == '单向车道转双向四车道':
                sideboundary1 = self.boundaryPointList[9]
                sideboundary2 = self.boundaryPointList[10]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[12]
                sideboundary5 = self.boundaryPointList[15]
                sideboundary6 = self.boundaryPointList[8]
                sideboundary7 = self.boundaryPointList[16]
                sideboundary8 = self.boundaryPointList[20]
                sideboundary9 = self.special_barrier
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, True)

            if self.laneFlag == '同向双车道转双向双车道':
                sideboundary1 = self.boundaryPointList[7]
                sideboundary2 = self.boundaryPointList[9]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[11]
                sideboundary5 = self.boundaryPointList[12]
                sideboundary6 = self.boundaryPointList[6]
                sideboundary7 = self.boundaryPointList[13]
                sideboundary8 = self.boundaryPointList[15]
                sideboundary9 = self.special_barrier
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, True)

            if self.laneFlag == '同向双车道转双向三车道一' or self.laneFlag == '同向双车道转双向三车道二':
                sideboundary1 = self.boundaryPointList[8]
                sideboundary2 = self.boundaryPointList[10]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[12]
                sideboundary5 = self.boundaryPointList[14]
                sideboundary6 = self.boundaryPointList[7]
                sideboundary7 = self.boundaryPointList[15]
                sideboundary8 = self.boundaryPointList[18]
                sideboundary9 = self.special_barrier
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, True)

            if self.laneFlag == '同向双车道转双向四车道':
                sideboundary1 = self.boundaryPointList[9]
                sideboundary2 = self.boundaryPointList[11]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[13]
                sideboundary5 = self.boundaryPointList[16]
                sideboundary6 = self.boundaryPointList[8]
                sideboundary7 = self.boundaryPointList[17]
                sideboundary8 = self.boundaryPointList[21]
                sideboundary9 = self.special_barrier
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, True)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, True)

            if self.laneFlag == '双向双车道转双向双车道':
                sideboundary1 = self.boundaryPointList[9]
                sideboundary2 = self.boundaryPointList[11]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[13]
                sideboundary5 = self.boundaryPointList[14]
                sideboundary6 = self.boundaryPointList[8]
                sideboundary7 = self.boundaryPointList[15]
                sideboundary8 = self.boundaryPointList[17]
                sideboundary9 = self.boundaryPointList[5]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向双车道转双向三车道一' or self.laneFlag == '双向双车道转双向三车道二':
                sideboundary1 = self.boundaryPointList[12]
                sideboundary2 = self.boundaryPointList[14]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[16]
                sideboundary5 = self.boundaryPointList[18]
                sideboundary6 = self.boundaryPointList[11]
                sideboundary7 = self.boundaryPointList[19]
                sideboundary8 = self.boundaryPointList[22]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向双车道转双向四车道':
                sideboundary1 = self.boundaryPointList[13]
                sideboundary2 = self.boundaryPointList[15]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[17]
                sideboundary5 = self.boundaryPointList[20]
                sideboundary6 = self.boundaryPointList[12]
                sideboundary7 = self.boundaryPointList[21]
                sideboundary8 = self.boundaryPointList[25]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向三车道一转双向双车道':
                sideboundary1 = self.boundaryPointList[10]
                sideboundary2 = self.boundaryPointList[13]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[15]
                sideboundary5 = self.boundaryPointList[16]
                sideboundary6 = self.boundaryPointList[9]
                sideboundary7 = self.boundaryPointList[17]
                sideboundary8 = self.boundaryPointList[19]
                sideboundary9 = self.boundaryPointList[6]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向三车道一转双向三车道一' or self.laneFlag == '双向三车道一转双向三车道二':
                sideboundary1 = self.boundaryPointList[12]
                sideboundary2 = self.boundaryPointList[15]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[17]
                sideboundary5 = self.boundaryPointList[19]
                sideboundary6 = self.boundaryPointList[11]
                sideboundary7 = self.boundaryPointList[20]
                sideboundary8 = self.boundaryPointList[23]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向三车道一转双向四车道':
                sideboundary1 = self.boundaryPointList[13]
                sideboundary2 = self.boundaryPointList[16]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[18]
                sideboundary5 = self.boundaryPointList[21]
                sideboundary6 = self.boundaryPointList[12]
                sideboundary7 = self.boundaryPointList[22]
                sideboundary8 = self.boundaryPointList[26]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向三车道二转双向双车道':
                sideboundary1 = self.boundaryPointList[11]
                sideboundary2 = self.boundaryPointList[14]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[16]
                sideboundary5 = self.boundaryPointList[17]
                sideboundary6 = self.boundaryPointList[10]
                sideboundary7 = self.boundaryPointList[18]
                sideboundary8 = self.boundaryPointList[20]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向三车道二转双向三车道一' or self.laneFlag == '双向三车道二转双向三车道二':
                sideboundary1 = self.boundaryPointList[12]
                sideboundary2 = self.boundaryPointList[15]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[17]
                sideboundary5 = self.boundaryPointList[19]
                sideboundary6 = self.boundaryPointList[11]
                sideboundary7 = self.boundaryPointList[20]
                sideboundary8 = self.boundaryPointList[23]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向三车道二转双向四车道':
                sideboundary1 = self.boundaryPointList[13]
                sideboundary2 = self.boundaryPointList[16]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[18]
                sideboundary5 = self.boundaryPointList[21]
                sideboundary6 = self.boundaryPointList[12]
                sideboundary7 = self.boundaryPointList[22]
                sideboundary8 = self.boundaryPointList[26]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向四车道转双向双车道':
                sideboundary1 = self.boundaryPointList[11]
                sideboundary2 = self.boundaryPointList[15]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[17]
                sideboundary5 = self.boundaryPointList[18]
                sideboundary6 = self.boundaryPointList[10]
                sideboundary7 = self.boundaryPointList[19]
                sideboundary8 = self.boundaryPointList[21]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向四车道转双向三车道一' or self.laneFlag == '双向四车道转双向三车道二':
                sideboundary1 = self.boundaryPointList[12]
                sideboundary2 = self.boundaryPointList[16]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[18]
                sideboundary5 = self.boundaryPointList[20]
                sideboundary6 = self.boundaryPointList[11]
                sideboundary7 = self.boundaryPointList[21]
                sideboundary8 = self.boundaryPointList[24]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向四车道转双向四车道':
                sideboundary1 = self.boundaryPointList[13]
                sideboundary2 = self.boundaryPointList[17]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[19]
                sideboundary5 = self.boundaryPointList[22]
                sideboundary6 = self.boundaryPointList[12]
                sideboundary7 = self.boundaryPointList[23]
                sideboundary8 = self.boundaryPointList[27]
                sideboundary9 = self.boundaryPointList[7]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

            if self.laneFlag == '双向双车道转同向双车道':
                sideboundary1 = self.boundaryPointList[7]
                sideboundary2 = self.boundaryPointList[9]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[11]
                sideboundary5 = self.boundaryPointList[12]
                sideboundary6 = self.boundaryPointList[6]
                sideboundary7 = self.boundaryPointList[13]
                sideboundary8 = self.boundaryPointList[15]
                sideboundary9 = self.boundaryPointList[3]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, True)
                    self.baseBarrier(f, sideboundary6, self.sideType, True)
                    self.baseBarrier(f, sideboundary7, self.sideType, True)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)

        if self.laneType == 'intersection':
            if self.laneFlag == '双向双车道十字路口':
                sideboundary1 = self.boundaryPointList[19]
                sideboundary2 = self.boundaryPointList[20]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[22]
                sideboundary5 = self.boundaryPointList[23]
                sideboundary6 = self.boundaryPointList[5]
                sideboundary7 = self.boundaryPointList[26]
                sideboundary8 = self.boundaryPointList[25]
                sideboundary9 = self.boundaryPointList[8]
                sideboundary10 = self.boundaryPointList[28]
                sideboundary11 = self.boundaryPointList[29]
                sideboundary12 = self.boundaryPointList[10]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)
                    self.baseBarrier(f, sideboundary10, self.sideType, False)
                    self.baseBarrier(f, sideboundary11, self.sideType, False)
                    self.baseBarrier(f, sideboundary12, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    middleboundary1 = self.boundaryPointList[18]
                    middleboundary2 = self.boundaryPointList[21]
                    middleboundary3 = self.boundaryPointList[24]
                    middleboundary4 = self.boundaryPointList[27]
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, False)
                    self.baseBarrier(f, middleboundary3, self.middleType, False)
                    self.baseBarrier(f, middleboundary4, self.middleType, False)
            if self.laneFlag == '四车道十字路口':
                sideboundary1 = self.boundaryPointList[23]
                sideboundary2 = self.boundaryPointList[26]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[28]
                sideboundary5 = self.boundaryPointList[31]
                sideboundary6 = self.boundaryPointList[5]
                sideboundary7 = self.boundaryPointList[36]
                sideboundary8 = self.boundaryPointList[33]
                sideboundary9 = self.boundaryPointList[9]
                sideboundary10 = self.boundaryPointList[38]
                sideboundary11 = self.boundaryPointList[41]
                sideboundary12 = self.boundaryPointList[13]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)
                    self.baseBarrier(f, sideboundary10, self.sideType, False)
                    self.baseBarrier(f, sideboundary11, self.sideType, False)
                    self.baseBarrier(f, sideboundary12, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    middleboundary1 = self.boundaryPointList[24]
                    middleboundary2 = self.boundaryPointList[29]
                    middleboundary3 = self.boundaryPointList[34]
                    middleboundary4 = self.boundaryPointList[39]
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, False)
                    self.baseBarrier(f, middleboundary3, self.middleType, False)
                    self.baseBarrier(f, middleboundary4, self.middleType, False)

            if self.laneFlag == '六车道十字路口':
                sideboundary1 = self.boundaryPointList[25]
                sideboundary2 = self.boundaryPointList[30]
                sideboundary3 = self.boundaryPointList[1]
                sideboundary4 = self.boundaryPointList[32]
                sideboundary5 = self.boundaryPointList[37]
                sideboundary6 = self.boundaryPointList[5]
                sideboundary7 = self.boundaryPointList[44]
                sideboundary8 = self.boundaryPointList[39]
                sideboundary9 = self.boundaryPointList[9]
                sideboundary10 = self.boundaryPointList[46]
                sideboundary11 = self.boundaryPointList[51]
                sideboundary12 = self.boundaryPointList[13]
                if self.optionDict.get('Side') == '1':  # 添加两侧护栏
                    # 添加左侧护栏
                    self.baseBarrier(f, sideboundary1, self.sideType, False)
                    self.baseBarrier(f, sideboundary2, self.sideType, False)
                    self.baseBarrier(f, sideboundary3, self.sideType, False)
                    self.baseBarrier(f, sideboundary4, self.sideType, False)
                    self.baseBarrier(f, sideboundary5, self.sideType, False)
                    self.baseBarrier(f, sideboundary6, self.sideType, False)
                    self.baseBarrier(f, sideboundary7, self.sideType, False)
                    self.baseBarrier(f, sideboundary8, self.sideType, False)
                    self.baseBarrier(f, sideboundary9, self.sideType, False)
                    self.baseBarrier(f, sideboundary10, self.sideType, False)
                    self.baseBarrier(f, sideboundary11, self.sideType, False)
                    self.baseBarrier(f, sideboundary12, self.sideType, False)
                if self.optionDict.get('Middle') == '1':
                    middleboundary1 = self.boundaryPointList[27]
                    middleboundary2 = self.boundaryPointList[34]
                    middleboundary3 = self.boundaryPointList[41]
                    middleboundary4 = self.boundaryPointList[48]
                    self.baseBarrier(f, middleboundary1, self.middleType, True)
                    self.baseBarrier(f, middleboundary2, self.middleType, False)
                    self.baseBarrier(f, middleboundary3, self.middleType, False)
                    self.baseBarrier(f, middleboundary4, self.middleType, False)


































































