import pygame

pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
SIZE = ([WIDTH, HEIGHT])
TITLE = "Gradient"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
start = (0, 150, 200)
end = (255, 200, 75)

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code
    for y in range(HEIGHT):
        r = int((end[0] - start[0]) * y / HEIGHT)
        g = int(start[1] + (end[1] - start[1]) * y / HEIGHT)
        b = int(start[2] + (end[2] - start[2]) * y / HEIGHT)

        pygame.draw.line(screen, [r, g, b], [0, y], [WIDTH, y])

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
