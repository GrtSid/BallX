PLAYGROUND_WIDTH=900
PLAYGROUND_HEIGHT=500
PLAYGROUND_COLOR='yellow'
line_Color="powder blue"
line_MOVING_SPEED=2
gamevalid=1
try:
 import Tkinter
except:
 import tkinter as Tkinter
import time, random
class main(Tkinter.Tk):
    def __init__(self, *args, **kwargs):
        Tkinter.Tk.__init__(self, *args, **kwargs)
        self.creating_playground()
        self.creating_ball()
        self.creating_line()
        self.barrier_moving()
        self.scoreboard()
        self.bind('<Any-KeyPress>',self.connecting_ball_with_keys)
    def scoreboard(self):
        self.scoreboard=Tkinter.Label(self,text="Score: {}".format(self.score))
        self.scoreboard.pack(anchor='n')
        return
    def update_score_board(self):
        self.score=(self.score+1)
        self.scoreboard['text']="Score: {}".format(int(self.score/11))
    def barrier_moving(self):
        self.y=line_MOVING_SPEED
        self.y1=line_MOVING_SPEED
        self.x=0
        self.roadmap=[(0,0)]
        self.ball_target=None
        global gamevalid
        gamevalid=1
        self.score=0
        return
    def connecting_ball_with_keys(self,event=None):
        self.moving_line()
        key=event.keysym
        if key=='Left':
            self.turn_left()
        elif key=='Right':
            self.turn_right()
        else:
            pass
        return
    def turn_left(self):
        self.x=self.x-10
        self.y=0
        return
    def turn_right(self):
        self.moving_line()
        self.x=self.x+10
        self.y=0
        return
    def creating_line(self):
        x1=random.randint(15,PLAYGROUND_WIDTH-15)
        self.lin=self.board.create_rectangle(PLAYGROUND_WIDTH-x1,0,PLAYGROUND_WIDTH-x1-50,10,tag="l2",outline="yellow")
        self.line=self.board.create_rectangle(PLAYGROUND_WIDTH-x1-50,0,0,10,fill="powder blue",tag="l1",outline="yellow")
        self.line1=self.board.create_rectangle(PLAYGROUND_WIDTH,0,PLAYGROUND_WIDTH-x1,10,fill="powder blue",tag="l1",outline="yellow")

        return
    def creating_ball(self):
        self.ball=self.board.create_oval(1,PLAYGROUND_HEIGHT/2,11,PLAYGROUND_HEIGHT/2 - 10,fill="black",tag="b")
        return
    def creating_playground(self):
        self.board=Tkinter.Canvas(self,width=PLAYGROUND_WIDTH, height=PLAYGROUND_HEIGHT,background=PLAYGROUND_COLOR)
        self.board.pack(padx=10,pady=10)
        return
    def moving_line(self):
        self.board.move(self.line,0,self.y1)
        self.board.move(self.line1,0,self.y1)
        self.board.move(self.lin,0,self.y1)
        return
    def game_loss(self):
        self.board.create_text(PLAYGROUND_WIDTH/2,PLAYGROUND_HEIGHT/2,text="Game Over",font=('arial 60 bold'),fill='red')
        self.board.create_text(PLAYGROUND_WIDTH/2,PLAYGROUND_HEIGHT/2+70,text="SCORE: {}".format(int(self.score/11)),font=('arial 20 bold'),fill='powder blue')
        global gamevalid
        gamevalid=0
        return
    def moving_ball(self):
        self.board.move(self.ball,self.x,0)
        return
    def re_update(self):
        self.moving_line()
        self.moving_ball()
        self.update_line()
        return
    def update_line(self):
        x1,y1,x2,y2=self.board.coords(self.ball)
        x3,y3,x4,y4=self.board.coords(self.lin)
        x5,y5,x6,y6=self.board.coords(self.line)
        x7,y7,x8,y8=self.board.coords(self.line1)
        global line_MOVING_SPEED
        if self.ball_target==None:
            if (len(self.board.find_overlapping(x3,y3,x4,y4))>3):
                self.update_score_board()   
            if (len(self.board.find_overlapping(x5,y5,x6,y6))>2) or (len(self.board.find_overlapping(x7,y7,x8,y8))>2):
                self.board.delete('target')
                self.board.delete('l1')
                self.board.delete('l2')
                self.game_loss()
                self.board.delete('b')
            if y3>PLAYGROUND_HEIGHT/2+70:
                self.board.delete('target')
                self.board.delete('l1')
                self.board.delete('l2')
                line_MOVING_SPEED=line_MOVING_SPEED+1
                self.creating_line()
        self.ball_target=None
        return        
if __name__ == '__main__':
    root=main(className=" Game ")
    while True:
        root.update()
        root.update_idletasks()
        root.re_update()
        if gamevalid==0:
            break
        time.sleep(0.09)
            
            
            
            
        
    
        
        
    
        
        
        
        
        
        
        
    
 
  
  
