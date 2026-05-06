import pandas as pd
import numpy as np
import os

# data has format 
# [
#     [
#         [anchor_11, anchor_12, ..], 
 #        [positive_11, positive_12, ...], 
#         [negative_11, negative_12, ...]
#     ],
#     [
#         [anchor_21, anchor_22, ..], 
#         [positive_21, positive_22, ...], 
#         [negative_21, negative_22, ...]
#     ],
#     ...
# ]
# where every positive_ij matches anchor_ik and every negative_ij doesnt match anchor_ik for every i, j, k

data = [
    [
        [
            'where I can find data about how much hours translators were working',
            'where I can find data about how much hours workers were working',
            'where I can find data about how much hours employees were working',
            'where I can find data about translators work efficiency'
        ],
        [
            'table dw.fact.Productivity_TIME contains information about how much time employees were working',
            'table Stage.emp.tbl_TSProductivityTimeSpans contains information from timesheet about productive activities and operations user perform, their date, cost code'
        ],
        [
            "table dw.fact.Quality_Evaluations contains information about quality evaluations of performed translations. It is created by ssis package 'Quality Evaluation (Translation)'",
            'table Stage.dbi.AdjustmentFactor_Map contains information about adjustment factors for calculating adjusted words for different tasks and units',
            'Joe longworth is dealing with Helix data',
            'Nikhil Marathe might help with data from empower'
        ]
    ],
    [
        [
            'where I can find data about how many words translators translated',
            'where I can find data about how many words workers translated',
            'where I can find data about how many words employees translated',
            'where I can find data about translators work efficiency'
        ],
        [
            'table dw.fact.Productivity_WORDS contains information about how many words employees have translated',
            'table Stage.emp.tbl_TSProductivityEntries contains information from timesheet about users productivity, productivity measure, number of translated words'
        ],
        [
            "table dw.fact.Quality_Evaluations contains information about quality evaluations of performed translations. It is created by ssis package 'Quality Evaluation (Translation)'",
            'table Stage.dbi.AdjustmentFactor_Map contains information about adjustment factors for calculating adjusted words for different tasks and units',
            'Joe longworth is dealing with Helix data',
            'Nikhil Marathe might help with data from empower'
        ]
    ],
    [
       [
           "I can't see translators productive hours",
           "I can't see employees productive hours",
           "I can't see workers productive hours",
           "productive hours worked not visible",
           "productive hours worked disappeared",
           "productivity data not visible",
           "productivity data not disappear",
           "translators productive hours worked disappear",
           "translators productive hours worked not visible",
           "workers productive hours worked not visible",
           "workers productive hours worked disappear",
           "employees productive hours worked not visible",
           "employees productive hours worked disappear"
        ],
        [
            "in order to allow someone to see someone's productivity data we need to adjust data security rules in elasticube"
        ],
        [
            'table dw.fact.Productivity_TIME contains information about how much time employees were working',
            'data about how much productive hours or words someone has is taken from the table stage.emp.tbl_TSProductivityTimeSpans and stage.emp.tbl_TSProductivityEntries',
            'table dw.fact.Productivity_WORDS contains information about how many words employees have translated',
            'table Stage.emp.tbl_TSProductivityTimeSpans contains information from timesheet about productive activities and operations user perform, their date, cost code'
        ]
    ],
    [
        [
            'where I can find data about cost center hierarchy',
            'where I can find information about cost center hierarchy',
            'which table contains data about cost center hierarchy',
            'which table contains information about cost center hierarchy'
        ],
        [
            'table Stage.dbo.vw_CCH_V6a contains information about cost center, hierarchy, office, region, business unit, business sub unit, type'
        ],
        [
            'table Stage.emp.tblLU_Offices contains information from empower about offices, their managers, region, country, currency, adress, city',
            'table Stage.emp.tblLU_CostControlCodes contains information about cost codes',
            'Nikhil Marathe might help with data from empower',
            'table Stage.emp.tbl_TSProductivityTimeSpans contains information from timesheet about productive activities and operations user perform, their date, cost code'
        ],
    ],
    [
        [
            'where I can find information about suppliers',
            'where I can find data about suppliers',
            'in which table I can find information about suppliers',
            'in which table I can find data about suppliers',
            'where I can find information about vendors',
            'where I can find data about vendors',
            'in which table I can find information about vendors',
            'in which table I can find data about vendors',
            'where I can find information about suppliers name',
            'where I can find data about suppliers email',
            'in which table I can find information about suppliers status',
            'in which table I can find data about suppliers code',
            'where I can find information about vendors code',
            'where I can find data about vendors email',
            'in which table I can find information about vendors name',
            'in which table I can find data about vendors status'
        ],
        [
            'table Stage.dbi.PRTL_Vendor contains information from helix about vendor id, code, name, user name, email, status'
        ],
        [
            'Nikhil Marathe might help with data from empower',
            'table stage.helix.JT_External_PO_v2 contains information about purchase orders from Helix',
            'Joe longworth is dealing with Helix data'
        ]
    ],
    [
        [
            'helix data procurement',
            'helix information orders',
            'helix data purchases'
        ],
        [
            'table stage.helix.JT_External_PO_v2 contains information about purchase orders from Helix'
        ],
        [
            'Joe longworth is dealing with Helix data',
            'Helix documentation: https://sdl.appiancloud.com/suite/sites/data-dictionary'
        ]
    ],
    [
        [
            'data about jobs',
            'data about tasks'
        ],
        [
            'table stage.helix.JT_Task_v2 contains information about tasks from Helix'
        ],
        [
            'table stage.dbi.Headcount_NEW contains information about employees who are working for us, who joined us and who left us',
            'table dw.fact.Productivity_TIME contains information about how much time employees were working',
            'data about how much productive hours or words someone has is taken from the table stage.emp.tbl_TSProductivityTimeSpans and stage.emp.tbl_TSProductivityEntries'
        ]
    ],
    [
        [
            'information about how good are our translations',
            'information about how good is our work',
            'information about how well we do our work'
        ],
        [
            "table dw.fact.Quality_Evaluations contains information about quality evaluations of performed translations. It is created by ssis package 'Quality Evaluation (Translation)'"
        ],
        [
            'table Stage.emp.tbl_TSProductivityEntries contains information from timesheet about users productivity, productivity measure, number of translated words',
            'table Stage.emp.tblLU_TSProductivityMeasures contains information from timesheet about productivity type, operation, productivity measure',
            'table dw.fact.Productivity_TIME contains information about how much time employees were working'
        ]
    ]
]

train_data = []

for i in range(len(data)):
    train_data_new_sec = []
    anchors = data[i][0]
    positives = data[i][1]
    negatives = data[i][2]
    # firstable we want to take all values from anchors, positives and negatives to our train_data_new_sec
    for j in range(max(len(anchors), len(positives), len(negatives))):
        train_data_new_sec.append([anchors[j % len(anchors)], positives[j % len(positives)], negatives[j % len(negatives)]])

    # now we want to take different combinations of anchors, positives and negatives such that total amount
    # of examples in train_data_new_sec is not bigger then 30
    for anchor in anchors:
        for positive in positives:
            for negative in negatives:
                if ([anchor, positive, negative] not in train_data_new_sec
                    and len(train_data_new_sec) < 30):
                    train_data_new_sec.append([anchor, positive, negative])
    
    train_data += train_data_new_sec
    
train_data = pd.DataFrame(train_data)
train_data.columns = ['anchor', 'positive', 'negative']
if not os.path.isdir('data'):
    os.makedirs('data')
train_data.to_csv('data/train_data.csv')