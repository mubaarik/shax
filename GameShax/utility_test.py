import Tkinter as tk
class ShaxArray:
    def __init__(self):
        ## these are th valid slots in shax, which can be reperented as 7X7 matrix.
        ## But only the slot in shax_array which are "rowclumn" are valid slots
        self.shax_array = ["00", "03", "06",
              "11", "13", "15",
              "22", "23", "24",
              "30", "31", "32",
              "34", "35", "36",
              "42", "43", "44",
              "51", "53", "55",
              "60", "63", "66"]
        ##maps valid shax slots to their neighbors
        self.shaxNeighborMap = {
        "00": ["30", "03"],"03": ["00", "06", "13"],"06": ["03", "36"],
        "11": ["31", "13"],"13":["11","03","15", "23"],"15":["13","35"],
        "22":["23", "32"], "23":["13", "22", "24"], "24": ["23", "34"],
        "30": ["00", "60", "31"], "31": ["30", "11", "32", "51"], "32": ["22", "42", "31"],
        "34": ["24", "44","35"],"35":["15", "34","55", "36"],"36": ["06", "35", "66"],
        "42": ["32", "43"], "43":["42", "53","44"],"44": ["43", "34"],
        "51": ["53", "31"],"53":["51","43", "55", "63"],"55":["53", "35"],
        "60": ["30","63"], "63": ["53","60","66"],"66": ["63", "36"]

        }
    def getShaxArray(self):
        return self.shax_array;
    def getMap(self):
        return self.shaxNeighborMap

class ShaxSlot:#(tk.Button):
    def __init__(self,tk = tk,name = None, status = None, height = 30, width = 30):
        #tk.Button.__init__(self)
        self.height = height;
        self.width = width;
        self.name = name;
        self.tk = tk;
        self.status = status;
        self.neighbors = self.getNeighbors();
        if status ==None:
            self.status = False;
    def getName(self):
        return self.name;
    def setName(self,name):
        self.name = name;
    def getStatus(self):
        return self.status;
    def setStatus(self,status):
        self.status = status;
    #Get the neighbors of the slot using the map
    def getNeighbors(self):
        shaxMap = ShaxArray().getMap()
        return shaxMap[self.name];
    def slotIrmans(self):
        pass
    def slotButton(self, width, height, pad_x, pad_y):
        bg_color = "green"
        bState = self.tk.ACTIVE
        if self.status == True:
            bState = self.tk.NORMAL
            bg_color = "grey"
        b = self.tk.Button(text = self.name,  bg = bg_color, state = bState)
        _x, _y = self.findPose(self.name, width, height, pad_x, pad_y)
        b.place(x = _x, y = _y)
    def findPose(self,name, width, height, pad_x, pad_y):
        name_x = float(name[0])
        name_y = float(name[1])

        x = round((width - pad_x)/6.0*name_x + pad_x)
        y = round((height - pad_y)/6.0*name_y + pad_y)

        return x, y 
    def neiPathDisp(self,width, height, pad_x, pad_y):
        slotNeis = self.getNeighbors()
        for neib in slotNeis:
            x,y = self.findPose(neib, width, height, pad_x, pad_y)
            nx,ny = self.findPose(neib, width, height, pad_x, pad_y)
            canvas = self.tk.Canvas(self)
            
            if neib[0] == self.name[0]:
                ny = ny+self.height
                canvas.create_rectangle(x, y, nx, ny, outline="#fb0", fill="#fb0")
                canvas.pack()
            else:
                nx = self.width+nx;
                canvas.create_rectangle(x, y, nx, ny, outline="#fb0", fill="#fb0")
                canvas.pack()






class Shax:
    ## board_map-> dictionary mapping slots to players or slot to None if the slot is not occupied.
    ## Players -> two players to play the game
    ## whos_turn -> indicates who moves or put a piece down
    ## game_state-> indicates whether the players are putting their pieces down or making moves 
    def __init__(self, board_map = None, players = ['player_one', 'player_two'], whos_turn = None, game_state = None):
        self.shax_array = ShaxArray().getShaxArray()
        self.board_map = board_map;
        if board_map == None:
            self.board_map = self.getEmptyShaxBoard()
        self.players = players;
        self.whos_turn = whos_turn;
        if whos_turn == None:
            self.whos_turn = self.players[0];
        self.game_state = game_state
        if game_state == None:
            self.game_state = "degmo"

    ##set the players in the game
    def setPlayers(self, players):
        if isinstance(players, list) or isinstance(players, list):
            if len(players)==2:
                self.players = players;
            else:#make sure that there are only two players
                raise ValueError("expected two players; found %s players"%len(players));
        else:
            raise ValueError("expected list or a tuple; found %s:\n" %type(players).__name__);

    def getPlayers(self):
        return self.players;
    #Set who should move or put a piece down next
    def setWhos_turn(self, player):
        if player in self.players:
            self.whos_turn = player;
        else:
            raise ValueError("expected %s"%self.player[0]+"or %s;"%self.players[1] +"found %s! Make sure the current player is in the game."%player);
    def geWhos_turn(self):
        return self.whos_turn

    ## initialize the shax occupance
    def getEmptyShaxBoard(self):
        shax_map = {}
        shaxArray = self.shax_array
        for name in shaxArray:
            shax_map[name] = "x";
        return shax_map
    def setMapElement(self, slot, value):
        if not slot in self.board_map:
            raise ValueError("please provide a valid shaxSlot")
        elif value not in [0,1, "x"]:
            raise ValueError("please provide a player in the games or string x")
        else:
            self.board_map[slot]=value 
    #print the a snap shot of the current state
    def printSnapShot(self):
        print ("\n"+str(self.board_map["00"])+"___________"+str(self.board_map["03"])+"__________"+str(self.board_map["06"])+"\n"+
               "|           |          |\n"+
        "|  "+str(self.board_map["11"])+"________"+str(self.board_map["13"])+"_______"+str(self.board_map["15"])+"  |"+"\n"+
               "|  |        |       |  |\n"+
        "|  |  "+str(self.board_map["22"])+"_____"+str(self.board_map["23"])+"____"+str(self.board_map["24"])+"  |  |"+"\n"+
            "|  |  |          |  |  |\n"+str(self.board_map["30"])+"__"+str(self.board_map["31"])+"__"+str(self.board_map["32"])+"     "+
            "     "+str(self.board_map["34"])+"__"+str(self.board_map["35"])+"__"+str(self.board_map["36"])+"\n"+"|  |  |          |  |  |\n"+
            "|  |  "+str(self.board_map["42"])+"_____"+str(self.board_map["43"])+"____"+str(self.board_map["44"])+"  |  |"+"\n"+
               "|  |        |       |  |\n"+"|  "+str(self.board_map["51"])+"________"+str(self.board_map["53"])+"_______"+str(self.board_map["55"])+"  |"+"\n"+
              "|           |          |\n"+str(self.board_map["60"])+"___________"+str(self.board_map["63"])+"__________"+str(self.board_map["66"])+"\n" )
    ##Find the valid sedex(three in Somali) chains
    ## Uses FindChains to find chains from collection of neighboring slots
    def shedex_chains(self):
        shaxChains = []
        for i in range(7):
            chain = []
            for slot in self.shax_array:
                if str(i) in slot:
                    chain.append(slot)
            new_chains = self.findChains(chain, i)
            for chain in new_chains:
                shaxChains.append(chain)
        return shaxChains
    ##// Chains in a list of slots sharing a column and a row and the row/column number
    ##// Contructs chains of three from that list
    def findChains(self,chain, i):
        if i!= 3:
            chains = [[],[]]
            for slot in chain:

                if slot[0]==str(i):
                    chains[0].append(slot)
                if slot[1]==str(i):
                    chains[1].append(slot)
            return chains
        else:
            chains = [[],[], [],[]]
            for slot in chain:
                if slot[0]==str(i):
                    if slot[1]<str(i):
                        chains[1].append(slot)
                    elif slot[1]>str(i):
                        chains[2].append(slot)
                elif slot[1] == str(i):
                    if slot[0]<str(i):
                        chains[0].append(slot)
                    elif slot[0]>str(i):
                        chains[3].append(slot)
            return chains
    def playerSedex(self, player):
        sedexs = self.shedex_chains()
        players = []
        for sedex in sedexs:
            match = True 
            for slot in sedex:
                if self.board_map[slot]!=player:
                    match = False
            if match:
                players.append(sedex)
        return players
    def isTopChain(self, chain):
        for slot in chain:
            if slot[0] >=str(3):
                return False
        return True
    def isLeftChain(self, chain):
        for slot in chain:
            if slot[1] >=str(3):
                return False
        return True
    def isRightChain(self, chain):
        for slot in chain:
            if slot[1] <=str(3):
                return False
        return True
    def isBottomChain(self, chain):
        for slot in chain:
            if slot[0] <=str(3):
                return False
        return True
    def chainMap(self):
        chain_map= {"top": [], "left": [], "right": [], "bottom": []}
        chains = self.shedex_chains()
        for chain in chains:
            if self.isTopChain(chain):
                chain_map["top"].append(chain)
            elif self.isLeftChain(chain):
                chain_map["left"].append(chain)
            elif self.isRightChain(chain):
                chain_map["right"].append(chain)
            elif self.isBottomChain(chain):
                chain_map["bottom"].append(chain)
            else:
                raise ValueError("How did I get Here! This chain(%s) defied classification "%str(chain))
        return chain_map
    def chainCommon(self, chain):
        if chain[0][0]==chain[1][0]:
            return chain[0][0]
        else:
            return chain[0][1]
    def chainLinks(self, chain):
        links = []
        for slot in chain:
            slot_neighbors = ShaxSlot(slot).getNeighbors()
            for neighbor in slot_neighbors:
                if neighbor not in chain:
                    links.append((slot, neighbor))
        return links 

    def twoChainLink(self, chain1, chain2):
        if chain1 == chain2:
            return None
        for link in self.chainLinks(chain1):
            for link2 in self.chainLinks(chain2):
                if link == link2 or link[::-1]==link2:
                    return link 
        return None 

        

    def sedex_link_map(self):
        sedexChains = self.shedex_chains()
        sedex_map = {}
        for sedex in sedexChains:
            for otherSedex in sedexChains:
                link = self.twoChainLink(sedex, otherSedex)
                if link!=None:
                    if str(sedex) not in sedex_map:
                        sedex_map[str(sedex)] = [otherSedex]
                    else:
                        sedex_map[str(sedex)].append(otherSedex)
        return sedex_map

    def playerIrmans(self, player):
        player_chains = self.playerSedex(player)
        game_chains = self.shedex_chains()
        player_irmans = []
        for sedex in player_chains:
            for gsedex in game_chains:
                link = self.twoChainLink(sedex, gsedex)
                if link!=None:
                    link_other = link[0]
                    if link_other in sedex:
                        link_other=link[1]
                    other_slots = [x for x in gsedex if x!=link_other]
                    print other_slots, link_other
                    if self.game_state == "degmo":
                        if self.board_map[other_slots[0]] == player and self.board_map[other_slots[1]] == player:
                            player_irmans.append(sedex+other_slots)
                    else:
                        if self.board_map[link_other]=="x" and self.board_map[other_slots[0]] == player and self.board_map[other_slots[1]] == player:
                            print "check"
                            player_irmans.append(sedex+other_slots)
        return player_irmans

    def display(self,width, height, pad_x, pad_y):
        shaxArrObj = ShaxArray()
        shax_array = shaxArrObj.shax_array
        shaxObjArr = []
        for slot in shax_array:
            slotObj = ShaxSlot(name = slot)
            slotObj.slotButton(width, height, pad_x, pad_y)
            shaxObjArr.append(slotObj)
        return shaxObjArr



    def slotSedexChains(self, slot):
        pass
    def ShaxIrmans(self):
        pass 



    def findSecondSlots(self, slotOne):
        similarity = 1
        for slot in shax_array:
            if slot!=slotOne:
                pass


def disp_test():
    root = tk.Tk()
    width = 500;
    height = 500;
    pad_x = 50;
    pad_y = 50;

    frame = tk.Frame(root, height = height, width = width)
    frame.pack()
    shaxObj = Shax()
    shaxObj.display(width, height, pad_x, pad_y)
    root.mainloop()
def test_player(player = None, slot = None):
    shaxObj = Shax()
    shaxArrObj = ShaxArray()

    marray = shaxArrObj.getShaxArray()[:]
    import random 
    while marray:
        left = len(marray)
        j = random.choice(range(left))
        k = random.choice(range(left))
        if k>j:
            
            slot1 = marray.pop(k)
            slot2 = marray.pop(j)
            shaxObj.setMapElement(slot1, 0)
            shaxObj.setMapElement(slot2, 1)
        else:
            slot1 = marray.pop(j)
            slot2 = marray.pop(k)
            shaxObj.setMapElement(slot1, 0)
            shaxObj.setMapElement(slot2, 1)
    return shaxObj






