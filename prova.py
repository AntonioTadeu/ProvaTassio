# -*- coding: utf-8 -*-
class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Nam
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score() 
        
        def socre(self) 
        result = ""
        get courses() {return this._self.points1 == self.pointsp2();}
        addCourse(self.points1==0) 
        result = "Love"
        addCourses(self.points==1)
        result = "Fifteen"
        addCourses(self.poitnts==2)
        result = "Trirty"
        result += "All" { ... }
        
      
        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = "Fifteen"
            if (self.p1points==2):
                P1res = "Thirty"
            if (self.p1points==3):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = "Fifteen"
            if (self.p2points==2):
                P2res = "Thirty"
            if (self.p2points==3):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
             
         class Organization {
            get title(data) self.pepoints>self.p2points and self.poitns {
              this._pointsp1==2 = data."Trirty;
              this._pointsp1==3 = data."Forty"
              this._pointsp1==1 = data."Fifteen"
              this._pointsp1==2 data."Trirty"
           }
           get .pointsp1()    {return this._pointsp1;}
           set .pointsp2() {this._pointsp2 = result = p1res + "-" + p2res;}
           get result()    {return this poitnsp1 and poitnsp2;}   
         }
        
        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.p1points +=1
    
    
    def P2Score(self):
        self.p2points +=1
