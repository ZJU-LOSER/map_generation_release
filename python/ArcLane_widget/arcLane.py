from func.printAuto import printAutoInd
from func.widget import Widget
import sympy as sy
import numpy as np
import math
class ArcLane(Widget):
    ID=1 #道路id
    Start=(0,0) #起始位置
    End=(0,0) #结束位置
    Width=3.5
    BoundaryId1='b1' #左边界的id
    BoundaryId2='b2' #右边界的id
    Diretction = 0 #0代表向右转，1代表向左转
    TravelDirection = 'Forward' #保存车道的行驶方向forward, backward, bidirectional
    LaneAssetType = {} #字典，保存每个车道的车道线种类{BoundaryID:'SSW',...} SW白色实线, DW白色虚线, DSW白色虚实线, SDW白色双实线, SY黄色实线, DY黄色虚线, DSY黄色虚实线, SDY黄色双实线.
    LaneType = 'Driving' #默认道路类型都是driving
    k = '+0'  # 指定该道路（起点）的方向。k表示直线的斜率。+0表示水平向右，-0表示水平向左，+表示竖直向上，-表示竖直向下。
    k1= '+0'  # 指定该道路（终点）的方向。k表示直线的斜率。+0表示水平向右，-0表示水平向左，+表示竖直向上，-表示竖直向下。
    Flag = '' #组件标记符
    lanePoints=[]
    boundaryPoints=[]

    def __init__(self,dict1):
        self.ID=dict1.get('ID')
        self.Start=dict1.get('Start')
        self.End=dict1.get('End')
        self.Width=dict1.get('Width')
        self.BoundaryId1=dict1.get('BoundaryId1')
        self.BoundaryId2=dict1.get('BoundaryId2')
        self.Direction=dict1.get('Direction')
        self.TravelDirection=dict1.get('TravelDirection')
        self.LaneAssetType=dict1.get('LaneAssetType')
        self.LaneType=dict1.get('LaneType')
        self.k=dict1.get('k')
        self.k1=dict1.get('k1')
        self.Flag=dict1.get('Flag')
        self.lanePoints=self.getlanepoint()
        self.boundaryPoints=self.getboundarypoint()
        
        # Widget.LaneID +=1
        # Widget.BoundaryID +=2

 #判断圆心相对于起点的位置
    def relativePositon(self):
        relative=0 #1：左上 2：左下 3：右上 4：右下
        if self.End[0]<self.Start[0]:#在左边+1
            relative=1
        else:#在右边+3
            relative=3 
        if self.End[1]<self.Start[1]:#在下面+1
            relative+=1
        return relative

    #获取圆心坐标
    def getCirclePoint(self,tag,start,end):
        point=(0,0)
        if tag==0:
            # x=sy.symbols('x')
            # print(end[0])
            # result=sy.solve((x-start[0])**2-(x-end[0])**2-(start[1]-end[1])**2,x)
            x=float("{:.3f}".format((start[0]**2-end[0]**2-(start[1]-end[1])**2)/(2*start[0]-2*end[0])))
            # point=(result[0],start[1])
            point=(x,start[1])
            # print(point)
        else:
            # print("start",start)
            # print("end",end)
            # y=sy.symbols('y')
            # result=sy.solve((y-start[1])**2-(y-end[1])**2-(start[0]-end[0])**2,y)
            # point=(start[0],result[0])
            y=float("{:.3f}".format((start[1]**2-end[1]**2-(start[0]-end[0])**2)/(2*start[1]-2*end[1])))
            point=(start[0],y)
            # print("point",point)
        return point

    #计算圆的方程
    def getCircleFunction(self,start,end):
        relative=self.relativePositon()
        tag=0 #0:水平方向 1：竖直方向
        if relative==1 and self.Direction==0:
            tag=1
        elif relative==1 and self.Direction==1:
            tag=0
        elif relative==2 and self.Direction==0:
            tag=0
        elif relative==2 and self.Direction==1:
            tag=1
        elif relative==3 and self.Direction==0:
            tag=0
        elif relative==3 and self.Direction==1:
            tag=1
        elif relative==4 and self.Direction==0:
            tag=1
        elif relative==4 and self.Direction==1:
            tag=0
        point=self.getCirclePoint(tag,start,end)
        # radius=math.sqrt((point[0]-start[0])**2+(point[1]-start[1])**2)
        radius=0
        if tag==0:
            radius=abs(point[0]-start[0])
        elif tag==1:
            radius=abs(point[1]-start[1])
        # print("radius",radius)
        result=[point,radius]
        return result
    
    #生成道路点
    def getlanepoint(self):
        pointlist=[]
        result=self.getCircleFunction(self.Start,self.End)
        # print(result)
        circlePoint=result[0]
        circleRadius=result[1]
        # print(circlePoint)
        # print(circleRadius)
        pointlistx=np.linspace(self.Start[0],self.End[0],100)
        
        pointlisty=[]
        pointlistx=np.delete(pointlistx,0)
        pointlistx=np.delete(pointlistx,len(pointlistx)-1)
        # print(pointlistx)
        for i in pointlistx:
            y=sy.symbols('y')
            # print(i)
            a=sy.solve((i-circlePoint[0])**2+(y-circlePoint[1])**2-circleRadius**2,y)
            # print(a)
            for j in a:
                
                if j>=min(self.Start[1],self.End[1]) and j<=max(self.Start[1],self.End[1]):
                    pointlisty.append(j)

        # print(len(pointlisty))
        # print(pointlisty)
        pointlist.append(self.Start)
        for i in range(len(pointlistx)):
            point=(pointlistx[i],pointlisty[i])
            pointlist.append(point)
        pointlist.append(self.End)
        # resultlist=[]
        # resultlist.append(pointlist)
        # return(resultlist)
        return(pointlist)
        

    #生成左右两个边界的点
    def getboundarypoint(self):
        twoBoundary=[]
        result=self.getBoundarySEPoint()
        # print(result)
        leftStart=result[0]
        leftEnd=result[1]
        rightStart=result[2]
        rightEnd=result[3]
        leftCircleResult=self.getCircleFunction(leftStart,leftEnd)
        rightCircleResult=self.getCircleFunction(rightStart,rightEnd)
        leftCirclePoint=leftCircleResult[0]
        leftCircleRadius=leftCircleResult[1]
        rightCirclePoint=rightCircleResult[0]
        rightCircleRadius=rightCircleResult[1]

        leftBoundary=[]
        rightBoundary=[]
        leftBoundaryX=np.linspace(leftStart[0],leftEnd[0],100)
        leftBoundaryY=[]
        leftBoundaryX=np.delete(leftBoundaryX,0)
        leftBoundaryX=np.delete(leftBoundaryX,len(leftBoundaryX)-1)
        for i in leftBoundaryX:
            y=sy.symbols('y')
            a=sy.solve((i-leftCirclePoint[0])**2+(y-leftCirclePoint[1])**2-leftCircleRadius**2,y)
            #print(a)
            for j in a:
                if j>=min(leftStart[1],leftEnd[1]) and j<=max(leftStart[1],leftEnd[1]):
                    leftBoundaryY.append(j)
        # print(len(leftBoundaryX))
        # print(leftBoundaryY)
        # print(len(leftBoundaryY))
        leftBoundary.append(leftStart)

        for i in range(len(leftBoundaryX)):
            leftBoundary.append((leftBoundaryX[i],leftBoundaryY[i]))
        leftBoundary.append(leftEnd)
        
        rightBoundaryX=np.linspace(rightStart[0],rightEnd[0],100)
        rightBoundaryY=[]
        rightBoundaryX=np.delete(rightBoundaryX,0)
        rightBoundaryX=np.delete(rightBoundaryX,len(rightBoundaryX)-1)
        for i in rightBoundaryX:
            y=sy.symbols('y')
            a=sy.solve((i-rightCirclePoint[0])**2+(y-rightCirclePoint[1])**2-rightCircleRadius**2,y)
            for j in a:
                if j>=min(rightStart[1],rightEnd[1]) and j<=max(rightStart[1],rightEnd[1]):
                    rightBoundaryY.append(j)
        rightBoundary.append(rightStart)
        for i in range(len(rightBoundaryX)):
            rightBoundary.append((rightBoundaryX[i],rightBoundaryY[i]))
        rightBoundary.append(rightEnd)

        # leftResult=[]
        # leftResult.append(leftBoundary)
        # rightResult=[]
        # rightResult.append(rightBoundary)
        # twoBoundary.append(leftResult)
        # twoBoundary.append(rightResult)
        twoBoundary.append(leftBoundary)
        twoBoundary.append(rightBoundary)
        return(twoBoundary)
        
    #获取左右两个边界的起点和终点坐标。
    def getBoundarySEPoint(self):
        result=[]#leftStart,leftEnd,rightStart,rightEnd
        leftStart=(0,0)
        leftEnd=(0,0)
        rightStart=(0,0)
        rightEnd=(0,0)
        if self.k=='+0':
            leftStart=(self.Start[0],self.Start[1]+self.Width/2)
            rightStart=(self.Start[0],self.Start[1]-self.Width/2)
        if self.k=='-0':
            leftStart=(self.Start[0],self.Start[1]-self.Width/2)
            rightStart=(self.Start[0],self.Start[1]+self.Width/2)
        if self.k=='+':
            leftStart=(self.Start[0]-self.Width/2,self.Start[1])
            rightStart=(self.Start[0]+self.Width/2,self.Start[1])
        if self.k=='-':
            leftStart=(self.Start[0]+self.Width/2,self.Start[1])
            rightStart=(self.Start[0]-self.Width/2,self.Start[1])
        if self.k1=='+0':
            leftEnd=(self.End[0],self.End[1]+self.Width/2)
            rightEnd=(self.End[0],self.End[1]-self.Width/2)
        if self.k1=='-0':
            leftEnd=(self.End[0],self.End[1]-self.Width/2)
            rightEnd=(self.End[0],self.End[1]+self.Width/2)
        if self.k1=='+':
            leftEnd=(self.End[0]-self.Width/2,self.End[1])
            rightEnd=(self.End[0]+self.Width/2,self.End[1])
        if self.k1=='-':
            leftEnd=(self.End[0]+self.Width/2,self.End[1])
            rightEnd=(self.End[0]-self.Width/2,self.End[1])
        result.append(leftStart)
        result.append(leftEnd)
        result.append(rightStart)
        result.append(rightEnd)
        return(result)

    def PointtoString(self,lst):
        # [[(-1.5, 0), (-1.5, 5.0), (-1.5, 10)], [(1.5, 0), (1.5, 5.0), (1.5, 10)]] 变成 [-1.5 0;-1.5 5.0;-1.5 10],[1.5 0;1.5 5.0;1.5 10]的字符串
        lst=[str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string


#如何制定startid
    def generate_road(self,f):
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a StraightRoad widget.')
        printAutoInd(f, '% Set the lanes.')
        printAutoInd(f, 'rrMap.Lanes(' + str(self.ID) + ') = roadrunner.hdmap.Lane();')
        
        printAutoInd(f, '[rrMap.Lanes(' + str(self.ID) + ').ID] = deal(\'Lane' + str(self.ID) + '\');')
        lanePointList=self.getlanepoint()
        lanePointStr=self.PointtoString(lanePointList)
        printAutoInd(f,'[rrMap.Lanes(' + str(self.ID) + ').Geometry] = deal(' + lanePointStr + ');')
        printAutoInd(f, '[rrMap.Lanes(' + str(self.ID) + ').TravelDirection] = deal(\'' + self.TravelDirection + '\');')
        printAutoInd(f, '[rrMap.Lanes(' + str(self.ID) + ').LaneType] = deal(\''+self.LaneType+'\');')

        #Boundary
        printAutoInd(f, '% Set the lane boundaries.')
        printAutoInd(f, 'rrMap.LaneBoundaries(' + str(self.BoundaryId1) + ') = roadrunner.hdmap.LaneBoundary();')
        printAutoInd(f, 'rrMap.LaneBoundaries(' + str(self.BoundaryId2) + ') = roadrunner.hdmap.LaneBoundary();')

        boundaryPointList=self.getboundarypoint()
        leftBoundaryPointList=boundaryPointList[0]
        rightBoundaryPointList=boundaryPointList[1]
        leftBoundaryPointStr=self.PointtoString(leftBoundaryPointList)
        rightBoundaryPointstr=self.PointtoString(rightBoundaryPointList)

        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId1) + ').ID] = deal(\'Boundary' + str(self.BoundaryId1) + '\');')
        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId2) + ').ID] = deal(\'Boundary' + str(self.BoundaryId2) + '\');')

        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId1) + ').Geometry] = deal(' + leftBoundaryPointStr + ');')
        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId2) + ').Geometry] = deal(' + rightBoundaryPointstr + ');')
         # 关联lane 与lane boundaries
        printAutoInd(f, '% Associate lanes and lane boundaries.')
        printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.ID) + '),"Boundary' + str(self.BoundaryId1) + '",Alignment="Forward");')
        printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.ID) + '),"Boundary'+ str(self.BoundaryId2) +'",Alignment="Forward");')
        printAutoInd(f, '% End of this widget')