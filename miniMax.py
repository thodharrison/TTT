
def runMiniMax(b):
    # mini max algo wrapper
    print miniMax(b,10,True)[1]
    return miniMax(b,10,True)

def miniMax(board,depth, maximizingPlayer):
    # depth or terminal state is reached (base cas)
    if depth == 0 or board.getState()!=-2:
        return (board.getState(),board)

    # maximize for maximizing player
    if maximizingPlayer:
        bchild= None
        children=board.getChildren(maximizingPlayer)
        best=-2
        for child in children:
            val=miniMax(child,depth-1,False)
            if(val[0]>best):
                best=val[0]
                bchild=child
        return (best,bchild)
    # minimize for minimizing player
    else: 
        children=board.getChildren(not maximizingPlayer)
        best=2
        bchild=None
        for child in children:
            val=miniMax(child,depth-1,True)
            if(val[0]<best):
                best=val[0]
                bchild=child
        return (best,bchild)    
    
    
       


