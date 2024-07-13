from func.Object import Object
from func.printAuto import printAutoInd


class TrafficLight(Object):
    Geometry = (0, 0)  # 红绿灯添加的位置
    Direction = '0'  # 红绿灯添加的方向
    Type = 'Single'  # 红绿灯的类别
    offset = 0.5  # 红绿灯距离道路的间隔
    ObjectID = Object.ObjectID  # 维护有多少个Static Object 用于声明
    vertical_rod = {'length': 0.3,
                    'width': 0.3,
                    'height': 9,
                    'boxGrade': [0, 0, 0]
                    }  # 纵杆参数
    horizontal_rod = {'length': 3.8,
                      'width': 0.1,
                      'height': 1,
                      'absolute_height': 7.5,
                      'boxGrade': [0, 0, 0]
                      }  # 横杆参数
    light = {'length': 0.3,
             'width': 0.2,
             'height': 1,
             'boxGrade': [0, 0, 0],
             'light0XYZ': [0, 0.3, 7],
             'light2XYZ': [4.5, 0.1, 7.8],  # 定义XYZ方向上的余量
             'light3XYZ': [1.5, 0.2, 7.4]
             }  # 灯参数

    def __init__(self, dict):
        self.Geometry = dict.get('Geometry')
        self.Direction = dict.get('Direction')
        self.Type = dict.get('Type')
        self.ObjectID = Object.ObjectID
        self.vertical_rod['center'] = [self.Geometry[0], self.Geometry[1], 4.5]
        self.rotate()  # 旋转坐标参数
        # center1 代表最左端的灯
        # center2 代表中间的灯
        # center3 代表最右侧的灯

    # 根据Direction旋转坐标
    def rotate(self):  # 根据红绿灯的朝向 构建红绿灯
        print("正在进行旋转...")
        if self.Direction == '0':  # 横杆朝左 坐标角度不需要变换 直接赋值即可
            print("Direction == '0'")
            self.horizontal_rod['center'] = [self.Geometry[0] - self.horizontal_rod.get('length'), self.Geometry[1],
                                             self.horizontal_rod.get('absolute_height')]
            self.horizontal_rod['boxGrade'] = [0, 0, 0]
            self.light['center0'] = [self.Geometry[0], self.Geometry[1] - self.light.get('light0XYZ')[1],
                                     self.light.get('light0XYZ')[2]]
            self.light['center1'] = [self.Geometry[0] - self.horizontal_rod.get('length') * 2, self.Geometry[1],
                                     self.horizontal_rod.get('absolute_height') + self.light.get('height') / 2]
            self.light['center2'] = [self.Geometry[0] - self.light.get('light2XYZ')[0],
                                     self.Geometry[1] - self.light.get('light2XYZ')[1],
                                     self.light.get('light2XYZ')[2]]
            self.light['center3'] = [self.Geometry[0] - self.light.get('light3XYZ')[0],
                                     self.Geometry[1] - self.light.get('light3XYZ')[1],
                                     self.light.get('light3XYZ')[2]]
            self.light['boxGrade'] = [0, 0, 0]



        elif self.Direction == '1':  # 横杆朝上 横杆和红绿灯顺时针旋转90° 纵杆无需变化
            print("Direction == '1'")
            # 旋转横杆参数
            self.horizontal_rod['center'] = [self.Geometry[0], self.Geometry[1] + self.horizontal_rod.get('length'),
                                             self.horizontal_rod.get('absolute_height')]
            self.horizontal_rod['boxGrade'] = [0, 0, 270]
            # 旋转灯参数
            self.light['center0'] = [self.Geometry[0] - self.light.get('light0XYZ')[1], self.Geometry[1],
                                     self.light.get('light0XYZ')[2]]
            self.light['center1'] = [self.Geometry[0], self.Geometry[1] + self.horizontal_rod.get('length') * 2,
                                     self.horizontal_rod.get('absolute_height') + self.light.get('height') / 2]

            self.light['center2'] = [self.Geometry[0] - self.light.get('light2XYZ')[1],
                                     self.Geometry[1] + self.light.get('light2XYZ')[0],
                                     self.light.get('light2XYZ')[2]]
            self.light['center3'] = [self.Geometry[0] - self.light.get('light3XYZ')[1],
                                     self.Geometry[1] + self.light.get('light3XYZ')[0], self.light.get('light3XYZ')[2]]
            self.light['boxGrade'] = [0, 0, 270]


        elif self.Direction == '2':  # 横杆朝右
            print("Direction == '2'")
            # 旋转横杆参数
            self.horizontal_rod['center'] = [self.Geometry[0] + self.horizontal_rod.get('length'), self.Geometry[1],
                                             self.horizontal_rod.get('absolute_height')]
            self.horizontal_rod['boxGrade'] = [0, 0, 180]
            # 旋转灯参数
            self.light['center0'] = [self.Geometry[0], self.Geometry[1] + self.light.get('light0XYZ')[1],
                                     self.light.get('light0XYZ')[2]]
            self.light['center1'] = [self.Geometry[0] + self.horizontal_rod.get('length') * 2, self.Geometry[1],
                                     self.horizontal_rod.get('absolute_height') + self.light.get('height') / 2]
            self.light['center2'] = [self.Geometry[0] + self.light.get('light2XYZ')[0],
                                     self.Geometry[1] + self.light.get('light2XYZ')[1],
                                     self.light.get('light2XYZ')[2]]
            self.light['center3'] = [self.Geometry[0] + self.light.get('light3XYZ')[0],
                                     self.Geometry[1] + self.light.get('light3XYZ')[1],
                                     self.light.get('light3XYZ')[2]]
            self.light['boxGrade'] = [0, 0, 180]
        elif self.Direction == '3':  # 横杆朝下
            print("Direction == '3'")
            self.horizontal_rod['center'] = [self.Geometry[0], self.Geometry[1] - self.horizontal_rod.get('length'),
                                             self.horizontal_rod.get('absolute_height')]
            self.horizontal_rod['boxGrade'] = [0, 0, 90]
            self.light['center0'] = [self.Geometry[0] + self.light.get('light0XYZ')[1], self.Geometry[1],
                                     self.light.get('light0XYZ')[2]]
            self.light['center1'] = [self.Geometry[0], self.Geometry[1] - self.horizontal_rod.get('length') * 2,
                                     self.horizontal_rod.get('absolute_height') + self.light.get('height') / 2]
            self.light['center2'] = [self.Geometry[0] + self.light.get('light2XYZ')[1],
                                     self.Geometry[1] - self.light.get('light2XYZ')[0],
                                     self.light.get('light2XYZ')[2]]
            self.light['center3'] = [self.Geometry[0] + self.light.get('light3XYZ')[1],
                                     self.Geometry[1] - self.light.get('light3XYZ')[0], self.light.get('light3XYZ')[2]]
            self.light['boxGrade'] = [0, 0, 90]

        else:
            print("方向有误！")

    # 输出通用角度
    def output_grade(self, f):
        printAutoInd(f, 'geoAngle3 = mathworks.scenario.common.GeoAngle3;')
        printAutoInd(f, '[geoAngle3.roll,geoAngle3.pitch,geoAngle3.heading] = deal(0,0,90);')
        printAutoInd(f, 'geoOrientation3 = mathworks.scenario.common.GeoOrientation3;')
        printAutoInd(f, 'geoOrientation3.geo_angle = geoAngle3;')

    def generateByID(self, f, id):
        if id == 0:
            nowID = self.getID()
            printAutoInd(f, '[L_length,L_width,L_height] = deal({},{},{});'.format(self.light.get('length'),
                                                                                   self.light.get('width'),
                                                                                   self.light.get('height')))
            printAutoInd(f, 'LGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
            printAutoInd(f, 'LGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.light.get('center0')[0],
                                                                                  self.light.get('center0')[1],
                                                                                  self.light.get('center0')[2]))
            printAutoInd(f, 'LGeoOrientedBoundingBox.Dimension = [L_length L_width L_height/2];')
            self.output_grade(f)
            printAutoInd(f, 'LGeoOrientedBoundingBox.GeoOrientation = [deg2rad({}) deg2rad({}) deg2rad({})];'.format(
                self.light.get('boxGrade')[0], self.light.get('boxGrade')[1], self.light.get('boxGrade')[2]))
            printAutoInd(f, 'rrMap.StaticObjects(' + str(
                nowID) + ') = roadrunner.hdmap.StaticObject(ID=' + '"TrafficLight' + str(
                nowID) + '",Geometry=LGeoOrientedBoundingBox,ObjectTypeReference=Signal_3Light_Ref);')

        if id == 1:
            nowID = self.getID()
            printAutoInd(f, '[L_length,L_width,L_height] = deal({},{},{});'.format(self.light.get('length'),
                                                                                   self.light.get('width'),
                                                                                   self.light.get('height')))
            printAutoInd(f, 'LGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
            printAutoInd(f, 'LGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.light.get('center1')[0],
                                                                                  self.light.get('center1')[1],
                                                                                  self.light.get('center1')[2]))
            printAutoInd(f, 'LGeoOrientedBoundingBox.Dimension = [L_length L_width L_height/2];')
            self.output_grade(f)
            printAutoInd(f, 'LGeoOrientedBoundingBox.GeoOrientation = [deg2rad({}) deg2rad({}) deg2rad({})];'.format(
                self.light.get('boxGrade')[0], self.light.get('boxGrade')[1], self.light.get('boxGrade')[2]))
            printAutoInd(f, 'rrMap.StaticObjects(' + str(
                nowID) + ') = roadrunner.hdmap.StaticObject(ID=' + '"TrafficLight' + str(
                nowID) + '",Geometry=LGeoOrientedBoundingBox,ObjectTypeReference=Signal_3Light_Ref);')
        if id == 2:
            nowID = self.getID()
            printAutoInd(f, '[L_length,L_width,L_height] = deal({},{},{});'.format(self.light.get('length'),
                                                                                   self.light.get('width'),
                                                                                   self.light.get('height')))
            printAutoInd(f, 'LGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
            printAutoInd(f, 'LGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.light.get('center2')[0],
                                                                                  self.light.get('center2')[1],
                                                                                  self.light.get('center2')[2]))
            printAutoInd(f, 'LGeoOrientedBoundingBox.Dimension = [L_length L_width L_height/2];')
            self.output_grade(f)
            printAutoInd(f, 'LGeoOrientedBoundingBox.GeoOrientation = [deg2rad({}) deg2rad({}) deg2rad({})];'.format(
                self.light.get('boxGrade')[0], self.light.get('boxGrade')[1], self.light.get('boxGrade')[2]))
            printAutoInd(f, 'rrMap.StaticObjects(' + str(
                nowID) + ') = roadrunner.hdmap.StaticObject(ID=' + '"TrafficLight' + str(
                nowID) + '",Geometry=LGeoOrientedBoundingBox,ObjectTypeReference=Signal_3Light_Ref);')
        if id == 3:
            nowID = self.getID()
            printAutoInd(f, '[L_length,L_width,L_height] = deal({},{},{});'.format(self.light.get('length'),
                                                                                   self.light.get('width'),
                                                                                   self.light.get('height')))
            printAutoInd(f, 'LGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
            printAutoInd(f, 'LGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.light.get('center3')[0],
                                                                                  self.light.get('center3')[1],
                                                                                  self.light.get('center3')[2]))
            printAutoInd(f, 'LGeoOrientedBoundingBox.Dimension = [L_length L_width L_height/2];')
            self.output_grade(f)
            printAutoInd(f, 'LGeoOrientedBoundingBox.GeoOrientation = [deg2rad({}) deg2rad({}) deg2rad({})];'.format(
                self.light.get('boxGrade')[0], self.light.get('boxGrade')[1], self.light.get('boxGrade')[2]))
            printAutoInd(f, 'rrMap.StaticObjects(' + str(
                nowID) + ') = roadrunner.hdmap.StaticObject(ID=' + '"TrafficLight' + str(
                nowID) + '",Geometry=LGeoOrientedBoundingBox,ObjectTypeReference=Signal_3Light_Ref);')

    def getID(self):
        ID = Object.ObjectID
        Object.ObjectID += 1
        return ID

    def generate_light(self, f):
        printAutoInd(f, '% Here is a Traffic Light widget.')
        printAutoInd(f, "% set {} Traffic Light".format(self.Type))
        # 设置纵杆
        nowID = self.getID()
        printAutoInd(f, '% 设置纵杆')
        # [variable1, variable2, variable3] = deal(value1, value2, value3);
        printAutoInd(f, '[V_length,V_width,V_height] = deal({},{},{});'.format(self.vertical_rod.get('length'),
                                                                               self.vertical_rod.get('width'),
                                                                               self.vertical_rod.get('height')))
        printAutoInd(f, 'VGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
        printAutoInd(f, 'VGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.vertical_rod.get('center')[0],
                                                                              self.vertical_rod.get('center')[1],
                                                                              self.vertical_rod.get('center')[2]))
        printAutoInd(f, 'VGeoOrientedBoundingBox.Dimension = [V_length V_width V_height/2];')
        self.output_grade(f)
        printAutoInd(f, 'VGeoOrientedBoundingBox.GeoOrientation = [deg2rad(0) deg2rad(0) deg2rad(0)];')
        printAutoInd(f, 'rrMap.StaticObjects(' + str(
            nowID) + ') = roadrunner.hdmap.StaticObject(ID=' + '"TrafficLight' + str(
            nowID) + '",Geometry=VGeoOrientedBoundingBox,ObjectTypeReference=Signal_Post_Ref);')
        if self.Type != 'SingleLane':
            # 设置横杆
            nowID = self.getID()
            printAutoInd(f, ' ')
            printAutoInd(f, '% 设置横杆')
            printAutoInd(f, '[H_length,H_width,H_height] = deal({},{},{});'.format(self.horizontal_rod.get('length'),
                                                                                   self.horizontal_rod.get('width'),
                                                                                   self.horizontal_rod.get('height')))
            printAutoInd(f, 'HGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
            printAutoInd(f, 'HGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.horizontal_rod.get('center')[0],
                                                                                  self.horizontal_rod.get('center')[1],
                                                                                  self.horizontal_rod.get('center')[2]))
            printAutoInd(f, 'HGeoOrientedBoundingBox.Dimension = [H_length H_width H_height/2];')
            self.output_grade(f)
            # printAutoInd(f, 'HGeoOrientedBoundingBox.GeoOrientation = [deg2rad(0) deg2rad(0) deg2rad(0)];')
            printAutoInd(f, 'HGeoOrientedBoundingBox.GeoOrientation = [deg2rad({}) deg2rad({}) deg2rad({})];'.format(
                self.horizontal_rod.get('boxGrade')[0], self.horizontal_rod.get('boxGrade')[1],
                self.horizontal_rod.get('boxGrade')[2]))
            printAutoInd(f, 'rrMap.StaticObjects(' + str(
                nowID) + ') = roadrunner.hdmap.StaticObject(ID=' + '"TrafficLight' + str(
                nowID) + '",Geometry=HGeoOrientedBoundingBox,ObjectTypeReference=Signal_MastArm_Ref);')
            printAutoInd(f, ' ')
            printAutoInd(f, '% 设置红绿灯')
        # 根据红绿灯进行选择生成
        if self.Type == 'Single':  # 一灯红绿灯
            self.generateByID(f, 2)
            printAutoInd(f, ' ')
        if self.Type == 'Double':  # 二灯红绿灯
            self.generateByID(f, 1)
            printAutoInd(f, ' ')
            self.generateByID(f, 2)
            printAutoInd(f, ' ')
        if self.Type == 'Triple':
            self.generateByID(f, 1)
            printAutoInd(f, ' ')
            self.generateByID(f, 2)
            printAutoInd(f, ' ')
            self.generateByID(f, 3)
            printAutoInd(f, ' ')
        if self.Type == 'SingleLane':
            self.generateByID(f, 0)
            printAutoInd(f, ' ')

        return

# dict1 = {'Geometry': (3, 50),
#          'Direction': 0,
#          'Function': '+',
#          'K': '+',
#          'Type': 'Single'}
# tl = TrafficLight(dict1)
#
# print(tl.vertical_rod)
# print(tl.horizontal_rod)
# print(tl.light)
