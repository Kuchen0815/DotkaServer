import Pyro4

server = Pyro4.Proxy("PYRO:example.Server@localhost:55361")
print(server.login("TestName"))
print(server.sendMove("playerName", "actionName", "unit", "target", "node"))
