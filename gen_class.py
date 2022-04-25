# !/usr/bin/env python
# coding: utf-8
import os
from moody.libeb import MiliDoS
from moody import Evm
from key import NETWORK, ROOT

SOLV = "0.8.6"

CONTRACT_LIST = [
    "vault/ConnextPriceOracle.sol",
    "vault/Multicall.sol",
    "vault/PriceOracle.sol",
    "vault/ProposedOwnable.sol",
    "vault/Router.sol",
    "vault/RouterFactory.sol",
    "vault/TransactionManager.sol"
]

r = MiliDoS(NETWORK)
print("-----> this is now started")
print(ROOT)
print("-----> now it is root")
r.setWorkspace(ROOT).setEvm(Evm.ISTANBUL).setClassSolNames(CONTRACT_LIST).setOptimizationRuns(10000).remoteCompile(SOLV).localTranspile("app")
# r.setWorkspace(ROOT).setClassSolNames(CONTRACT_LIST).localTranspile()
# os.system("sh localpile")
