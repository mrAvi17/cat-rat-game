import pygame
import random

# Initialize Pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

# Create images
cat_image = pygame.image.load("cat.png")
cat_rect = cat_image.get_rect()
cat_rect.topleft = (0, 0)

rat_image = pygame.image.load("rat.png")
rat_rect = rat_image.get_rect()
rat_rect.topright = (WINDOW_WIDTH, 200)

# Set initial movement values
dx = 0
dy = 0

# Load sound effects
eat_sound = pygame.mixer.Sound("cat-meow-6226.wav")

# Set background music
pygame.mixer.music.load("music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # Play the music in a loop

# Score
score = 0
font = pygame.font.Font(None, 50)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -2  # Move left
            elif event.key == pygame.K_RIGHT:
                dx = 2  # Move right
            elif event.key == pygame.K_UP:
                dy = -2  # Move up
            elif event.key == pygame.K_DOWN:
                dy = 2  # Move down

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0  # Stop horizontal movement
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0  # Stop vertical movement

    # Update image positions based on movement
    cat_rect.x += dx
    cat_rect.y += dy

    # Check boundaries to prevent images from going off-screen
    if cat_rect.left < 0:
        cat_rect.left = 0
    elif cat_rect.right > WINDOW_WIDTH:
        cat_rect.right = WINDOW_WIDTH
    if cat_rect.top < 0:
        cat_rect.top = 0
    elif cat_rect.bottom > WINDOW_HEIGHT:
        cat_rect.bottom = WINDOW_HEIGHT

    # Collision detection
    if cat_rect.colliderect(rat_rect):
        rat_rect.x = random.randint(0, WINDOW_WIDTH - rat_rect.width)
        rat_rect.y = random.randint(0, WINDOW_HEIGHT - rat_rect.height)
        score += 1
        eat_sound.play()

    # Fill the display surface with white color
    display_surface.fill((255, 255, 255))

    # Blit (copy) the images onto the display surface
    display_surface.blit(cat_image, cat_rect)
    display_surface.blit(rat_image, rat_rect)

    # Display score
    score_text = font.render(" Your Score: " + str(score), True, (0, 0, 0))
    display_surface.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

# Stop background music when the game ends
pygame.mixer.music.stop()

# End the game
pygame.quit()
