import networkx as nx

from utils import load_json, get_actions_list, get_verb_object

def rules_for_graph(action_i, action_j):
    # 0-level actions: walk to sth, run to sth

    # 1-level actions: open sth, grab sth, switch on sth, sit on sth, 

    # 2-level actions: close sth, drink sth, switch off sth, stand up, put in, put back
    v_i, o_i_1, o_i_2 = get_verb_object(action_i)
    v_j, o_j_1, o_j_2 = get_verb_object(action_j)
    flag = 0
    if (v_i == "walk" and v_j == "walk" and o_i_1 != o_j_1) or (v_i == "walk" and v_j == "run" and o_i_1 != o_j_1) \
        or (v_i == "walk" and v_j == "open" and o_i_1 == o_j_1) or (v_i == "walk" and v_j == "grab" and o_i_1 == o_j_1) \
        or (v_i == "walk" and v_j == "switchon" and o_i_1 == o_j_1) \
        or (v_i == "walk" and v_j == "sit" and o_i_1 == o_j_1) \
        or (v_i == "walk" and v_j == "close" and o_i_1 == o_j_1) \
        or (v_i == "walk" and v_j == "switch off" and o_i_1 == o_j_1) \
        or (v_i == "walk" and v_j == "drink") \
        or (v_i == "walk" and v_j == "putback" and o_i_1 == o_j_2) or (v_i == "walk" and v_j == "putin" and o_i_1 == o_j_2):
        flag = 1
    elif (v_i == "run" and v_j == "run" and o_i_1 != o_j_1) or (v_i == "run" and v_j == "walk" and o_i_1 != o_j_1) \
        or (v_i == "run" and v_j == "drink"):
        flag = 1
    elif (v_i == "open" and v_j == "close" and o_i_1 == o_j_1) or (v_i == "open" and v_j == "putin" and o_i_1 == o_j_2) \
        or (v_i == "open" and v_j == "walk" and o_i_1 != o_j_1) or (v_i == "open" and v_j == "run" and o_i_1 != o_j_1) \
        or (v_i == "open" and v_j == "drink" and o_i_1 != o_j_1):
        flag = 1
    elif (v_i == "grab" and v_j == "drink" and o_i_1 == o_j_1) \
        or (v_i == "grab" and v_j == "walk" and o_i_1 != o_j_1) \
        or (v_i == "grab" and v_j == "run" and o_i_1 != o_j_1) \
        or (v_i == "grab" and v_j == "putin" and o_i_1 == o_j_1):
        flag = 1
    elif (v_i == "switchon" and v_j == "switchoff" and o_i_1 == o_j_1) or (v_i == "switchon" and v_j == "walk" and o_i_1 != o_j_1) \
        or (v_i == "switchon" and v_j == "run" and o_i_1 != o_j_1) or (v_i == "switchon" and v_j == "drink" and o_i_1 != o_j_1):
        flag = 1
    elif (v_i == "sit" and v_j == "stand up"):
        flag = 1
    elif (v_i == "close" and v_j == "walk" and o_i_1 != o_j_1) or (v_i == "close" and v_j == "run" and o_i_1 != o_j_1) \
        or (v_i == "close" and v_j == "drink" and o_i_1 != o_j_1):
        flag = 1
    elif (v_i == "drink" and v_j == "walk" and o_i_1 != o_j_1) or (v_i == "drink" and v_j == "run" and o_i_1 != o_j_1):
        flag = 1
    elif (v_i == "switchoff" and v_j == "walk" and o_i_1 != o_j_1) or (v_i == "switchoff" and v_j == "run" and o_i_1 != o_j_1) \
        or (v_i == "switchoff" and v_j == "drink" and o_i_1 != o_j_1):
        flag = 1
    elif (v_i == "stand up" and v_j == "walk") or (v_i == "stand up" and v_j == "run") or (v_i == "stand up" and v_j == "drink"):
        flag = 1
    elif (v_i == "putin" and v_j == "walk" and o_i_2 != o_j_1 and o_i_1 != o_j_1) \
        or (v_i == "putin" and v_j == "run" and o_i_2 != o_j_1 and o_i_1 != o_j_1) \
        or (v_i == "putin" and v_j == "drink" and o_i_2 != o_j_1 and o_i_1 != o_j_1) \
        or (v_i == "putin" and v_j == "close" and o_i_2 == o_j_1):
        flag = 1
    elif (v_i == "putback" and v_j == "walk" and o_i_2 != o_j_1 and o_i_1 != o_j_1) \
        or (v_i == "putback" and v_j == "run" and o_i_2 != o_j_1 and o_i_1 != o_j_1) \
        or (v_i == "putback" and v_j == "drink" and o_i_2 != o_j_1 and o_i_1 != o_j_1):
        flag = 1
    return flag



def create_directed_graph(all_actions_file):
    all_ = load_json(all_actions_file)
    all_actions = get_actions_list(all_)
    
    DG = nx.MultiDiGraph()
    DG.add_nodes_from(all_actions)

    for action_i in all_actions:
        for action_j in all_actions:
            if action_i != action_j:
                flag = rules_for_graph(action_i, action_j)
                if flag == 1:
                    DG.add_edges_from([(action_i, action_j)])

    return DG