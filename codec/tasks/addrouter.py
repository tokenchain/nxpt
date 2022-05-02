from moody.libeb import MiliDoS

from codec.gen_py.transaction_manager import TransactionManager


def add_router(j: MiliDoS, router_address: str, txManager: str):
    # router
    # assetId
    # amount
    tx_manager = TransactionManager(j, txManager)
    tx_manager.CallAutoConf(j)
    approvedRouter = tx_manager.approved_routers(router_address)
    if not approvedRouter:
        print(f"Router {router_address} is not approved")

    if approvedRouter:
        print(f"Router {router_address} is approved, no need to add")
        return

    tx_manager.add_router(router_address)

    approvedRouter = tx_manager.approved_routers(router_address)

    if not approvedRouter:
        print(f"Router {router_address} is not approved")

    if approvedRouter:
        print(f"Router {router_address} is approved")
