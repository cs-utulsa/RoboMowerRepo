import pygame
import math

# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 30)

# Create a dot
dot_color = (255, 0, 0)
dot_radius = 5
dot_x = 200
dot_y = 150

# Create a rectangle to constrain the dot's movement
constraint_rect = pygame.Rect(50, 50, 600, 400)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of the arrow keys
    keys = pygame.key.get_pressed()

    # Update the dot's position based on the arrow keys
    if keys[pygame.K_LEFT]:
        dot_x -= .25
    if keys[pygame.K_RIGHT]:
        dot_x += .25
    if keys[pygame.K_UP]:
        dot_y -= .25
    if keys[pygame.K_DOWN]:
        dot_y += .25

    # Constrain the dot's movement to the rectangle
    if not constraint_rect.collidepoint(dot_x, dot_y):
        dot_x = max(constraint_rect.left + dot_radius, dot_x)
        dot_x = min(constraint_rect.right - dot_radius, dot_x)
        dot_y = max(constraint_rect.top + dot_radius, dot_y)
        dot_y = min(constraint_rect.bottom - dot_radius, dot_y)

    angle_A = abs(math.atan2(constraint_rect.topright[1]-dot_y,constraint_rect.topright[0]-dot_x)-math.atan2(constraint_rect.bottomright[1]-dot_y,constraint_rect.bottomright[0]-dot_x))
    angle_A = math.degrees(angle_A)

    angle_B = abs(math.atan2(constraint_rect.topright[1]-dot_y,constraint_rect.topright[0]-dot_x)-math.pi/2)
    angle_B = math.degrees(angle_B)







    # Draw the dot, the rectangle, the triangle, and the angles on the screen
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, dot_color, (dot_x, dot_y), dot_radius)
    pygame.draw.rect(screen, (0, 255, 0), constraint_rect, 2)
    pygame.draw.polygon(screen, (0, 0, 255), [(dot_x, dot_y), constraint_rect.topright, constraint_rect.bottomright])

    # Draw the label of the triangle points
    screen.blit(font.render("A", True, (0, 0, 255)), (dot_x-10, dot_y-10))
    screen.blit(font.render("B", True, (0, 0, 255)), constraint_rect.topright)
    screen.blit(font.render("C", True, (0, 0, 255)), constraint_rect.bottomright)
    # Draw the angle A
    screen.blit(font.render(str(angle_A)+"°", True, (255, 0, 0)), (dot_x-20, dot_y-30))
    # Draw the angle B
    screen.blit(font.render(str(angle_B)+"°", True, (255, 0, 0)), constraint_rect.topright)


    pygame.display.update()



# Quit Pygame
pygame.quit()
