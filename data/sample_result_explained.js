/* 这份文件用于解释数据接口，不会在项目中使用。无奈json加不了注释 */
/* 数据都是手打的，非真实（ */
let result = {
  "group": 1, // 团伙id，从1依次增加
  "info": {
    "groupSize": 1, // 团伙size，1小型；2中型；3大型
    "totalNodes": 176, // 团伙中所有的节点数
    "totalLinks": 213, // 团伙中所有的边数
    "industryComponents":{ // 团伙中domain节点对应的industry，做一个统计，
      "A": 100, // 表示这个团伙中A产业的数量
      "B": 12,
      "C": 17,
      "D": 21,
      "E": 19,
      "F": 67,
      "G": 18,
      "H": 29,
      "I": 80
    }
  },
  "nodesCore":[ // 核心节点列表
    {
      // 节点信息，与Node.csv中存储的格式一样
      "id": "Domain_2d3bbcec29453b6f56fb85ea28e8e5ea5fc5f5562e0f896b6b52b113a6cc1e44",
      "name": "2d3bbcec29.com",
      "type": "Domain",
      "industry": [
        "C", "E", "A", "B"
      ]
    },
    {
      "id": "Domain_9bbf71ad49989e141f42613d1bf41bb85d4e0cdd538417292884ea4fd340c9ca",
      "name": "9bbf71ad49.com",
      "type": "Domain",
      "industry":[
        "A", "G", "C", "E", "B"
      ]
    },
    {
      "id": "Domain_141f42613d1bf41bb85d4e0cdd53841729bbf71ad49989e92884ea4fd340c9ca",
      "name": "141f42613d1.com",
      "type": "Domain",
      "industry":["C", "E", "B"]
    },
    {
      "id": "ASN_3bc5b0706c3df8182f7784cafa0bd864c4a6d432266863609f1f5c22c47fa04b",
      "name": "AS_3bc5b0706c",
      "type": "ASN",
      "industry":[]
    }
  ],
  "linksImportant": [ // 关键链路
    {
      // source与target，(虽说这是无向边
      "source": "Domain_141f42613d1bf41bb85d4e0cdd53841729bbf71ad49989e92884ea4fd340c9ca",
      "target": "Domain_9bbf71ad49989e141f42613d1bf41bb85d4e0cdd538417292884ea4fd340c9ca",
      "distance": 3, // 路径长度，例如A-B-C-D，则A-D路径长度为3
      "importance": 4 // 路径重要性，取路径中边重要性的最小值 1-较弱，2-一般，3-较强，4-很强
    },
    {
      "source": "Domain_141f42613d1bf41bb85d4e0cdd53841729bbf71ad49989e92884ea4fd340c9ca",
      "target": "Domain_2d3bbcec29453b6f56fb85ea28e8e5ea5fc5f5562e0f896b6b52b113a6cc1e44",
      "distance": 4,
      "importance": 4
    },
    {
      "source": "Domain_141f42613d1bf41bb85d4e0cdd53841729bbf71ad49989e92884ea4fd340c9ca",
      "target": "ASN_3bc5b0706c3df8182f7784cafa0bd864c4a6d432266863609f1f5c22c47fa04b",
      "distance": 3,
      "importance": 2
    }
  ]
}