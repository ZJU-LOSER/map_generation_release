import random

# 定义两侧的barrier可选类型
SideType = ['HighwayFence', 'LargeFence', 'FShapeBarrier', 'BridgeRailing', 'ConstantSlopeBarrier', 'Fence',
            'GuardRail', 'GuardRail02', 'JerseyBarrier', 'MetalFencePost01', 'StoneRockyWall', 'WoodenFence01',
            'WoodenFence02', 'HighwayBorderwall01']
# 定义道路中间barrier可选类型
MiddleType = ['BridgeRailing', 'ConstantSlopeBarrier', 'Fence', 'GuardRail02', 'JerseyBarrier', 'MetalFencePost01',
              'WoodenFence01', 'WoodenFence02','FShapeBarrier']


def getMiddleType(sideType):
    global middleType # 道路中央barrier类型
    global MiddleTypeList # 道路中央barrier类型列表
    if sideType == 'BridgeRailing':
        MiddleTypeList = ['BridgeRailing','ConstantSlopeBarrier','JerseyBarrier','MetalFencePost01','FShapeBarrier']
    elif sideType in ['LargeFence','FShapeBarrier','ConstantSlopeBarrier','JerseyBarrier','HighwayFence']:
        MiddleTypeList = ['BridgeRailing','ConstantSlopeBarrier','Fence','FShapeBarrier','GuardRail02','JerseyBarrier','MetalFencePost01']
    elif sideType == 'GuardRail' or sideType == 'GuardRail02':
        MiddleTypeList = ['ConstantSlopeBarrier','Fence','FShapeBarrier','GuardRail','GuardRail02','JerseyBarrier','MetalFencePost01']
    elif sideType in ['Fence','MetalFencePost01']:
        MiddleTypeList = ['ConstantSlopeBarrier','Fence','FShapeBarrier','GuardRail','GuardRail02','JerseyBarrier','MetalFencePost01','WoodenFence02']
    elif sideType == 'HighwayBorderwall01':
        MiddleTypeList = ['ConstantSlopeBarrier','Fence','FShapeBarrier','HighwayBorderwall01','JerseyBarrier','MetalFencePost01']
    elif sideType in ['WoodenFence01','WoodenFence02']:
        MiddleTypeList = ['ConstantSlopeBarrier','Fence','FShapeBarrier','GuardRail','GuardRail02','JerseyBarrier','MetalFencePost01','WoodenFence01','WoodenFence02']
    elif sideType == 'StoneRockyWall':
        MiddleTypeList = ['ConstantSlopeBarrier','Fence','FShapeBarrier','GuardRail','GuardRail02','JerseyBarrier','StoneRockyWall','MetalFencePost01']

    middleType = random.choice(MiddleTypeList)

    return middleType

