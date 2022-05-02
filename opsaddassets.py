# !/usr/bin/env python
# coding: utf-8
# from web3.auto import w3
from datetime import datetime

from moody.libeb import MiliDoS

from codec.gen_py.connext_price_oracle import ConnextPriceOracle
from codec.gen_py.router_factory import RouterFactory
from codec.tasks.addasset import add_asset
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


# beri coin
add_asset(j, "0xf97C453899fCAe9fc815460a223cF91FD1a0a6e1", j.getAddr("TransactionManager"))
# USXXX
add_asset(j, "0x45F056BC4e2dEaE17135fE9B0F1EaC613422664b", j.getAddr("TransactionManager"))
# GLD
add_asset(j, "0xFAbc5eC387125fAe130Bd86e91A29b58D3b74171", j.getAddr("TransactionManager"))
# USDF
add_asset(j, "0xAd08d31579dd599801e8839db70Bd9C84D2B98e9", j.getAddr("TransactionManager"))
# LSL
add_asset(j, "0x8844D7C5645FC436D80f2dCd9830F5CB88Ff96a4", j.getAddr("TransactionManager"))