import pygame #access PyGame framework

pygame.init()       #initialize all the modules required for PyGame
screen = pygame.display.set_mode((400, 300))  #Will launch a window with desired size (width, height), it is a surface in which we will work
done = False

while not done:
    for event in pygame.event.get():  #используется для получения всех событий, которые произошли в очереди событий с момента последнего вызова
        
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
      # pygame.draw.rect(surface to draw, (colors in RGB), pygame.Rect(X,Y, width, height ))
      
        if event.type == pygame.QUIT:  #when you click the close button
            done = True
        
    pygame.display.flip() #обновляет поверхность всего окна 