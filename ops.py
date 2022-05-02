# !/usr/bin/env python
# coding: utf-8
# from web3.auto import w3
from datetime import datetime

from moody.libeb import MiliDoS

from codec.gen_py.connext_price_oracle import ConnextPriceOracle
from codec.gen_py.router_factory import RouterFactory
from codec.tasks.addliquity import add_liqudity
from codec.tasks.addasset import add_asset
from codec.tasks.addrouter import add_router
from codec.tasks.createrouter import create_router
from key import pri, NETWORK, ROOT, pub

# ========================== Of course
signer = "0x552De3B566A0417588f8094C648320Ec2Fa98018"
publicone = "0x8e56C4E7e9A87188D4Cb00B084d4ebD8F73d9B91"
j = MiliDoS(NETWORK).withPOA()
j.setWorkspace(ROOT).Auth(pri)
j.OverrideGasConfig(6000000, 2000000000)
# test of all routeres
# create_router(j, signer, pub)
router_add = "0x59Fe6e5c1354c45EC69503c130252445e445646a"
add_router(j, router_add, j.getAddr("TransactionManager"))
# beri coin
add_liqudity(j, router_add, "0xf97C453899fCAe9fc815460a223cF91FD1a0a6e1", 10, j.getAddr("TransactionManager"))
# USXXX
add_liqudity(j, router_add, "0x45F056BC4e2dEaE17135fE9B0F1EaC613422664b", 10, j.getAddr("TransactionManager"))
# GLD
add_liqudity(j, router_add, "0xFAbc5eC387125fAe130Bd86e91A29b58D3b74171", 10, j.getAddr("TransactionManager"))