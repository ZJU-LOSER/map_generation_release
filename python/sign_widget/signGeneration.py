# 传入道路组件和sign组件的dict信息，泛化生成sign路标指示牌
import random

from sign_widget.sign import Sign


class signGenerationClass():
    roadType = ''  # 组件类型
    roadBoundary = []  # 道路边界信息
    roadFlag = ''  # 道路类型

    signOffset = 0.7  # sign和道路的间隙长度

    def __init__(self, roadDict):
        self.roadType = roadDict.get('Type')
        self.roadFlag = roadDict.get('Flag')
        self.roadBoundary = roadDict.get('roadBoundary')
        self.K = roadDict.get('K')  #

    def getSignPointAndDirection(self):

        if self.roadType == 'straightlane':
            global signPointX  # sign的X坐标
            global signPointY  # sign的Y坐标
            global sign2PointX  # sign2的X坐标
            global sign2PointY  # sign2的Y坐标
            global Direction  # sign的方向
            global Direction2  # sign2的方向
            global targetBoundary1  # 待添加sign的路边
            global targetBoundary2  # 待添加sign2的路边
            if self.roadFlag == '单行道':  # 道路车道种类
                targetBoundary1 = self.roadBoundary[1]
                # 根据方向求解坐标和方向
                if self.K == '+':
                    signPointX = targetBoundary1[0][0] + self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '0'
                elif self.K == '-':
                    signPointX = targetBoundary1[0][0] - self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '2'
                elif self.K == '+0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] - self.signOffset
                    Direction = '1'
                elif self.K == '-0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] + self.signOffset
                    Direction = '3'
                return signPointX, signPointY, Direction  # 返回X,Y以及方向

            elif self.roadFlag == '单向虚线双行道' or self.roadFlag == '单向实线双行道' or self.roadFlag == '单向虚实线双行道' or self.roadFlag == '单向双实线双行道':
                targetBoundary1 = self.roadBoundary[2]
                # 根据方向求解坐标和方向
                if self.K == '+':
                    signPointX = targetBoundary1[0][0] + self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '0'
                elif self.K == '-':
                    signPointX = targetBoundary1[0][0] - self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '2'
                elif self.K == '+0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] - self.signOffset
                    Direction = '1'
                elif self.K == '-0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] + self.signOffset
                    Direction = '3'
                return signPointX, signPointY, Direction  # 返回X,Y以及方向
            elif self.roadFlag in ['双向虚线双行道', '双向实线双行道', '双向虚实线双行道', '双向双实线双行道']:
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[2]
                # 根据方向求解坐标和方向
                if self.K == '+':
                    signPointX = targetBoundary1[0][0] - self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '2'
                    Direction2 = '0'
                elif self.K == '-':
                    signPointX = targetBoundary1[0][0] + self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '0'
                    Direction2 = '2'
                elif self.K == '+0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '1'
                elif self.K == '-0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '3'

                return signPointX, signPointY, Direction, sign2PointX, sign2PointY, Direction2  # 返回X,Y以及方向
            elif self.roadFlag in ['一前行虚白线虚黄线三行道', '一前行虚白线实黄线三行道', '一前行实白线实黄线三行道',
                                   '二前行虚黄线虚白线三行道', '二前行虚黄线实白线三行道', '二前行实黄线虚白线三行道',
                                   '二前行实黄线实白线三行道']:
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[3]
                # 根据方向求解坐标和方向
                if self.K == '+':
                    signPointX = targetBoundary1[0][0] - self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '2'
                    Direction2 = '0'
                elif self.K == '-':
                    signPointX = targetBoundary1[0][0] + self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '0'
                    Direction2 = '2'
                elif self.K == '+0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '1'
                elif self.K == '-0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '3'

                return signPointX, signPointY, Direction, sign2PointX, sign2PointY, Direction2  # 返回X,Y以及方向
            elif self.roadFlag in ['双黄实线虚虚四车道', '双黄实线实实四车道', '双黄实线虚实四车道',
                                   '双黄实线实虚四车道']:
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[4]
                # 根据方向求解坐标和方向
                if self.K == '+':
                    signPointX = targetBoundary1[0][0] - self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '2'
                    Direction2 = '0'
                elif self.K == '-':
                    signPointX = targetBoundary1[0][0] + self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '0'
                    Direction2 = '2'
                elif self.K == '+0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '1'
                elif self.K == '-0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '3'

                return signPointX, signPointY, Direction, sign2PointX, sign2PointY, Direction2  # 返回X,Y以及方向
            elif self.roadFlag in ['双实线虚虚虚虚六车道', '双实线实实实实六车道', '双实线虚虚实实六车道']:
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[6]
                # 根据方向求解坐标和方向
                if self.K == '+':
                    signPointX = targetBoundary1[0][0] - self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '2'
                    Direction2 = '0'
                elif self.K == '-':
                    signPointX = targetBoundary1[0][0] + self.signOffset
                    signPointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    Direction = '0'
                    Direction2 = '2'
                elif self.K == '+0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '1'
                elif self.K == '-0':
                    signPointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    signPointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '3'

                return signPointX, signPointY, Direction, sign2PointX, sign2PointY, Direction2  # 返回X,Y以及方向

        if self.roadType == 'laneswitch':
            if self.roadFlag == '1*2左':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[5]
                targetBoundary3 = self.roadBoundary[4]
                targetBoundary4 = self.roadBoundary[7]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '1*2右':
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[7]
                targetBoundary3 = self.roadBoundary[2]
                targetBoundary4 = self.roadBoundary[5]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '2*1左':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[6]
                targetBoundary3 = self.roadBoundary[2]
                targetBoundary4 = self.roadBoundary[5]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '2*1右':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[6]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[3]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '2*3左':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[7]
                targetBoundary3 = self.roadBoundary[6]
                targetBoundary4 = self.roadBoundary[10]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '2*3右':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[10]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[7]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '3*2左':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[8]
                targetBoundary3 = self.roadBoundary[3]
                targetBoundary4 = self.roadBoundary[10]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '3*2右':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[10]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[8]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '3*4右':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[13]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[9]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '3*4左':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[9]
                targetBoundary3 = self.roadBoundary[3]
                targetBoundary4 = self.roadBoundary[13]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '4*3左':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[10]
                targetBoundary3 = self.roadBoundary[4]
                targetBoundary4 = self.roadBoundary[13]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '4*3右':
                targetBoundary1 = self.roadBoundary[4]
                targetBoundary2 = self.roadBoundary[13]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[10]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3  # 返回X,Y以及方向
            elif self.roadFlag == '4*6':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[12]
                targetBoundary3 = self.roadBoundary[4]
                targetBoundary4 = self.roadBoundary[18]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向
            elif self.roadFlag == '6*4':
                targetBoundary1 = self.roadBoundary[0]
                targetBoundary2 = self.roadBoundary[14]
                targetBoundary3 = self.roadBoundary[6]
                targetBoundary4 = self.roadBoundary[18]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4  # 返回X,Y以及方向

        if self.roadType == 'ulane':
            if self.roadFlag in ['单行道']:
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[3]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
            if self.roadFlag in ['单向虚线双行道', '单向实线双行道', '单向虚实线双行道', '单向双实线双行道']:
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[5]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
            if self.roadFlag in ['双向虚线双行道', '双向实线双行道', '双向虚实线双行道', '双向虚实线双行道',
                                 '双向双实线双行道']:
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[0]
                targetBoundary3 = self.roadBoundary[2]
                targetBoundary4 = self.roadBoundary[5]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    Direction3 = '0'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
            if self.roadFlag in ['一前行虚白线虚黄线三行道', '一前行实白线虚黄线三行道', '一前行虚白线实黄线三行道',
                                 '一前行实白线实黄线三行道', '二前行虚黄线虚白线三行道', '二前行虚黄线实白线三行道',
                                 '二前行实黄线虚白线三行道', '二前行实黄线实白线三行道']:
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[7]
                targetBoundary3 = self.roadBoundary[4]
                targetBoundary4 = self.roadBoundary[0]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    Direction3 = '0'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
            if self.roadFlag in ['双黄实线虚虚四车道', '双黄实线实实四车道', '双黄实线虚实四车道',
                                 '双黄实线虚实四车道']:
                targetBoundary1 = self.roadBoundary[5]
                targetBoundary2 = self.roadBoundary[0]
                targetBoundary3 = self.roadBoundary[4]
                targetBoundary4 = self.roadBoundary[9]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    Direction3 = '0'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
            if self.roadFlag in ['双实线虚虚虚虚六车道', '双实线实实实实六车道', '双实线虚虚实实六车道']:
                targetBoundary1 = self.roadBoundary[7]
                targetBoundary2 = self.roadBoundary[0]
                targetBoundary3 = self.roadBoundary[6]
                targetBoundary4 = self.roadBoundary[13]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    Direction3 = '0'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary4[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4

        if self.roadType == 'fork':
            if self.roadFlag in ['单车道右弯曲并入单向双车道']:
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[2]
                targetBoundary3 = self.roadBoundary[5]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '单车道右弯曲并入双向双车道':
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[2]
                targetBoundary3 = self.roadBoundary[4]
                targetBoundary4 = self.roadBoundary[6]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '单车道右弯曲并入二前行三车道':
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[2]
                targetBoundary3 = self.roadBoundary[5]
                targetBoundary4 = self.roadBoundary[8]
                targetBoundary5 = self.roadBoundary[6]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary5[0][0], targetBoundary5[2][0])
                    sign4PointY = targetBoundary5[0][1] - self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary5[0][0], targetBoundary5[2][0])
                    sign4PointY = targetBoundary5[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary5[0][0], targetBoundary5[2][0])
                    sign4PointY = targetBoundary5[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    sign4PointX = targetBoundary5[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary5[0][1], targetBoundary5[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4

            if self.roadFlag == '单车道右弯曲并入一前行三车道':
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[2]
                targetBoundary3 = self.roadBoundary[5]
                targetBoundary4 = self.roadBoundary[8]
                targetBoundary5 = self.roadBoundary[6]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '单车道右弯曲并入四车道':
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[2]
                targetBoundary3 = self.roadBoundary[7]
                targetBoundary4 = self.roadBoundary[6]
                targetBoundary5 = self.roadBoundary[10]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary5[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '1'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary5[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0], targetBoundary5[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1], targetBoundary5[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '0'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4

            if self.roadFlag == '单车道左弯曲并入单向双车道':
                targetBoundary1 = self.roadBoundary[1]
                targetBoundary2 = self.roadBoundary[4]
                targetBoundary3 = self.roadBoundary[6]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '1'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    Direction1 = '3'
                    Direction2 = '2'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                return

            if self.roadFlag == '单向双车道右弯曲并入二前行三车道':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[3]
                targetBoundary3 = self.roadBoundary[6]
                targetBoundary4 = self.roadBoundary[8]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '双向双车道右弯曲并入一前行三车道':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[3]
                targetBoundary3 = self.roadBoundary[6]
                targetBoundary4 = self.roadBoundary[8]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '单向双车道右弯曲并入四车道':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[3]
                targetBoundary3 = self.roadBoundary[7]
                targetBoundary4 = self.roadBoundary[10]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '双向双车道左弯曲并入二前行三车道':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[3]
                targetBoundary3 = self.roadBoundary[6]
                targetBoundary4 = self.roadBoundary[8]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '二前行三车道右弯曲并入四车道':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[4]
                targetBoundary3 = self.roadBoundary[10]
                targetBoundary4 = self.roadBoundary[8]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '一前行三车道左弯曲并入四车道':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[4]
                targetBoundary3 = self.roadBoundary[10]
                targetBoundary4 = self.roadBoundary[8]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '0'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  # 存在问题
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = targetBoundary1[0][1]
                    sign2PointX = random.uniform(targetBoundary2[0][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '3'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = targetBoundary1[0][0]
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[0][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '3'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '单向双车道右弯曲岔路':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[4]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '0'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1],targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':  # 可以用
                    sign1PointX = random.uniform(targetBoundary1[0][0],targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '1'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0],targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0],targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '3'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2

            if self.roadFlag == '双向双车道右弯曲岔路':
                targetBoundary1 = self.roadBoundary[2]
                targetBoundary2 = self.roadBoundary[4]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '0'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':  # 可以用
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2


            if self.roadFlag == '一前行三车道右弯曲岔路':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[0]
                targetBoundary3 = self.roadBoundary[4]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary3[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':  # 可以用
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2

            if self.roadFlag == '二前行三车道一右弯曲岔路':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[0]
                targetBoundary3 = self.roadBoundary[4]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary3[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':  # 可以用
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2

            if self.roadFlag == '二前行三车道二右弯曲岔路':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[0]
                targetBoundary3 = self.roadBoundary[4]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary3[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':  # 可以用
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2

            if self.roadFlag == '一前行三车道左右弯曲岔路':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[6]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[4]
                targetBoundary5 = self.roadBoundary[6]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1],targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[-1][0]
                    sign4PointY = targetBoundary4[-1][1] - self.signOffset
                    Direction1 = '0'
                    Direction2 = '2'
                    Direction3 = '2'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1],targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[-1][0]
                    sign4PointY = targetBoundary4[-1][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '0'
                    Direction3 = '0'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0],targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = targetBoundary4[-1][0] - self.signOffset
                    sign4PointY = targetBoundary4[-1][1]
                    Direction1 = '1'
                    Direction2 = '3'
                    Direction3 = '3'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':  #
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = targetBoundary4[-1][0] + self.signOffset
                    sign4PointY = targetBoundary4[-1][1]
                    Direction1 = '3'
                    Direction2 = '1'
                    Direction3 = '1'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4

            if self.roadFlag == '二前行三车道左右弯曲岔路':
                targetBoundary1 = self.roadBoundary[3]
                targetBoundary2 = self.roadBoundary[6]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[4]
                targetBoundary5 = self.roadBoundary[6]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1],targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[-1][0]
                    sign4PointY = targetBoundary4[-1][1] - self.signOffset
                    Direction1 = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1],targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[-1][0]
                    sign4PointY = targetBoundary4[-1][1] + self.signOffset
                    Direction1 = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0],targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = targetBoundary4[-1][0] - self.signOffset
                    sign4PointY = targetBoundary4[-1][1]
                    Direction1 = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':  #
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = targetBoundary4[-1][0] + self.signOffset
                    sign4PointY = targetBoundary4[-1][1]
                    Direction1 = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4

            if self.roadFlag == '四车道一右弯曲岔路':
                targetBoundary1 = self.roadBoundary[4]
                targetBoundary2 = self.roadBoundary[8]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[5]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1],targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '0'
                    Direction2 = '0'
                    Direction3 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1],targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary4[2][1])
                    Direction1 = '2'
                    Direction2 = '2'
                    Direction3 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '+0':  
                    sign1PointX = random.uniform(targetBoundary1[0][0],targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0],targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '1'
                    Direction3 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3
                if self.K == '-0':  #
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary4[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '3'
                    Direction3 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3

            if self.roadFlag == '四车道二右弯曲岔路':
                targetBoundary1 = self.roadBoundary[4]
                targetBoundary2 = self.roadBoundary[5]
                targetBoundary3 = self.roadBoundary[0]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary3[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '+0':  # 可以用
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                if self.K == '-0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2
                return

            if self.roadFlag == '四车道左右弯曲岔路':
                targetBoundary1 = self.roadBoundary[4]
                targetBoundary2 = self.roadBoundary[7]
                targetBoundary3 = self.roadBoundary[0]
                targetBoundary4 = self.roadBoundary[9]
                if self.K == '+':
                    sign1PointX = targetBoundary1[0][0] + self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] - self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] - self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] + self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1],targetBoundary4[2][1])
                    Direction1 = '0'
                    Direction2 = '2'
                    Direction3 = '2'
                    Direction4 = '0'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-':
                    sign1PointX = targetBoundary1[0][0] - self.signOffset
                    sign1PointY = random.uniform(targetBoundary1[0][1], targetBoundary1[2][1])
                    sign2PointX = targetBoundary2[0][0] + self.signOffset
                    sign2PointY = random.uniform(targetBoundary2[1][1], targetBoundary2[2][1])
                    sign3PointX = targetBoundary3[0][0] + self.signOffset
                    sign3PointY = random.uniform(targetBoundary3[0][1], targetBoundary3[2][1])
                    sign4PointX = targetBoundary4[0][0] - self.signOffset
                    sign4PointY = random.uniform(targetBoundary4[0][1],targetBoundary4[2][1])
                    Direction1 = '2'
                    Direction2 = '0'
                    Direction3 = '0'
                    Direction4 = '2'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '+0':
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] - self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] + self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] + self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[1][0],targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] - self.signOffset
                    Direction1 = '1'
                    Direction2 = '3'
                    Direction3 = '3'
                    Direction4 = '1'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4
                if self.K == '-0':  #
                    sign1PointX = random.uniform(targetBoundary1[0][0], targetBoundary1[2][0])
                    sign1PointY = targetBoundary1[0][1] + self.signOffset
                    sign2PointX = random.uniform(targetBoundary2[1][0], targetBoundary2[2][0])
                    sign2PointY = targetBoundary2[0][1] - self.signOffset
                    sign3PointX = random.uniform(targetBoundary3[0][0], targetBoundary3[2][0])
                    sign3PointY = targetBoundary3[0][1] - self.signOffset
                    sign4PointX = random.uniform(targetBoundary4[0][0],targetBoundary4[2][0])
                    sign4PointY = targetBoundary4[0][1] + self.signOffset
                    Direction1 = '3'
                    Direction2 = '1'
                    Direction3 = '1'
                    Direction4 = '3'
                    return sign1PointX, sign1PointY, Direction1, sign2PointX, sign2PointY, Direction2, sign3PointX, sign3PointY, Direction3, sign4PointX, sign4PointY, Direction4

    def buildSign(self, f):
        if self.roadType == 'straightlane':
            if self.roadFlag in ['单行道', '单向虚线双行道', '单向实线双行道', '单向虚实线双行道',
                                 '单向双实线双行道']:  # 道路车道种类
                # 泛化生成道路组件，间距需要大于等于30m
                # 获取待生成的sign种类
                signType = 'Sign_208'

                signPointX, signPointY, Direction = self.getSignPointAndDirection()
                signDict = {
                    'Geometry': [signPointX, signPointY],
                    'Direction': Direction,
                    'Type': signType,
                }
                currentSign = Sign(signDict)
                currentSign.generate_sign(f)
            if self.roadFlag in ['双向虚线双行道', '双向实线双行道', '双向虚实线双行道', '双向双实线双行道',
                                 '一前行虚白线虚黄线三行道', '一前行虚白线实黄线三行道', '一前行实白线实黄线三行道',
                                 '二前行虚黄线虚白线三行道', '二前行虚黄线实白线三行道', '二前行实黄线虚白线三行道',
                                 '二前行实黄线实白线三行道', '双黄实线虚虚四车道', '双黄实线实实四车道',
                                 '双黄实线虚实四车道', '双黄实线实虚四车道', '双实线虚虚虚虚六车道',
                                 '双实线实实实实六车道', '双实线虚虚实实六车道']:
                signType = 'Sign_209_30'
                signType2 = 'Sign_209_30'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                # print("第一个点坐标为:", [signPointX1, signPointY1])
                # print("第二个点坐标为:", [signPointX2, signPointY2])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)

                return

        if self.roadType == 'laneswitch':
            if self.roadFlag in ['1*2左', '1*2右', '2*1左', '2*1右', '2*3左', '2*3右', '3*2左', '3*2右', '3*4右',
                                 '3*4左', '4*3左', '4*3右']:
                signType1 = 'Sign_208'
                signType2 = 'Sign_208'
                signType3 = 'Sign_208'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2, signPointX3, signPointY3, Direction3 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType1,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                signDict3 = {
                    'Geometry': [signPointX3, signPointY3],
                    'Direction': Direction3,
                    'Type': signType3,
                }
                # print("第一个点坐标为:", [signPointX1, signPointY1])
                # print("第二个点坐标为:", [signPointX2, signPointY2])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)
                currentSign3 = Sign(signDict3)
                currentSign3.generate_sign(f)
            elif self.roadFlag in ['4*6', '6*4']:
                signType1 = 'Sign_208'
                signType2 = 'Sign_208'
                signType3 = 'Sign_208'
                signType4 = 'Sign_208'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2, signPointX3, signPointY3, Direction3, signPointX4, signPointY4, Direction4 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType1,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                signDict3 = {
                    'Geometry': [signPointX3, signPointY3],
                    'Direction': Direction3,
                    'Type': signType3,
                }
                signDict4 = {
                    'Geometry': [signPointX4, signPointY4],
                    'Direction': Direction4,
                    'Type': signType4,
                }
                # print("第一个点坐标为:", [signPointX1, signPointY1])
                # print("第二个点坐标为:", [signPointX2, signPointY2])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)
                currentSign3 = Sign(signDict3)
                currentSign3.generate_sign(f)
                currentSign4 = Sign(signDict4)
                currentSign4.generate_sign(f)

        if self.roadType == 'ulane':
            # 随机生成至多2个道路指示牌
            if self.roadFlag in ['单行道', '单向虚线双行道', '单向实线双行道', '单向虚实线双行道', '单向双实线双行道']:
                signType1 = 'Sign_208'
                signType2 = 'Sign_208'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType1,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                print("第一个点坐标为:", [signPointX1, signPointY1])
                print("第二个点坐标为:", [signPointX2, signPointY2])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)
            # 随机生成至多4个道路指示牌
            if self.roadFlag in ['双向虚线双行道', '双向实线双行道', '双向虚实线双行道', '双向虚实线双行道',
                                 '双向双实线双行道', '一前行虚白线虚黄线三行道', '一前行实白线虚黄线三行道',
                                 '一前行虚白线实黄线三行道', '一前行实白线实黄线三行道', '二前行虚黄线虚白线三行道',
                                 '二前行虚黄线实白线三行道', '二前行实黄线虚白线三行道', '二前行实黄线实白线三行道',
                                 '双黄实线虚虚四车道', '双黄实线实实四车道', '双黄实线虚实四车道', '双黄实线虚实四车道',
                                 '双实线虚虚虚虚六车道', '双实线实实实实六车道', '双实线虚虚实实六车道']:
                signType1 = 'Sign_208'
                signType2 = 'Sign_208'
                signType3 = 'Sign_208'
                signType4 = 'Sign_208'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2, signPointX3, signPointY3, Direction3, signPointX4, signPointY4, Direction4 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType1,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                signDict3 = {
                    'Geometry': [signPointX3, signPointY3],
                    'Direction': Direction3,
                    'Type': signType3,
                }
                signDict4 = {
                    'Geometry': [signPointX4, signPointY4],
                    'Direction': Direction4,
                    'Type': signType4,
                }
                print("第一个点坐标为:", [signPointX1, signPointY1])
                print("第二个点坐标为:", [signPointX2, signPointY2])
                print("第三个点坐标为:", [signPointX3, signPointY3])
                print("第四个点坐标为:", [signPointX4, signPointY4])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)
                currentSign3 = Sign(signDict3)
                currentSign3.generate_sign(f)
                currentSign4 = Sign(signDict4)
                currentSign4.generate_sign(f)
                return

            return

        if self.roadType == 'fork':
            # 生成2个sign
            if self.roadFlag in ['单向双车道右弯曲岔路','双向双车道右弯曲岔路','一前行三车道右弯曲岔路','二前行三车道一右弯曲岔路','二前行三车道二右弯曲岔路','四车道二右弯曲岔路']:
                signType1 = 'Sign_208'
                signType2 = 'Sign_208'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType1,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                print("第一个点坐标为:", [signPointX1, signPointY1])
                print("第二个点坐标为:", [signPointX2, signPointY2])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)
            # 生成3个sign
            if self.roadFlag in ['单车道右弯曲并入单向双车道', '单车道右弯曲并入双向双车道',
                                 '单车道右弯曲并入一前行三车道', '单车道左弯曲并入单向双车道',
                                 '单向双车道右弯曲并入二前行三车道', '双向双车道右弯曲并入一前行三车道',
                                 '单向双车道右弯曲并入四车道', '双向双车道左弯曲并入二前行三车道',
                                 '二前行三车道右弯曲并入四车道', '一前行三车道左弯曲并入四车道','四车道一右弯曲岔路']:
                signType1 = 'Sign_208'
                signType2 = 'Sign_208'
                signType3 = 'Sign_208'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2, signPointX3, signPointY3, Direction3 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType1,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                signDict3 = {
                    'Geometry': [signPointX3, signPointY3],
                    'Direction': Direction3,
                    'Type': signType3,
                }
                print("第一个点坐标为:", [signPointX1, signPointY1])
                print("第二个点坐标为:", [signPointX2, signPointY2])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)
                currentSign3 = Sign(signDict3)
                currentSign3.generate_sign(f)
            # 生成4个sign
            if self.roadFlag in ['单车道右弯曲并入二前行三车道', '单车道右弯曲并入四车道','一前行三车道左右弯曲岔路','二前行三车道左右弯曲岔路','四车道左右弯曲岔路']:
                signType1 = 'Sign_208'
                signType2 = 'Sign_208'
                signType3 = 'Sign_208'
                signType4 = 'Sign_208'
                signPointX1, signPointY1, Direction1, signPointX2, signPointY2, Direction2, signPointX3, signPointY3, Direction3, signPointX4, signPointY4, Direction4 = self.getSignPointAndDirection()
                signDict1 = {
                    'Geometry': [signPointX1, signPointY1],
                    'Direction': Direction1,
                    'Type': signType1,
                }
                signDict2 = {
                    'Geometry': [signPointX2, signPointY2],
                    'Direction': Direction2,
                    'Type': signType2,
                }
                signDict3 = {
                    'Geometry': [signPointX3, signPointY3],
                    'Direction': Direction3,
                    'Type': signType3,
                }
                signDict4 = {
                    'Geometry': [signPointX4, signPointY4],
                    'Direction': Direction4,
                    'Type': signType4,
                }
                print("第一个点坐标为:", [signPointX1, signPointY1])
                print("第二个点坐标为:", [signPointX2, signPointY2])
                currentSign1 = Sign(signDict1)
                currentSign1.generate_sign(f)
                currentSign2 = Sign(signDict2)
                currentSign2.generate_sign(f)
                currentSign3 = Sign(signDict3)
                currentSign3.generate_sign(f)
                currentSign4 = Sign(signDict4)
                currentSign4.generate_sign(f)

        if self.roadType == 'curve':

            return
