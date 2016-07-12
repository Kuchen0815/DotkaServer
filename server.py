import Pyro4

@Pyro4.expose
class Server(object):
    def __init__(self):
        self.playerList = []

    def login(self, playerName):
        self.playerList.append(playerName)
        print("{0} hat sich angemeldet".format(playerName))
        return self.playerList

    def sendMove(self, playerName, actionName, unit, target, node):
        # if moves von allen spielern erhalten
        return doServerLogic("moveList")


def doServerLogic(moveList):
    return "Antwort vom Server"

def main():
    Pyro4.Daemon.serveSimple(
            {
                Server: "example.Server"
            },
            host = 'localhost',
            port = 55361,
            ns = False)

if __name__=="__main__":
    main()
