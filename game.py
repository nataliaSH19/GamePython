class Area():
 def init(self, x=0, y=0, width =10, height =10, color=None):
  self.rect = pygame.Rect(x, y, width, height)#прямокутник
  self.fill_color = color


 def color(self, new_color):
  self.fill_color = new_color


 def fill(self):
   pygame.draw.rect(mw,self.fill_color,self.rect)
 def outline(self, frame_color, thickness):#обведення існуючого прямокутника
  pygame.draw.rect(mw, frame_color,self.rect, thickness)