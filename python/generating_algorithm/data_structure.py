import json
import re
from straigntlane_widget import StraightLaneLibrary as st
from Ulane_widget import ULaneLibrary as ul
from curve_widget import curvelibrary as cur
from laneswitch_widget import LaneSwitchLibrary as ls
from Intersection_widget import intersectionlibrary as ins
from roundabout_widget import roundaboutlibrary as rdb
from fork_widget import forklibrary as fk
from TJunction_widget import tJunctionLibrary as tj

str_dic_mapping = {
    'straightlane': {
        '单行道': st.dict1,
        '单向虚线双行道': st.dict2,
        '单向实线双行道': st.dict3,
        '单向虚实线双行道': st.dict4,
        '单向双实线双行道': st.dict5,
        '双向虚线双行道': st.dict6,
        '双向实线双行道': st.dict7,
        '双向虚实线双行道': st.dict8,
        '双向双实线双行道': st.dict9,
        '一前行虚白线虚黄线三行道': st.dict10,
        '一前行实白线虚黄线三行道': st.dict11,
        '一前行虚白线实黄线三行道': st.dict12,
        '一前行实白线实黄线三行道': st.dict13,
        '二前行虚黄线虚白线三行道': st.dict14,
        '二前行虚黄线实白线三行道': st.dict15,
        '二前行实黄线虚白线三行道': st.dict16,
        '二前行实黄线实白线三行道': st.dict17,
        '双黄实线虚虚四车道': st.dict18,
        '双黄实线实实四车道': st.dict19,
        '双黄实线虚实四车道': st.dict20,
        '双黄实线实虚四车道': st.dict21,
        '双实线虚虚虚虚六车道': st.dict22,
        '双实线实实实实六车道': st.dict23,
        '双实线虚虚实实六车道': st.dict24,
    },
    'curve': {
        # 没有补充完
        '单行道': cur.dict1_0,
        '单向虚线双行道': cur.dict2_0,
        '单向实线双行道': cur.dict3_0,
        '单向虚实线双行道': cur.dict4_0,
        '单向双实线双行道': cur.dict5_0,
        '双向虚线双行道': cur.dict6_0,
        '双向实线双行道': cur.dict7_0,
        '双向虚实线双行道': cur.dict8_0,
        '双向双实线双行道': cur.dict9_0,
        '一前行虚白线虚黄线三行道': cur.dict10_0,
        '一前行实白线虚黄线三行道': cur.dict11_0,
        '一前行虚白线实黄线三行道': cur.dict12_0,
        '一前行实白线实黄线三行道': cur.dict13_0,
        '二前行虚黄线虚白线三行道': cur.dict14_0,
        '二前行虚黄线实白线三行道': cur.dict15_0,
        '二前行实黄线虚白线三行道': cur.dict16_0,
        '二前行实黄线实白线三行道': cur.dict17_0,
        '双黄实线虚虚四车道': cur.dict18_0,
        '双黄实线实实四车道': cur.dict19_0,
        '双黄实线虚实四车道': cur.dict20_0,
        '双黄实线实虚四车道': cur.dict21_0,
    },
    'fork': {
        '单车道右弯曲并入单向双车道': fk.dict1,
        '单车道右弯曲并入双向双车道': fk.dict2,
        '单车道右弯曲并入二前行三车道': fk.dict3,
        '单车道右弯曲并入一前行三车道': fk.dict4,
        '单车道右弯曲并入四车道': fk.dict5,
        '单车道左弯曲并入单向双车道': fk.dict6,
        '单向双车道右弯曲并入二前行三车道': fk.dict7,
        '双向双车道右弯曲并入一前行三车道': fk.dict8,
        '单向双车道右弯曲并入四车道': fk.dict9,
        '双向双车道左弯曲并入二前行三车道': fk.dict10,
        '二前行三车道右弯曲并入四车道': fk.dict11,
        '一前行三车道左弯曲并入四车道': fk.dict12,
        '单向双车道右弯曲岔路': fk.dict13,
        '双向双车道右弯曲岔路': fk.dict14,
        '一前行三车道右弯曲岔路': fk.dict15,
        '二前行三车道一右弯曲岔路': fk.dict16,
        '二前行三车道二右弯曲岔路': fk.dict17,
        '一前行三车道左右弯曲岔路': fk.dict18,
        '二前行三车道左右弯曲岔路': fk.dict19,
        '四车道一右弯曲岔路': fk.dict20,
        '四车道二右弯曲岔路': fk.dict21,
        '四车道左右弯曲岔路': fk.dict22

    },
    'intersection': {
        '双向双车道十字路口': ins.Intersectiondict1,
        '四车道十字路口': ins.Intersectiondict2,
        '六车道十字路口': ins.Intersectiondict3,
    },
    'laneswitch': {
        '1*2左': ls.dict1,
        '1*2右': ls.dict13,
        '2*1左': ls.dict2,
        '2*1右': ls.dict14,
        '2*3左': ls.dict3,
        '2*3右': ls.dict4,
        '3*2左': ls.dict5,
        '3*2右': ls.dict6,
        '3*4右': ls.dict7,
        '3*4左': ls.dict8,
        '4*3左': ls.dict9,
        '4*3右': ls.dict10,
        '4*6': ls.dict11,
        '6*4': ls.dict12,

    },
    'tJunction': {
        '单向车道转双向双车道': tj.Jdict1,
        '单向车道转双向三车道一': tj.Jdict2,
        '单向车道转双向三车道二': tj.Jdict3,
        '单向车道转双向四车道': tj.Jdict4,
        '同向双车道转双向双车道': tj.Jdict5,
        '同向双车道转双向三车道一': tj.Jdict6,
        '同向双车道转双向三车道二': tj.Jdict7,
        '同向双车道转双向四车道': tj.Jdict8,
        '双向双车道转双向双车道': tj.Jdict9,
        '双向双车道转双向三车道一': tj.Jdict10,
        '双向双车道转双向三车道二': tj.Jdict11,
        '双向双车道转双向四车道': tj.Jdict12,
        '双向三车道一转双向双车道': tj.Jdict13,
        '双向三车道一转双向三车道一': tj.Jdict14,
        '双向三车道一转双向三车道二': tj.Jdict15,
        '双向三车道一转双向四车道': tj.Jdict16,
        '双向三车道二转双向双车道': tj.Jdict17,
        '双向三车道二转双向三车道一': tj.Jdict18,
        '双向三车道二转双向三车道二': tj.Jdict19,
        '双向三车道二转双向四车道': tj.Jdict20,
        '双向四车道转双向双车道': tj.Jdict21,
        '双向四车道转双向三车道一': tj.Jdict22,
        '双向四车道转双向三车道二': tj.Jdict23,
        '双向四车道转双向四车道': tj.Jdict24,
        '双向双车道转同向双车道': tj.Jdict25

    },
    'ulane': {
        '单行道': ul.dict1_0,
        '单向虚线双行道': ul.dict2_0,
        '单向实线双行道': ul.dict3_0,
        '单向虚实线双行道': ul.dict4_0,
        '单向双实线双行道': ul.dict5_0,
        '双向虚线双行道': ul.dict6_0,
        '双向实线双行道': ul.dict7_0,
        '双向虚实线双行道': ul.dict8_0,
        '双向双实线双行道': ul.dict9_0,
        '一前行虚白线虚黄线三行道': ul.dict10_0,
        '一前行实白线虚黄线三行道': ul.dict11_0,
        '一前行虚白线实黄线三行道': ul.dict12_0,
        '一前行实白线实黄线三行道': ul.dict13_0,
        '二前行虚黄线虚白线三行道': ul.dict14_0,
        '二前行虚黄线实白线三行道': ul.dict15_0,
        '二前行实黄线虚白线三行道': ul.dict16_0,
        '二前行实黄线实白线三行道': ul.dict17_0,
        '双黄实线虚虚四车道': ul.dict18_0,
        '双黄实线实实四车道': ul.dict19_0,
        '双黄实线虚实四车道': ul.dict20_0,
        '双黄实线实虚四车道': ul.dict21_0,
        '双实线虚虚虚虚六车道': ul.dict22_0,
        '双实线实实实实六车道': ul.dict23_0,
        '双实线虚虚实实六车道': ul.dict24_0

    },  # 不全
    'roundabout': {
        '双车道环岛': rdb.dict1,
    }

}

# print(str_dic_mapping.get('straightlane').get("单行道"))
