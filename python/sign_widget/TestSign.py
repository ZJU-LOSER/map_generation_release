from generation_test.build_barrier import BuildRoad
from sign_widget.sign import Sign
from sign_widget.signGeneration import signGenerationClass
from straigntlane_widget.straightlane import StraightLane


def signGeneration(f):
    sign1 = {'Geometry': (-37.5, 90),
             'Direction': '2',
             'Function': '+',
             'K': '+',
             'Type': 'Accessible'}
    dict1 = {'Start': (20, -200),
              'W': 3.5,
              'R': 10,
              'StartLaneID': 1,
              'StartBoundaryID': 1,
              'LaneNumber': 8,
              'BoundaryNumber': 12,
              'LaneAssetType': {'Boundary1': 'SW',
                                'Boundary2': 'DW',
                                'Boundary3': 'SDY',
                                'Boundary4': 'DW',
                                'Boundary5': 'SW',
                                'Boundary6': 'SW',
                                'Boundary7': 'SW',
                                'Boundary8': 'SW',
                                'Boundary9': 'SY',
                                'Boundary10': 'SW',
                                'Boundary11': 'SW',
                                'Boundary12': 'SW',
                                },  # boundary的个数根据组件类型得出
              'Function': '+',
              'K': '+',
              'Type': 'fork',
              'Flag': '四车道左右弯曲岔路'}
    SL = BuildRoad(dict1)
    SL.generate_road(f)
    roadBoundary = SL.getboundarypoint()
    dict1['roadBoundary'] = roadBoundary
    print(dict1)
    #
    Sign1 = signGenerationClass(dict1)
    Sign1.buildSign(f)
