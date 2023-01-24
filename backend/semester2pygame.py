import math

import pygame

# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((1000, 600))
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


    # calculate the vectors AB and BC
    AB = (dot_x - constraint_rect.topright[0], dot_y - constraint_rect.topright[1])
    BC = (constraint_rect.bottomright[0] - constraint_rect.topright[0], constraint_rect.bottomright[1] - constraint_rect.topright[1])
    # calculate the dot product of the vectors
    dot_product = AB[0]*BC[0] + AB[1]*BC[1]
    # calculate the magnitude of the vectors
    AB_magnitude = math.sqrt(AB[0]*AB[0] + AB[1]*AB[1])
    BC_magnitude = math.sqrt(BC[0]*BC[0] + BC[1]*BC[1])
    # calculate the angle between the vectors
    angle_B = math.acos(dot_product / (AB_magnitude * BC_magnitude))
    angle_B = math.degrees(angle_B)

    # calculate the vectors BC and AC
    AC = (constraint_rect.bottomright[0] - dot_x, constraint_rect.bottomright[1] - dot_y)
    # calculate the dot product of the vectors
    dot_product = BC[0]*AC[0] + BC[1]*AC[1]
    # calculate the magnitude of the vectors
    AC_magnitude = math.sqrt(AC[0]*AC[0] + AC[1]*AC[1])
    # calculate the angle between the vectors
    angle_C = math.acos(dot_product / (BC_magnitude * AC_magnitude))
    angle_C = math.degrees(angle_C)


    # Create a new point D at the bottom left of the constraining rectangle
    point_D = (constraint_rect.left, constraint_rect.bottom)

    # Calculate the angle A prime using the lines from point A to C and point A to D
    AC = (constraint_rect.bottomright[0] - dot_x, constraint_rect.bottomright[1] - dot_y)
    AD = (point_D[0] - dot_x, point_D[1] - dot_y)
    dot_product = AC[0]*AD[0] + AC[1]*AD[1]
    AC_magnitude = math.sqrt(AC[0]*AC[0] + AC[1]*AC[1])
    AD_magnitude = math.sqrt(AD[0]*AD[0] + AD[1]*AD[1])
    angle_A_prime = math.acos(dot_product / (AC_magnitude * AD_magnitude))
    angle_A_prime = math.degrees(angle_A_prime)





    # Draw the dot, the rectangle, the triangle, and the angles on the screen
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, dot_color, (dot_x, dot_y), dot_radius)
    pygame.draw.rect(screen, (0, 255, 0), constraint_rect, 2)
    pygame.draw.polygon(screen, (0, 0, 255), [(dot_x, dot_y), constraint_rect.topright, constraint_rect.bottomright])
    # pygame.draw.circle(screen, dot_color, constraint_rect.bottomleft, dot_radius)
    pygame.draw.polygon(screen, (255, 0, 0),
                        [(dot_x, dot_y), constraint_rect.bottomright,
                         (constraint_rect.left, constraint_rect.bottom)])

    # Draw the new triangle using the points A, C, and D
    pygame.draw.polygon(screen, (255, 0, 0), [(dot_x, dot_y), constraint_rect.bottomright, point_D])



    # Draw the label of the triangle points
    screen.blit(font.render("A", True, (255, 255, 255)), (dot_x-10, dot_y-10))
    screen.blit(font.render("B", True, (255, 255, 255)), constraint_rect.topright)
    screen.blit(font.render("C", True, (255, 255, 255)), constraint_rect.bottomright)
    screen.blit(font.render("D", True, (255, 255, 255)), (constraint_rect.left, constraint_rect.bottom))


    # Draw the angle labels
    screen.blit(font.render("Angle A =", True, (255, 255, 255)), (constraint_rect.right + 20, constraint_rect.top + 20))
    screen.blit(font.render("Angle B =", True, (255, 255, 255)), (constraint_rect.right + 20, constraint_rect.top + 50))
    screen.blit(font.render("Angle C =", True, (255, 255, 255)), (constraint_rect.right + 20, constraint_rect.top + 80))
    screen.blit(font.render("Angle A Red =", True, (255, 255, 255)), (constraint_rect.right + 20, constraint_rect.top + 110))

    # Draw the angles
    screen.blit(font.render(str(angle_A)+"°", True, (255, 255, 255)), (constraint_rect.right + 120, constraint_rect.top + 20))
    screen.blit(font.render(str(angle_B)+"°", True, (255, 255, 255)), (constraint_rect.right + 120, constraint_rect.top + 50))
    screen.blit(font.render(str(angle_C)+"°", True, (255, 255, 255)), (constraint_rect.right + 120, constraint_rect.top + 80))
    screen.blit(font.render(str(angle_A_prime)+"°", True, (255, 255, 255)), (constraint_rect.right + 165, constraint_rect.top + 110))



    pygame.display.update()



# Quit Pygame
pygame.quit()
