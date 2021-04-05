# coding: utf8
import os
from farbox_bucket.client.sync import sync_to_farbox

# 如果 DEBUG 设定是 yes，会在日志中输出同步的记录
os.environ['DEBUG'] = 'yes'

private_key = """
填写你的私钥
"""

root = "posts"

# 节点
node = "填写服务器IP"

# 开始同步
sync_to_farbox(node=node, root=root, private_key=private_key)
