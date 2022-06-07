#%%
import networkx as nx
import csv
from collections import deque

#%%
## 一个包含所有Nodes和Links的图
## 内存消耗可能比较大，不过貌似不重要
# 从csv文件里面读取数据并加入

ImportanceNodes = {'Domain':3, 'IP':3, 'Cert':3, 'Whois_Name':2, 'Whois_Phone':2, 'Whois_Email':2, 'IP_C':1, 'ASN':1}
ImportanceLinks = {'r_cert': 4, 'r_subdomain': 4, 'r_request_jump': 4, 'r_dns_a': 4, 'r_whois_name': 3, 'r_whois_email': 3, 'r_whois_phone': 3, 'r_cert_chain': 2, 'r_cname': 2, 'r_asn': 1, 'r_cidr': 1}

def read_in_all_graph(): # 用函数包裹一下，避免可能的变量污染
    graph_all = nx.Graph()
    with open('data/Node.csv', 'r', encoding='utf-8') as nodes:
        nodes.readline() # get rid of first line
        reader = csv.reader(nodes)
        for data in reader:
            graph_all.add_node(
                data[0],
                name = data[1],
                type = data[2],
                industry = data[3],
                classified = False, # 是否已经分到一个group里
                is_core_node = False, # 是否是核心节点
                importance = ImportanceNodes[data[2]], # 重要性，1-3
            )

    with open('data/Link.csv', 'r', encoding='utf-8') as links:
        links.readline() # get rid of first line
        reader = csv.reader(links)
        for data in reader:
            graph_all.add_edge(
                data[1], # source
                data[2], # target
                relation = data[0],
                importance = ImportanceLinks[data[0]]
            )

    return graph_all

graph_all = read_in_all_graph()
print("graph_all loading complete!")

# It seems that nx use a hashable object to represent the node
# And a subgraph is easily created through g.subgraph(('n1', 'n2',...))


#%%
def subgraph_mining(init_id, mining_depth, min_num_edges, max_num_neighbors):
    subgraph_id = set()
    for id in init_id:
        subgraph_id.add(id)

        # BFS search
        stack = deque([id])
        level = 0  # level < mining_depth
        while stack:
            for _ in range(len(stack)):
                node_id = stack.popleft()

                # get all neighbors
                neighbors = list(graph_all.neighbors(node_id))  # 迭代器转为list，重复遍历
                # judge if is core node
                if graph_all.nodes[node_id]['importance'] == 3:
                    if len(neighbors) >= min_num_edges:
                        weak_edges = 0  # 50%以上的邻边关联强度较弱的网络资产不被认为是核心网络资产
                        num_ip = 0  # 同时关联2个以上IP地址的Domain网络资产不被认为是核心网络资产
                        for neighbor in neighbors:
                            if graph_all.nodes[neighbor]['type'] == 'IP':
                                num_ip += 1
                            if graph_all.edges[node_id, neighbor]['importance'] == 1:
                                weak_edges += 1

                        if num_ip < 2 and weak_edges / len(neighbors) < 0.5:  # 核心资产
                            graph_all.nodes[node_id]['is_core_node'] = True

                # visualize the subgraph
                num_neighbors = 0  # if num > max_num_neighbors, stop
                for neighbor in neighbors:
                    if neighbor not in subgraph_id:
                        subgraph_id.add(neighbor)
                        graph_all.nodes[neighbor]['classified'] = True  # 分到一个group里
                        stack.append(neighbor)
                        num_neighbors += 1

                    if num_neighbors > max_num_neighbors:
                        break

            # level order
            level += 1
            if level >= mining_depth:
                break

    return list(subgraph_id)


# small-size group
init_id_1 = [
    'Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9',
    'Domain_f3554b666038baffa5814c319d3053ee2c2eb30d31d0ef509a1a463386b69845',
]
subgraph_1 = subgraph_mining(init_id_1, 2, 7, 30)

# medium-size group
init_id_2 = [
    'IP_400c19e584976ff2a35950659d4d148a3d146f1b71692468132b849b0eb8702c',
    'Domain_b10f98a9b53806ccd3a5ee45676c7c09366545c5b12aa96955cde3953e7ad058',
]
subgraph_2 = subgraph_mining(init_id_2, 3, 10, 40)

# large-size group
init_id_3 = [
    'IP_7e730b193c2496fc908086e8c44fc2dbbf7766e599fabde86a4bcb6afdaad66e',
    'Cert_6724539e5c0851f37dcf91b7ac85cb35fcd9f8ba4df0107332c308aa53d63bdb',
]
subgraph_3 = subgraph_mining(init_id_3, 3, 10, 30)

## 用于存储每个group的graph
graph_group_list = [subgraph_1, subgraph_2, subgraph_3]

#%%
## 根据graph_group_list中存储的信息，整理生成一个info list
## 随后转换成json格式并存储
group_info_list = []
# 这一部分的代码就交给Kyre写吧
for group_graph in graph_group_list:
    group_info = {}
    graph_group_list.append(group_info)

# jsonify group_info_list and store it to `data/final_result.json`
