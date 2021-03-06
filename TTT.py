import copy
import random
import miniMax
class board():

    def __init__(self, _br=[['.','.','.'],['.','.','.'],['.','.','.']]):
        self.b = _br
        
    def getChildren(self,xs):
        # returns child states for game algo
        children=[]
        for i in range(len(self.b)):
            for j in range(len(self.b[i])):
                if self.b[i][j]=='.':
                    temp=copy.deepcopy(self.b)
                    if xs ==True:
                        temp[i][j]='x'
                        
                    else:
                        temp[i][j]='o'
                    tempb=board(temp)
                    children.append(tempb)    
                        
        return children   
        
    def getCols(self):
        # return md list of all columns
        cols=[[],[],[]]
        for i in range(len(self.b)):
            for j in range(len(self.b[i])):
                
                cols[j].append(self.b[i][j])
        return cols
        

    def getDiag(self):
        #returns md list of all diags
        diags=[]
        
        ltr=[self.b[0][0],self.b[1][1],self.b[2][2]]
        rtl=[self.b[0][2],self.b[1][1],self.b[2][0]]
        
        diags.append(ltr)
        diags.append(rtl)
        return diags
        
        
        
        
        
            
    
    def getState(self):
        # get the state of the board... did sombody win?
        if self.checkListThree(self.b,'x'):
            return 1
        if self.checkListThree(self.b,'o'):
            return -1 
            
        cols=self.getCols()
        if self.checkListThree(cols,'x'):
            return 1
        if self.checkListThree(cols,'o'):
            return -1 
        diags = self.getDiag()
        if self.checkListThree(diags,'x'):
            return 1
        if self.checkListThree(diags,'o'):
            return -1 

        spaceEmpty=False
        for row in self.b:
            if "." in row:
                spaceEmpty=True
        if spaceEmpty==False:
            return 0  
            
        return -2            
        
            
  
                    
        
         
                    
    def checkListThree(self,l,ch):
        # winning condition, three of the same chars in a list
        for i in range(len(l)):
            for j in range(len(l[i])):
                if not l[i][j]==ch:
                    break
                if j == len(l[i])-1:
                    return True
        return False
    
                    
    def randMove(self,xs):
        if xs==True:
            char='x'
        else:
            char='o'
        placed = False
        while placed == False:
            i=random.randint(0,2)
            j=random.randint(0,2)
            if self.b[i][j]=='.':
                self.b[i][j]=char
                placed=True             
                
        
    def __repr__(self):

        
        return "|"+self.b[0][0]+"|"+self.b[0][1]+"|"+self.b[0][2]+"|\n"+"|"+self.b[1][0]+"|"+self.b[1][1]+"|"+self.b[1][2]+"|\n"+"|"+self.b[2][0]+"|"+self.b[2][1]+"|"+self.b[2][2]+"|\n"
    
        
    
def randVSrand(): 
          
    b = board([['.','.','.'],['.','.','.'],['.','.','.']])
   

    
    
    stop = -2
    counter=0
    while stop == -2:
        if counter%2 == 0:
            b.randMove(True)
        else:
            b.randMove(False)
          
        stop=b.getState()
        print b
        print stop
        counter+=1
    return stop
 
def randVSrand(): 
          
    b = board([['.','.','.'],['.','.','.'],['.','.','.']])
   

    
    
    stop = -2
    counter=0
    while stop == -2:
        if counter%2 == 0:
            b.randMove(True)
        else:
            b.randMove(False)
          
        stop=b.getState()
        print b
        print stop
        counter+=1
    return stop 
def mmVSrand(): 
          
    b = board([['.','.','.'],['.','.','.'],['.','.','.']])
   

    
    
    stop = -2
    counter=0
    while stop == -2:
        if counter%2 == 0:
            b=miniMax.runMiniMax(b)[1]
        else:
            b.randMove(False)
          
        stop=b.getState()
        print b
        print stop
        counter+=1
    return stop      
        
         
        
            
if __name__ == "__main__":


    # play 50 games of rand vs rand
    results=[0,0,0]
    for i in range(50):
        res=randVSrand()
        if res == 1:
            results[0]+=1
        if res == 0:
            results[1]+=1
        if res == -1:
            results[2]+=1
    print results
    
    # play 50 games of rand vs minimax
    results=[0,0,0]
    for i in range(50):
        res=mmVSrand()
        if res == 1:
            results[0]+=1
        if res == 0:
            results[1]+=1
        if res == -1:
            results[2]+=1
    print results
    
     
                 

        

            
        
    
    
    
    
    
    
    
    











