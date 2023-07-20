#huffman.py

class Nodes:
    def __init__(self, probability, symbol, left=None, right=None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''
  
def CalculateProbability(the_data):  
    the_symbols = dict()  
    for item in the_data:  
        if the_symbols.get(item) == None:  
            the_symbols[item] = 1  
        else:   
            the_symbols[item] += 1       
    return the_symbols  
   
the_codes = dict()  
  
def CalculateCodes(node, value = ''):  
    newValue = value + str(node.code)  
  
    if(node.left):  
        CalculateCodes(node.left, newValue)  
    if(node.right):  
        CalculateCodes(node.right, newValue)  
  
    if(not node.left and not node.right):  
        the_codes[node.symbol] = newValue  
           
    return the_codes  

def OutputEncoded(the_data, coding):  
    encodingOutput = []  
    for element in the_data:   
        encodingOutput.append(coding[element])  
          
    the_string = ''.join([str(item) for item in encodingOutput])      
    return the_string  

def TotalGain(the_data, coding):  
    beforeCompression = len(the_data) * 8  
    afterCompression = 0  
    the_symbols = coding.keys()  
    for symbol in the_symbols:  
        the_count = the_data.count(symbol)   
        afterCompression += the_count * len(coding[symbol])  
    print("Space usage before compression (in bits):", beforeCompression)  
    print("Space usage after compression (in bits):",  afterCompression)  
huffmanTree = None

def HuffmanEncoding(the_data):
    global huffmanTree 
    symbolWithProbs = CalculateProbability(the_data)  
    the_symbols = symbolWithProbs.keys()  
    the_probabilities = symbolWithProbs.values()  
    print("symbols: ", the_symbols)  
    print("probabilities: ", the_probabilities)  
      
    the_nodes = []  
    for symbol in the_symbols:  
        the_nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))  
      
    while len(the_nodes) > 1:  
        the_nodes = sorted(the_nodes, key = lambda x: x.probability)  
        right = the_nodes[0]  
        left = the_nodes[1]        
        left.code = 0  
        right.code = 1  
        newNode = Nodes(left.probability + right.probability, left.symbol + right.symbol, left, right)        
        the_nodes.remove(left)  
        the_nodes.remove(right)  
        the_nodes.append(newNode)  
              
    huffmanEncoding = CalculateCodes(the_nodes[0])  
    print("symbols with codes", huffmanEncoding)  
    TotalGain(the_data, huffmanEncoding)  
    encodedOutput = OutputEncoded(the_data,huffmanEncoding)  
    huffmanTree = the_nodes[0]

    return encodedOutput

def HuffmanDecoding(encodedData):
    global huffmanTree 
    decodedOutput = []  
    currentNode = huffmanTree
    for x in encodedData:
        if x == '1':  
            currentNode = currentNode.right
        elif x == '0':
            currentNode = currentNode.left
        try:
            if currentNode.left is None and currentNode.right is None:
                decodedOutput.append(currentNode.symbol)
                currentNode = huffmanTree
        except AttributeError:
            pass            
 
    print(decodedOutput)
    return decodedOutput


