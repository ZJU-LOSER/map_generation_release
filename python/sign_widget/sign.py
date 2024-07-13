from func.Object import Object
from func.printAuto import printAutoInd


class Sign(Object):
    Geometry = (0, 0)  # sign添加的位置
    Direction = '0'  # sign添加的方向
    Type = 'Speed'  # sign的类别
    SignID = Object.SignID
    ObjectID = Object.ObjectID
    prop = {
        'length': 0.035,
        'width': 0.035,
        'height': 3,
        'boxGrade': [0, 0, 0]
    }
    sign = {
        'length': 0.1,
        'width': 0.5,
        'height': 1,
        'boxGrade': [0, 0, 270]
    }
    SignType = ['Sign_215_Ref']

    def __init__(self, dict):
        self.Geometry = dict.get('Geometry')
        self.Direction = dict.get('Direction')
        self.Type = dict.get('Type')
        self.SignID = Object.SignID
        self.ObjectID = Object.ObjectID
        self.prop['center'] = [self.Geometry[0], self.Geometry[1],
                               self.prop.get('height') / 2]
        self.rotate()  # 根据方向初始化坐标

    def rotate(self):
        if self.Direction == '0':
            self.sign['boxGrade'] = [0, 0, 270]
            self.sign['center'] = [self.Geometry[0], self.Geometry[1] - self.prop.get('width'), self.prop.get('height')]
        elif self.Direction == '1':
            self.sign['center'] = [self.Geometry[0] - self.prop.get('width'), self.Geometry[1], self.prop.get('height')]
            self.sign['boxGrade'] = [0, 0, 180]
        elif self.Direction == '2':
            self.sign['center'] = [self.Geometry[0], self.Geometry[1] + self.prop.get('width'), self.prop.get('height')]
            self.sign['boxGrade'] = [0, 0, 90]
        elif self.Direction == '3':
            self.sign['center'] = [self.Geometry[0] + self.prop.get('width'), self.Geometry[1], self.prop.get('height')]
            self.sign['boxGrade'] = [0, 0, 0]
        else:
            print("方向有误...")

    def output_grade(self, f):
        printAutoInd(f, 'geoAngle3 = mathworks.scenario.common.GeoAngle3;')
        printAutoInd(f, '[geoAngle3.roll,geoAngle3.pitch,geoAngle3.heading] = deal(0,0,90);')
        printAutoInd(f, 'geoOrientation3 = mathworks.scenario.common.GeoOrientation3;')
        printAutoInd(f, 'geoOrientation3.geo_angle = geoAngle3;')

    def getID(self, flag):
        global ID
        if flag == 'object':
            ID = Object.ObjectID
            Object.ObjectID += 1
        if flag == 'sign':
            ID = Object.SignID
            Object.SignID += 1
        return ID

    def generate_sign(self, f):
        printAutoInd(f, '% Here is a Sign widget.')
        # 设置prop
        nowID = self.getID('object')  # 获得此时的 object ID
        printAutoInd(f, '% 设置 prop')
        printAutoInd(f, '[P_length,P_width,P_height] = deal({},{},{});'.format(self.prop.get('length'),
                                                                               self.prop.get('width'),
                                                                               self.prop.get('height')))
        printAutoInd(f, 'PGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
        printAutoInd(f, 'PGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.prop.get('center')[0],
                                                                              self.prop.get('center')[1],
                                                                              self.prop.get('center')[2]))
        printAutoInd(f, 'PGeoOrientedBoundingBox.Dimension = [P_length P_width P_height/2];')
        self.output_grade(f)
        printAutoInd(f, 'PGeoOrientedBoundingBox.GeoOrientation = [deg2rad({}) deg2rad({}) deg2rad({})];'.format(
            self.prop.get('boxGrade')[0], self.prop.get('boxGrade')[1], self.prop.get('boxGrade')[2]))
        printAutoInd(f, 'rrMap.StaticObjects(' + str(
            nowID) + ') = roadrunner.hdmap.StaticObject(ID=' + '"TrafficLight' + str(
            nowID) + '",Geometry=PGeoOrientedBoundingBox,ObjectTypeReference=Metal_CylinderPost_Ref);')

        # 设置sign
        nowID = self.getID('sign')
        printAutoInd(f, '% 设置 sign')
        printAutoInd(f, '[S_length,S_width,S_height] = deal({},{},{});'.format(self.sign.get('length'),
                                                                               self.sign.get('width'),
                                                                               self.sign.get('height')))
        printAutoInd(f, 'SGeoOrientedBoundingBox = roadrunner.hdmap.GeoOrientedBoundingBox;')
        printAutoInd(f, 'SGeoOrientedBoundingBox.Center = [{} {} {}];'.format(self.sign.get('center')[0],
                                                                              self.sign.get('center')[1],
                                                                              self.sign.get('center')[2]))
        printAutoInd(f, 'SGeoOrientedBoundingBox.Dimension = [S_length S_width S_height/2];')
        self.output_grade(f)
        printAutoInd(f, 'SGeoOrientedBoundingBox.GeoOrientation = [deg2rad({}) deg2rad({}) deg2rad({})];'.format(
            self.sign.get('boxGrade')[0], self.sign.get('boxGrade')[1], self.sign.get('boxGrade')[2]))
        printAutoInd(f, 'rrMap.Signs(' + str(
            nowID) + ') = roadrunner.hdmap.Sign(ID=' + '"Sign' + str(
            nowID) + '",Geometry=SGeoOrientedBoundingBox,SignTypeReference={});'.format(self.Type + '_Ref'))
