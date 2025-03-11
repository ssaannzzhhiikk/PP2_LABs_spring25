import pygame
from random import choice
pygame.init()

list_musics = ['01. BLOOD..mp3', '02. DNA..mp3', '03. YAH..mp3', '04. ELEMENT..mp3', '05. FEEL..mp3', '06. LOYALTY. (FEAT. RIHANNA.).mp3', '07. PRIDE..mp3', '08. HUMBLE..mp3', '09. LUST..mp3', '10. LOVE. (FEAT. ZACARI.).mp3', '11. XXX. (FEAT. U2.).mp3', '12. FEAR..mp3', '13. GOD..mp3', '14. DUCKWORTH.mp3']





height = 700
width = 700

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

#images
bg_image = pygame.transform.scale(pygame.image.load(r"C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\controller_images\album.jpg"), (width, height))
back_button = pygame.transform.scale( pygame.image.load(r"C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\controller_images\back.png"), (100,100))
next_button = pygame.transform.scale( pygame.image.load(r"C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\controller_images\next.png"), (100,100))
pressed_back_button = pygame.transform.scale( pygame.image.load(r"C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\controller_images\back.png"), (120,120))
pressed_next_button = pygame.transform.scale( pygame.image.load(r"C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\controller_images\next.png"), (120,120))
pause_button = pygame.transform.scale( pygame.image.load(r"C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\controller_images\pause.png"), (100,100))
play_button = pygame.transform.scale( pygame.image.load(r"C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\controller_images\play.png"), (100,100))

#Necessary variables
done = True
played = True
seq = 0

while done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            played = not played

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if seq >= 0 and seq < 13:
                seq += 1
            elif seq == 13:
                seq -= (len(list_musics)-1)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if seq > 0 and seq <= 13:
                seq -= 1
            elif seq == 0:
                seq += len(list_musics)-1

    pressed = pygame.key.get_pressed()

    #Displaying images
    screen.blit(bg_image, (0,0))
    screen.blit(next_button, (400,550))
    screen.blit(back_button, (200,550))


    #interactive control 
    if played: #play/pause
        screen.blit(play_button, (300,550))
        pygame.mixer.music.load(rf'C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\songs\{list_musics[seq]}')
        pygame.mixer.music.play(0)
    else:
        screen.blit(pause_button, (300,550))

    
    if pressed[pygame.K_LEFT]: #back
        screen.blit(pressed_back_button, (190,540))
        pygame.mixer.music.load(rf'C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\songs\{list_musics[seq]}')
        pygame.mixer.music.play(0)

    if pressed[pygame.K_RIGHT]: #next
        screen.blit(pressed_next_button, (390,540))
        pygame.mixer.music.load(rf'C:\Users\omark\OneDrive\Рабочий стол\PP2\lab7\songs\{list_musics[seq]}')
        pygame.mixer.music.play(0)
    
    
    pygame.display.flip()


pygame.quit()
