# coding: utf8
import os
from farbox_bucket.client.sync import sync_from_farbox

# 如果 DEBUG 设定是 yes，会在日志中输出同步的记录
os.environ['DEBUG'] = 'yes'

private_key = """
填写你的私钥
"""

root = "./"

# 节点
node = "填写服务器IP"

# 开始同步
sync_from_farbox(root=root, node=node, private_key=private_key)
