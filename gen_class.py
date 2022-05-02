# !/usr/bin/env python
# coding: utf-8
import os
from moody.libeb import MiliDoS
from moody import Evm
from key import NETWORK, ROOT

# SOLV = "0.8.6"

CONTRACT_LIST = [
    "vault/ConnextPriceOracle.sol",
    "vault/Multicall.sol",
    "vault/PriceOracle.sol",
    "vault/ProposedOwnable.sol",
    "vault/Router.sol",
    "vault/RouterFactory.sol",
    "vault/TransactionManager.sol",
    "vault/test/Counter.sol",
    "vault/test/TestERC20.sol",
    "vault/test/FeeERC20.sol",
]

SOLV = "0.8.12"

C811 = [
    "vault/connext/Connext.sol",
    "vault/nomad/BridgeRouter.sol",
    "vault/nomad/TokenRegistry.sol"
]

r = MiliDoS(NETWORK)
print("-----> this is now started")
print(ROOT)
print("-----> now it is root")
r.setClassSolNames(C811).setWorkspace(ROOT).setEvm(Evm.LONDON).setOptimizationRuns(10000).remoteCompile(SOLV).localTranspile("app")
# r.setWorkspace(ROOT).setClassSolNames(CONTRACT_LIST).localTranspile()
# os.system("sh localpile")
