# 指示牌种类的选择生成
def getSignType(roadType, roadFlag):
    global signTypeList
    signTypeList = {
        'Speed': [],
        'Vehicle': [],
        'Direction': [],
        'Accessible': [],
    }  # 分别对应 Speed Vehicle Direction Accessible 四种类型的道路牌
    if roadType == 'straightlane':
        if roadFlag == '单行道':
            signTypeList['Speed'] = ['Sign_274_5', 'Sign_274_10', 'Sign_274_20', 'Sign_274_30', 'Sign_274_40',
                                     'Sign_274_50', 'Sign_274_60', 'Sign_274_70', 'Sign_274_80', 'Sign_274_200',
                                     'Sign_274_110', 'Sign_274_120', 'Sign_274_130', 'Sign_275_30']
            signTypeList['Vehicle'] = []
            signTypeList['Direction'] = ['Sign_209_30']
            signTypeList['Accessible'] = []
        if roadFlag == '':
            return



