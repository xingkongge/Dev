from client_sdk_python import Web3,HTTPProvider
from client_sdk_python.eth import PlatON
w3 = Web3(HTTPProvider("http://47.241.98.219:6789"),chain_id=210309)
platon = PlatON(w3)
# platon_number = Web3.toInt(platon.blockNumber())
print(w3.isConnected())
print(platon.blockNumber)


