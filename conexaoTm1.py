# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:57:57 2021

@author: VitorGonçalvesRibeir
"""


from TM1py.Services import CellService, TM1Service, ServerService
from TM1py.Utils import Utils
from TM1py.Objects import Cube, Dimension, Element, ElementAttribute, Hierarchy
from TM1py.Utils.Utils import build_pandas_dataframe_from_cellset

address='10.28.28.240'
port=8002
user='OPS_COGNOSSERV'
password='N0BZamwyWVk='
namespace='AD'
decode_b64=True
ssl=True

with TM1Service(
    address=address,
    port=port,
    user=user,
    password=password,
    namespace=namespace,
    decode_b64=decode_b64,
    ssl=ssl
) as tm1:
    print("sucess")
