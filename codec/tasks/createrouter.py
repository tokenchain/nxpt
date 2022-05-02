from moody.libeb import MiliDoS

from codec.gen_py.router_factory import RouterFactory


def create_success(a, b):
    print("awesome the router is created")
    print(a, b)


def create_router(j: MiliDoS, signer_address: str, recipient: str):
    """
    j the context
    signer address, the router's signer address
    recipient address
    """
    if j.hasContractName("RouterFactory") is False:
        print("Router Factory is not deployed.")
        exit(3)

    router_factory = RouterFactory(j, j.getAddr("RouterFactory"))
    router_factory.CallAutoConf(j)
    router_address_from_signer = router_factory.get_router_address(signer_address)

    router_factory.onSuccssCallback(create_success)
    router_factory.create_router(signer_address, recipient)

    router_address = router_factory.router_addresses(signer_address)

    print(f"Router address got from the factory {router_address}")
    print(f"Router address get from the factory {router_address_from_signer}")
