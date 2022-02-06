
# Alaya节点锁定状态监控，

# 导入所需要的依赖包
from urllib import request
import requests

# HTTP连接api.alayascan.com 所提供的公开API接口资源：
# 已锁定验证人列表 /alaya-api/staking/lockedStakingList
url = "https://api.alayascan.com//alaya-api/staking/lockedStakingList"
data = {'address':'atp1hfmnlc7v7y5lkufh070tjf6ksaznva3w2ctdmy'}
# =dict(address='atp1hfmnlc7v7y5lkufh070tjf6ksaznva3w2ctdmy')
header = {
    "content_type":"application/json",
    }
response = requests.post(url,json=data)
print(type(response),response.status_code)
print(response.json())