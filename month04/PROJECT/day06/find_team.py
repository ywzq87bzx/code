#小学春游 - 两组同学，每组1-3人，每组有一个队长;春游期间，
# 由于景点人数较多，秩序混乱，班主任要求在指定地点，按组集合

#源数据
s = [{'name':'leader-1','belong_to':None},
     {'name':'jack','belong_to':'leader-2'},
     {'name':'lili','belong_to':'leader-1'},
     {'name':'leader-2','belong_to':None},
     {'name':'Tom', 'belong_to':'leader-1'}]
#目标数据
d = [
    {'name':'leader-1', 'team':[{'name':'lili'},{'name':'Tom'}]},
    {'name':'leader-2', 'team':[{'name':'jack'}]}
]
def find_team(data):
    leader_data=[]
    m_dict={}
    for d in data:
        if d['belong_to']:
            m_dict.setdefault(d['belong_to'],[])
            m_dict[d['belong_to']].append({'name':d['name']})
        else:
            leader_data.append({'name':d['name'],'team':[]})
    # print(m_dict)
    # print(leader_data)
    for r in leader_data:
        if r['name'] in m_dict:
            r['team']=m_dict[r['name']]
    print(leader_data)
    return leader_data




if __name__ == '__main__':
    find_team(s)


