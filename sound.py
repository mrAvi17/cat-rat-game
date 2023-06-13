import pygame #1

#Intialize pygame
pygame.init() #2

#Create a display surface #3
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds!")

#Load sound effects #6
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

#Play the sound effects
sound_1.play() #7 Test RUN
pygame.time.delay(2000) #9 2 Seconds or 2000 nano seconds
sound_2.play() #8 Test RUN
pygame.time.delay(2000) #10

#Change the volume of a sound effect
sound_2.set_volume(.1) #11
sound_2.play() #12 Test RUN

#Load background music
pygame.mixer.music.load('music.wav') #13

#Play and stop the music #14
pygame.mixer.music.play(-1, 0.0) # -1 infinite time, 0.0 starting point
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

#The main game loop #4
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#End the game #5
pygame.quit()