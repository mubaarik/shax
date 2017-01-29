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

class ShaxSlot:
    def __init__(self, name = None, status = None):
        self.name = name;
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
    def getNeighbors(self):
        shaxMapobj = ShaxArray()
        shaxMap = shaxMapobj.getMap()
        return shaxMap[self.name];
    
        
shax_array = ["00", "03", "06",
			  "11", "13", "15",
			  "22", "23", "24",
			  "30", "31", "32",
			  "34", "35", "36",
			  "42", "43", "44",
			  "51", "53", "55",
			  "60", "63", "66"]
def shedex_chains():
    shaxChains = []
    for i in range(7):
        chain = []
        for slot in shax_array:
            if str(i) in slot:
                chain.append(slot)
        new_chains = findChains(chain, i)
        for chain in new_chains:
            shaxChains.append(chain)
    return shaxChains
def findChains(chain, i):
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
def isTopChain(chain):
        for slot in chain:
            if slot[0] >=str(3):
                return False
        return True
def isLeftChain( chain):
    for slot in chain:
        if slot[1] >=str(3):
            return False
    return True
def isRightChain(chain):
    for slot in chain:
        if slot[1] <=str(3):
            return False
    return True
def isBottomChain(chain):
    for slot in chain:
        if slot[0] <=str(3):
            return False
    return True
def chainMap():
    chain_map= {"top": [], "left": [], "right": [], "bottom": []}
    chains = shedex_chains()
    for chain in chains:
        if isTopChain(chain):
            chain_map["top"].append(chain)
        elif isLeftChain(chain):
            chain_map["left"].append(chain)
        elif isRightChain(chain):
            chain_map["right"].append(chain)
        elif isBottomChain(chain):
            chain_map["bottom"].append(chain)
        else:
            raise ValueError("How did I get Here! This chain(%s) defied classification "%str(chain))
    return chain_map

def chainLinks(chain):
    links = []
    for slot in chain:
        slot_neighbors = ShaxSlot(slot).getNeighbors()
        for neighbor in slot_neighbors:
            if neighbor not in chain:
                links.append((slot, neighbor))
    return links 

def twoChainLink(chain1, chain2):
    for link in chainLinks(chain1):
        for link2 in chainLinks(chain2):
            if link == link2 or link[::-1]==link2:
                return link 
    return None 
