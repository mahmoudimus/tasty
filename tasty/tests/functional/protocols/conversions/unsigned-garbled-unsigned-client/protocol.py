# -*- coding: utf-8 -*-

__params__ = {'la': 32, 'lb': 32, 'dima': 10, 'dimb': 10}

def protocol(client, server, params):
    la = params['la']
    lb = params['lb']
    client.a = Unsigned(bitlen=la).input(src=driver, desc="a")
    server.b = Unsigned(bitlen=lb).input(src=driver, desc="b")

    client.ga = Garbled(val=client.a)
    client.cc = Unsigned(val=client.ga)

    client.gb <<= Garbled(val=server.b)
    client.sc = Unsigned(val=client.gb)

    server.ga <<= client.ga
    client.cc2 <<= Unsigned(val=server.ga)

    server.gb = Garbled(val=server.b)
    client.sc2 <<= Unsigned(val=server.gb)

    client.sc.output(dest=driver, desc="sc")
    client.cc.output(dest=driver, desc="cc")
    client.sc2.output(dest=driver, desc="sc2")
    client.cc2.output(dest=driver, desc="cc2")

