from func.GraphSimilarity import GetBaseSimilarity
from func.GraphSimilarityV2 import GetImproveSimilarity


def calculatesimilarity():
    five_random_h1 = [52, 41, 46, 55, 43]
    five_count_h1 = [47, 50, 55, 43, 50]
    five_random_h2 = [108, 84, 103, 98, 102]
    five_count_h2 = [85, 96, 100, 96, 93]
    five_random_h3 = [155, 136, 150, 150, 144]
    five_count_h3 = [127, 143, 146, 145, 143]
    five_random_h4 = [207, 181, 200, 215, 195]
    five_count_h4 = [176, 183, 198, 195, 184]
    five_random_h5 = [257, 229, 243, 267, 245]
    five_count_h5 = [216, 229, 242, 247, 238]
    five_random_h6 = [320, 265, 293, 330, 306]
    five_count_h6 = [261, 272, 300, 286, 284]
    five_random_h7 = [369, 323, 346, 394, 347]
    five_count_h7 = [317, 317, 343, 329, 329]
    five_random_h8 = [434, 378, 389, 454, 406]
    five_count_h8 = [359, 363, 371, 372, 372]
    five_random_h9 = [495, 442, 450, 516, 450]
    five_count_h9 = [400, 402, 411, 415, 420]
    five_random_h10 = [545, 499, 503, 584, 501]
    five_count_h10 = [458, 458, 463, 453, 469]
    five_random_h11 = [593, 570, 575, 650, 567]
    five_count_h11 = [506, 501, 513, 509, 514]
    five_random_h12 = [648, 630, 625, 694, 614]
    five_count_h12 = [546, 556, 565, 552, 564]
    five_random_h13 = [710, 692, 684, 745, 655]
    five_count_h13 = [593, 615, 613, 596, 514]
    five_random_h14 = [760, 755, 738, 810, 709]
    five_count_h14 = [643, 666, 655, 647, 659]
    five_random_h15 = [822, 808, 803, 857, 776]
    five_count_h15 = [691, 708, 691, 689, 711]
    five_random_h16 = [887, 883, 861, 923, 831]
    five_count_h16 = [736, 730, 736, 746, 755]
    five_random_h17 = [940, 945, 904, 968, 897]
    five_count_h17 = [785, 806, 776, 798, 803]
    five_random_h18 = [990, 1010, 960, 1028, 955]
    five_count_h18 = [834, 853, 820, 844, 846]
    five_random_h19 = [1047, 1058, 1024, 1078, 996]
    five_count_h19 = [876, 899, 872, 889, 901]
    five_random_h20 = [1101, 1115, 1075, 1135, 1052]
    five_count_h20 = [934, 951, 921, 932, 947]
    five_random_h21 = [1155, 1168, 1146, 1190, 1122]
    five_count_h21 = [967, 1002, 966, 981, 990]
    five_random_h22 = [1201, 1215, 1212, 1239, 1181]
    five_count_h22 = [1019, 1039, 1005, 1023, 1044]
    five_random_h23 = [1260, 1257, 1264, 1296, 1241]
    five_count_h23 = [1062, 1098, 1053, 1077, 1099]
    five_random_h24 = [1311, 1301, 1304, 1347, 1305]
    five_count_h24 = [1115, 1140, 1094, 1118, 1140]

    RandomStr = "five_random_h"
    CountStr = "five_count_h"

    # graph_dir0 = "./8_graph" #第0组
    # graph_dir1 = "./8_1graph"
    # graph_dir2 = "./8_2graph"
    # graph_dir3 = "./8_3graph"
    # graph_dir4 = "./8_4graph"

    graph_dir0 = "./data/graph"  # 第0组
    graph_dir1 = "./data/1graph"
    graph_dir2 = "./data/2graph"
    graph_dir3 = "./data/3graph"
    graph_dir4 = "./data/4graph"

    graphList = [graph_dir0, graph_dir1, graph_dir2, graph_dir3, graph_dir4]

    for index in range(1, 4):
        print(index, "小时结果")
        print("=======================================================================================")
        for i, (e1, e2) in enumerate(zip(eval(RandomStr + str(index)), eval(CountStr + str(index)))):
            print("第 ", i, " 组的实验结果为：--------------------------------------------------")
            #print("random-V1相似度判断方法结果")
            # GetBaseSimilarity(graphList[i], e1)
            # print("random-V2相似度判断方法结果")
            # GetImproveSimilarity(graphList[i], e1)
            # print("\n")
            # print("countBased-V1相似度判断方法结果")
            # GetBaseSimilarity(graphList[i] + "2", e2)
            # print("countBased-V2相似度判断方法结果")
            # GetImproveSimilarity(graphList[i] + "2", e2)
            # print("\n\n\n")

    # five_widget_V1_h1 = [52, 41, 46, 55, 43]
    # five_widget_V2_h1 = [47, 50, 55, 43, 50]
    # five_widget_V1_h2 = [108, 84, 103, 98, 102]
    # five_widget_V2_h2 = [85, 96, 100, 96, 93]
    # five_widget_V1_h3 = [155, 136, 150, 150, 144]
    # five_widget_V2_h3 = [127, 143, 146, 145, 143]
    # five_widget_V1_h4 = [207, 181, 200, 215, 195]
    # five_widget_V2_h4 = [176, 183, 198, 195, 184]
    # five_widget_V1_h5 = [257, 229, 243, 267, 245]
    # five_widget_V2_h5 = [216, 229, 242, 247, 238]
    # five_widget_V1_h6 = [320, 265, 293, 330, 306]
    # five_widget_V2_h6 = [261, 272, 300, 286, 284]
    # five_widget_V1_h7 = [369, 323, 346, 394, 347]
    # five_widget_V2_h7 = [317, 317, 343, 329, 329]
    # five_widget_V1_h8 = [434, 378, 389, 454, 406]
    # five_widget_V2_h8 = [359, 363, 371, 372, 372]
    # five_widget_V1_h9 = [495, 442, 450, 516, 450]
    # five_widget_V2_h9 = [400, 402, 411, 415, 420]
    # five_widget_V1_h10 = [545, 499, 503, 584, 501]
    # five_widget_V2_h10 = [458, 458, 463, 453, 469]
    # five_widget_V1_h11 = [593, 570, 575, 650, 567]
    # five_widget_V2_h11 = [506, 501, 513, 509, 514]
    # five_widget_V1_h12 = [648, 630, 625, 694, 614]
    # five_widget_V2_h12 = [546, 556, 565, 552, 564]
    # five_widget_V1_h13 = [710, 692, 684, 745, 655]
    # five_widget_V2_h13 = [593, 615, 613, 596, 514]
    # five_widget_V1_h14 = [760, 755, 738, 810, 709]
    # five_widget_V2_h14 = [643, 666, 655, 647, 659]
    # five_widget_V1_h15 = [822, 808, 803, 857, 776]
    # five_widget_V2_h15 = [691, 708, 691, 689, 711]
    # five_widget_V1_h16 = [887, 883, 861, 923, 831]
    # five_widget_V2_h16 = [736, 730, 736, 746, 755]
    # five_widget_V1_h17 = [940, 945, 904, 968, 897]
    # five_widget_V2_h17 = [785, 806, 776, 798, 803]
    # five_widget_V1_h18 = [990, 1010, 960, 1028, 955]
    # five_widget_V2_h18 = [834, 853, 820, 844, 846]
    # five_widget_V1_h19 = [1047, 1058, 1024, 1078, 996]
    # five_widget_V2_h19 = [876, 899, 872, 889, 901]
    # five_widget_V1_h20 = [1101, 1115, 1075, 1135, 1052]
    # five_widget_V2_h20 = [934, 951, 921, 932, 947]
    # five_widget_V1_h21 = [1155, 1168, 1146, 1190, 1122]
    # five_widget_V2_h21 = [967, 1002, 966, 981, 990]
    # five_widget_V1_h22 = [1201, 1215, 1212, 1239, 1181]
    # five_widget_V2_h22 = [1019, 1039, 1005, 1023, 1044]
    # five_widget_V1_h23 = [1260, 1257, 1264, 1296, 1241]
    # five_widget_V2_h23 = [1062, 1098, 1053, 1077, 1099]
    # five_widget_V1_h24 = [1313, 1303, 1306, 1350, 1307]
    # five_widget_V2_h24 = [1117, 1143, 1096, 1121, 1143]

    # graph_dir0 = "./data/graph"
    # graph_dir1 = "./data/1graph"
    # graph_dir2 = "./data/2graph"
    # graph_dir3 = "./data/3graph"
    # graph_dir4 = "./data/4graph"
    #
    #
