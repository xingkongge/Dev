# 目标：为lat委托人提供及时的节点状态异常信息
# 判断方法：定期（4小时）获取节点状态，进行前后两次的对比；节点状态由1、候选中；2、活跃中；3、出块中；变为6、已锁定；

# 导入所需依赖包
from urllib import request
import requests
from threading import Timer

#根据PlatONnetwork提供的openAPI文档，确定所需要的URL
urlAliveStakingList = "https://api.plateye.com/api/staking/aliveStakingList"   #实时验证人列表接口
urlLockedStakingList = "https://api.plateye.com/api/staking/lockedStakingList" # 已锁定验证人列表接口

parameterAliveStakingList = {
    # pageNo和pageSize设置为0，即获取全部数据
    "pageNo":0,  
    "pageSize":0,
    "key":"",
    "queryStatus":"all"
    }

parameterLockedStakingList = {
    "pageNo":0,
    "pageSize":0,
    "key":"" 
}
# 获取所有实时验证人节点
responseAliveStakingList = requests.post(url=urlAliveStakingList,json = parameterAliveStakingList)

# 获取所有已锁定验证人节点
# responseLockedStakingListInt = requests.post(url=urlLockedStakingList, json=parameterLockedStakingList)
# print(responseAliveStakingList.status_code,responseAliveStakingList.json())
def getLockedStakingList():
    return requests.post(url=urlLockedStakingList, json=parameterLockedStakingList)

lastLockedStakingList=getLockedStakingList().json()['data'][0:2]
print(lastLockedStakingList)
#'''
i=0 
while i<10:
    Timer(5,getLockedStakingList())
    i+=1
    currentLockedStakingList =getLockedStakingList().json()['data'][0:2]
    if lastLockedStakingList==currentLockedStakingList:
        pass
    else:
        for x in currentLockedStakingList:
            if x in lastLockedStakingList:
                pass
            else:print(x['nodeName'])
print("hello")
#'''

