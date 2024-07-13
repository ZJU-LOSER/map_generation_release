import random

from Intersection_widget.intersection import Intersection
from TJunction_widget.tJunction import tJunction
from Ulane_widget.ulane import ULane
from barrier_widget.barrier import Barrier
from curve_widget.curve import Curve
from fork_widget.fork import Fork
from barrier_widget.barrierType import SideType, MiddleType, getMiddleType
from laneswitch_widget.laneswitch import LaneSwitch
from roundabout_widget.roundabout import Roundabout
from straigntlane_widget.straightlane import StraightLane


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


def test_barrier(f,dict1):
    # dict1 = {'Start': (-40, -40),
    #      'LW': (20, 3.5),
    #      'LaneNumber': 4,
    #      'BoundaryNumber':5,
    #      'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW','Boundary3':'SDY','Boundary4':'DW','Boundary5':'SW'},
    #      'K':'+',
    #      'Type': 'straightlane',
    #      'Flag':'双黄实线实虚四车道'}

    Widget = BuildRoad(dict1)
    Widget.generate_road(f)
    barrier_dict = {
        'laneType': Widget.Type,
       # 'boundaryPoint': Widget.getboundarypoint(),
        'sideType': random.choice(SideType),
        'middleType': random.choice(MiddleType),
        'Flag': Widget.Flag,
    }
    barrier_dict['middleType'] = getMiddleType(barrier_dict['sideType'])
    if Widget.Type == 'tJunction':
        barrier_dict['specialBarrier'] = Widget.get_SpecialBarrier()
        barrier_dict['boundaryPoint'] = Widget.getLaneInfoList()[1] # tjunction 通过getLaneInfoList获取边界信息
    elif Widget.Type == 'intersection':
        barrier_dict['boundaryPoint'] = Widget.getLaneInfoList()[1]
    else:
        barrier_dict['boundaryPoint'] = Widget.getboundarypoint()

    #
    barrier = Barrier(barrier_dict)
    barrier.generate_barrier(f)
