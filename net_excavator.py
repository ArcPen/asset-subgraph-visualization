#%%
import networkx as nx
import csv

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
## 用于存储每个group的graph
graph_group_list = []
# 用一些算法挖掘好子图之后，append到这个list中


#%%
## 根据graph_group_list中存储的信息，整理生成一个info list
## 随后转换成json格式并存储
group_info_list = []
# 这一部分的代码就交给Kyre写吧
for group_graph in graph_group_list:
    group_info = {}
    graph_group_list.append(group_info)

# jsonify group_info_list and store it to `data/final_result.json`
