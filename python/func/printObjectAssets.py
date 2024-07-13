from func.printAuto import printAutoInd


def printObjectAsserts(f):
    printAutoInd(f, '% The following are the common parts of the various components.')
    printAutoInd(f, '% We define a new map file and import all possible assets in case of emergency.')
    # printAutoInd(f, 'rrMap = roadrunnerHDMap;')
    printAutoInd(f, '')
    # Static Object
    printAutoInd(f,
                 'Signal_Post = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Props/Signals/Signal_Post_35ft.fbx_rrx");')
    printAutoInd(f,
                 'Signal_MastArm = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Props/Signals/Signal_MastArm_45ft.fbx");')
    printAutoInd(f,
                 'Signal_3Light = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Props/Signals/Signal_3Light_Bare01.fbx_rrx");')
    printAutoInd(f,
                 'Metal_CylinderPost = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Props/Signals/Metal_CylinderPost_10ft.fbx_rrx");')
    printAutoInd(f,
                 'rrMap.StaticObjectTypes(1) = roadrunner.hdmap.StaticObjectType(ID="Signal_Post",AssetPath=Signal_Post);')
    printAutoInd(f,
                 'rrMap.StaticObjectTypes(2) = roadrunner.hdmap.StaticObjectType(ID="Signal_MastArm",AssetPath=Signal_MastArm);')
    printAutoInd(f,
                 'rrMap.StaticObjectTypes(3) = roadrunner.hdmap.StaticObjectType(ID="Signal_3Light",AssetPath=Signal_3Light);')
    printAutoInd(f,
                 'rrMap.StaticObjectTypes(4) = roadrunner.hdmap.StaticObjectType(ID="Metal_CylinderPost",AssetPath=Metal_CylinderPost);')

    # Sign
    printAutoInd(f,
                 'Stop_Sign = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_206.svg_rrx");')
    printAutoInd(f,
                 'Sign_208 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_208.svg_rrx");')
    printAutoInd(f,
                 'Sign_209_10 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_209-10.svg_rrx");')
    printAutoInd(f,
                 'Sign_209_20 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_209-20.svg_rrx");')
    printAutoInd(f,
                 'Sign_209_30 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_209-30.svg_rrx");')
    printAutoInd(f,
                 'Sign_209_31 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_209-31.svg_rrx");')
    printAutoInd(f,
                 'Sign_211_10 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_211-10.svg_rrx");')
    printAutoInd(f,
                 'Sign_211_20 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_211-20.svg_rrx");')
    printAutoInd(f,
                 'Sign_214_10 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_214-10.svg_rrx");')
    printAutoInd(f,
                 'Sign_214_20 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_214-20.svg_rrx");')
    printAutoInd(f,
                 'Sign_215 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Signs/Germany/Regulatory Signs/Sign_215.svg_rrx");')
    printAutoInd(f, 'rrMap.SignTypes(1) = roadrunner.hdmap.SignType(ID="Stop_Sign",AssetPath=Stop_Sign);')
    printAutoInd(f, 'rrMap.SignTypes(2) = roadrunner.hdmap.SignType(ID="Sign_208",AssetPath=Sign_208);')
    printAutoInd(f, 'rrMap.SignTypes(3) = roadrunner.hdmap.SignType(ID="Sign_209_10",AssetPath=Sign_209_10);')
    printAutoInd(f, 'rrMap.SignTypes(4) = roadrunner.hdmap.SignType(ID="Sign_209_20",AssetPath=Sign_209_20);')
    printAutoInd(f, 'rrMap.SignTypes(5) = roadrunner.hdmap.SignType(ID="Sign_209_30",AssetPath=Sign_209_30);')
    printAutoInd(f, 'rrMap.SignTypes(6) = roadrunner.hdmap.SignType(ID="Sign_209_31",AssetPath=Sign_209_31);')
    printAutoInd(f, 'rrMap.SignTypes(7) = roadrunner.hdmap.SignType(ID="Sign_211_10",AssetPath=Sign_211_10);')
    printAutoInd(f, 'rrMap.SignTypes(8) = roadrunner.hdmap.SignType(ID="Sign_211_20",AssetPath=Sign_211_20);')
    printAutoInd(f, 'rrMap.SignTypes(9) = roadrunner.hdmap.SignType(ID="Sign_214_10",AssetPath=Sign_214_10);')
    printAutoInd(f, 'rrMap.SignTypes(10) = roadrunner.hdmap.SignType(ID="Sign_214_20",AssetPath=Sign_214_20);')
    printAutoInd(f, 'rrMap.SignTypes(11) = roadrunner.hdmap.SignType(ID="Sign_215",AssetPath=Sign_215);')

    # Barrier
    printAutoInd(f,
                 'HighwayFence = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/HighwayFence01.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(1) = roadrunner.hdmap.BarrierType(ID="HighwayFence",ExtrusionPath=HighwayFence);')
    printAutoInd(f,
                 'LargeFence = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/LargeFence01.rrext");')
    printAutoInd(f, 'rrMap.BarrierTypes(2) = roadrunner.hdmap.BarrierType(ID="LargeFence",ExtrusionPath=LargeFence);')
    printAutoInd(f,
                 'FShapeBarrier = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/FShapeBarrier.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(3) = roadrunner.hdmap.BarrierType(ID="FShapeBarrier",ExtrusionPath=FShapeBarrier);')
    printAutoInd(f,
                 'BridgeRailing = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/BridgeRailing.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(4) = roadrunner.hdmap.BarrierType(ID="BridgeRailing",ExtrusionPath=BridgeRailing);')
    printAutoInd(f,
                 'ConstantSlopeBarrier = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/ConstantSlopeBarrier.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(5) = roadrunner.hdmap.BarrierType(ID="ConstantSlopeBarrier",ExtrusionPath=ConstantSlopeBarrier);')
    printAutoInd(f,
                 'Fence = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/Fence.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(6) = roadrunner.hdmap.BarrierType(ID="Fence",ExtrusionPath=Fence);')
    printAutoInd(f,
                 'GuardRail = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/GuardRail.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(7) = roadrunner.hdmap.BarrierType(ID="GuardRail",ExtrusionPath=GuardRail);')
    printAutoInd(f,
                 'GuardRail02 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/GuardRail02.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(8) = roadrunner.hdmap.BarrierType(ID="GuardRail02",ExtrusionPath=GuardRail02);')
    printAutoInd(f,
                 'JerseyBarrier = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/JerseyBarrier.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(9) = roadrunner.hdmap.BarrierType(ID="JerseyBarrier",ExtrusionPath=JerseyBarrier);')
    printAutoInd(f,
                 'MetalFencePost01 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/MetalFencePost01.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(10) = roadrunner.hdmap.BarrierType(ID="MetalFencePost01",ExtrusionPath=MetalFencePost01);')
    printAutoInd(f,
                 'StoneRockyWall = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/StoneRockyWall.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(11) = roadrunner.hdmap.BarrierType(ID="StoneRockyWall",ExtrusionPath=StoneRockyWall);')
    printAutoInd(f,
                 'WoodenFence01 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/WoodenFence01.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(12) = roadrunner.hdmap.BarrierType(ID="WoodenFence01",ExtrusionPath=WoodenFence01);')
    printAutoInd(f,
                 'WoodenFence02 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/WoodenFence02.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(13) = roadrunner.hdmap.BarrierType(ID="WoodenFence02",ExtrusionPath=WoodenFence02);')
    printAutoInd(f,
                 'HighwayBorderwall01 = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Extrusions/HighwayBorderwall01.rrext");')
    printAutoInd(f,
                 'rrMap.BarrierTypes(14) = roadrunner.hdmap.BarrierType(ID="HighwayBorderwall01",ExtrusionPath=HighwayBorderwall01);')

    # Barrier Ref
    printAutoInd(f, 'HighwayFence_Ref = roadrunner.hdmap.Reference(ID="HighwayFence");')
    printAutoInd(f, 'LargeFence_Ref = roadrunner.hdmap.Reference(ID="LargeFence");')
    printAutoInd(f, 'FShapeBarrier_Ref = roadrunner.hdmap.Reference(ID="FShapeBarrier");')
    printAutoInd(f, 'BridgeRailing_Ref = roadrunner.hdmap.Reference(ID="BridgeRailing");')
    printAutoInd(f, 'ConstantSlopeBarrier_Ref = roadrunner.hdmap.Reference(ID="ConstantSlopeBarrier");')
    printAutoInd(f, 'Fence_Ref = roadrunner.hdmap.Reference(ID="Fence");')
    printAutoInd(f, 'GuardRail_Ref = roadrunner.hdmap.Reference(ID="GuardRail");')
    printAutoInd(f, 'GuardRail02_Ref = roadrunner.hdmap.Reference(ID="GuardRail02");')
    printAutoInd(f, 'JerseyBarrier_Ref = roadrunner.hdmap.Reference(ID="JerseyBarrier");')
    printAutoInd(f, 'MetalFencePost01_Ref = roadrunner.hdmap.Reference(ID="MetalFencePost01");')
    printAutoInd(f, 'StoneRockyWall_Ref = roadrunner.hdmap.Reference(ID="StoneRockyWall");')
    printAutoInd(f, 'WoodenFence01_Ref = roadrunner.hdmap.Reference(ID="WoodenFence01");')
    printAutoInd(f, 'WoodenFence02_Ref = roadrunner.hdmap.Reference(ID="WoodenFence02");')
    printAutoInd(f, 'HighwayBorderwall01_Ref = roadrunner.hdmap.Reference(ID="HighwayBorderwall01");')

    # Static Object Ref
    printAutoInd(f, 'Signal_Post_Ref = roadrunner.hdmap.Reference(ID="Signal_Post");')
    printAutoInd(f, 'Signal_MastArm_Ref = roadrunner.hdmap.Reference(ID="Signal_MastArm");')
    printAutoInd(f, 'Signal_3Light_Ref = roadrunner.hdmap.Reference(ID="Signal_3Light");')
    printAutoInd(f, 'Metal_CylinderPost_Ref = roadrunner.hdmap.Reference(ID="Metal_CylinderPost");')

    # Sign Ref
    printAutoInd(f, 'Stop_Sign_Ref = roadrunner.hdmap.Reference(ID="Stop_Sign");')
    printAutoInd(f, 'Sign_208_Ref = roadrunner.hdmap.Reference(ID="Sign_208");')
    printAutoInd(f, 'Sign_209_10_Ref = roadrunner.hdmap.Reference(ID="Sign_209_10");')
    printAutoInd(f, 'Sign_209_20_Ref = roadrunner.hdmap.Reference(ID="Sign_209_20");')
    printAutoInd(f, 'Sign_209_30_Ref = roadrunner.hdmap.Reference(ID="Sign_209_30");')
    printAutoInd(f, 'Sign_209_31_Ref = roadrunner.hdmap.Reference(ID="Sign_209_31");')
    printAutoInd(f, 'Sign_211_10_Ref = roadrunner.hdmap.Reference(ID="Sign_211_10");')
    printAutoInd(f, 'Sign_211_20_Ref = roadrunner.hdmap.Reference(ID="Sign_211_20");')
    printAutoInd(f, 'Sign_214_10_Ref = roadrunner.hdmap.Reference(ID="Sign_214_10");')
    printAutoInd(f, 'Sign_214_20_Ref = roadrunner.hdmap.Reference(ID="Sign_214_20");')
    printAutoInd(f, 'Sign_215_Ref = roadrunner.hdmap.Reference(ID="Sign_215");')
