import math
import pygame

# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((1000, 600))
font = pygame.font.Font(None, 30)


# Create a dot
dot_color = (255, 0, 0)
dot_radius = 5
dot_x = 0
dot_y = 0
isMaxY = False
isMaxX = False


# Create a rectangle to constrain the dot's movement
constraint_rect = pygame.Rect(50, 50, 600, 400)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    """
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
    """

    # Creates a snake like motion
    if dot_x != 850 and dot_y != 450:
        if not isMaxY:
            dot_y += 0.10
            if dot_y >= 450:
                isMaxY = True
                dot_x += 50
        else:
            dot_y -= 0.10

            if dot_y <= 50:
                isMaxY = False
                dot_x += 50

    # constrain the dot's movement to the rectangle
    if not constraint_rect.collidepoint(dot_x, dot_y):
        dot_x = max(constraint_rect.left + dot_radius, dot_x)
        dot_x = min(constraint_rect.right - dot_radius, dot_x)
        dot_y = max(constraint_rect.top + dot_radius, dot_y)
        dot_y = min(constraint_rect.bottom - dot_radius, dot_y)

    # create the vectors AB, AC, BC, AD, and CD
    AB = (dot_x - constraint_rect.topright[0],
          dot_y - constraint_rect.topright[1])
    BC = (constraint_rect.bottomright[0] - constraint_rect.topright[0],
          constraint_rect.bottomright[1] - constraint_rect.topright[1])
    AC = (constraint_rect.bottomright[0] - dot_x,
          constraint_rect.bottomright[1] - dot_y)
    AD = (constraint_rect.bottomleft[0] - dot_x,
          constraint_rect.bottomleft[1] - dot_y)
    CD = (constraint_rect.bottomright[0] - constraint_rect.bottomleft[0],
          constraint_rect.bottomright[1] - constraint_rect.bottomleft[1])

    # calculate the magnitudes of vectors
    AB_magnitude = math.sqrt(AB[0]*AB[0] + AB[1]*AB[1])
    BC_magnitude = math.sqrt(BC[0]*BC[0] + BC[1]*BC[1])
    AC_magnitude = math.sqrt(AC[0]*AC[0] + AC[1]*AC[1])
    AD_magnitude = math.sqrt(AD[0]*AD[0] + AD[1]*AD[1])
    CD_magnitude = math.sqrt(CD[0]*CD[0] + CD[1]*CD[1])

    # blue triangle
    # calculate the dot product of the vectors
    dot_product = AB[0]*BC[0] + AB[1]*BC[1]
    # calculate the angle between the vectors
    angle_B_blue = math.acos(dot_product / (AB_magnitude * BC_magnitude))
    angle_B_blue = math.degrees(angle_B_blue)

    # calculate the angle between the vectors
    angle_A_blue = abs(math.atan2(constraint_rect.topright[1] -
                                  dot_y, constraint_rect.topright[0] - dot_x) -
                       math.atan2(constraint_rect.bottomright[1] - dot_y, constraint_rect.bottomright[0] - dot_x))
    angle_A_blue = math.degrees(angle_A_blue)

    # calculate the dot product of the vectors
    dot_product = AC[0]*BC[0] + AC[1]*BC[1]
    # calculate the angle between the vectors
    angle_C_blue = math.acos(dot_product / (AC_magnitude * BC_magnitude))
    angle_C_blue = math.degrees(angle_C_blue)

    # red triangle
    dot_product = AD[0]*AC[0] + AD[1]*AC[1]
    angle_A_red = math.acos(dot_product / (AD_magnitude * AC_magnitude))
    angle_A_red = math.degrees(angle_A_red)

    dot_product = CD[0]*AC[0] + CD[1]*AC[1]
    angle_C_red = math.acos(dot_product / (CD_magnitude * AC_magnitude))
    angle_C_red = math.degrees(angle_C_red)

    angle_D_red = 180 - angle_A_red - angle_C_red

    # round the numbers to the nearest tenth
    angle_B_blue = "{:.1f}".format(angle_B_blue)
    angle_A_blue = "{:.1f}".format(angle_A_blue)
    angle_C_blue = "{:.1f}".format(angle_C_blue)
    angle_A_red = "{:.1f}".format(angle_A_red)
    angle_D_red = "{:.1f}".format(angle_D_red)
    angle_C_red = "{:.1f}".format(angle_C_red)

    # Draw the dot, the rectangle, the triangle, and the angles on the screen
    screen.fill((0, 0, 0))
    # Draw the mower as a dot
    pygame.draw.circle(screen, dot_color, (dot_x, dot_y), dot_radius)
    # Draw the contraining rectangle
    pygame.draw.rect(screen, (0, 255, 0), constraint_rect, 2)
    # Draw the new triangle using the points A, B, and C
    pygame.draw.polygon(screen, (0, 0, 255), [
                        (dot_x, dot_y), constraint_rect.topright, constraint_rect.bottomright])
    # Draw the new triangle using the points A, C, and D
    pygame.draw.polygon(screen, (255, 0, 0), [
                        (dot_x, dot_y), constraint_rect.bottomright, constraint_rect.bottomleft])
    pygame.draw.circle(screen, (255, 255, 0), constraint_rect.topright, 10)
    pygame.draw.circle(screen, (255, 255, 0), constraint_rect.bottomright, 10)
    pygame.draw.circle(screen, (255, 255, 0), constraint_rect.bottomleft, 10)

    # Draw the label of the triangle points
    screen.blit(font.render("A", True, (255, 255, 255)), (dot_x-10, dot_y-10))
    screen.blit(font.render("B", True, (255, 255, 255)),
                constraint_rect.topright)
    screen.blit(font.render("C", True, (255, 255, 255)),
                constraint_rect.bottomright)
    screen.blit(font.render("D", True, (255, 255, 255)),
                (constraint_rect.left, constraint_rect.bottom))

    # Draw the angle labels
    screen.blit(font.render("Angle A Blue =", True, (255, 255, 255)),
                (constraint_rect.right + 20, constraint_rect.top + 20))
    screen.blit(font.render("Angle B Blue =", True, (255, 255, 255)),
                (constraint_rect.right + 20, constraint_rect.top + 50))
    screen.blit(font.render("Angle C Blue =", True, (255, 255, 255)),
                (constraint_rect.right + 20, constraint_rect.top + 80))
    screen.blit(font.render("Angle A Red =", True, (255, 255, 255)),
                (constraint_rect.right + 20, constraint_rect.top + 140))
    screen.blit(font.render("Angle D Red =", True, (255, 255, 255)),
                (constraint_rect.right + 20, constraint_rect.top + 170))
    screen.blit(font.render("Angle C Red =", True, (255, 255, 255)),
                (constraint_rect.right + 20, constraint_rect.top + 200))

    # Draw the angles
    screen.blit(font.render(str(angle_A_blue)+"°", True, (255, 255, 255)),
                (constraint_rect.right + 170, constraint_rect.top + 20))
    screen.blit(font.render(str(angle_B_blue)+"°", True, (255, 255, 255)),
                (constraint_rect.right + 170, constraint_rect.top + 50))
    screen.blit(font.render(str(angle_C_blue)+"°", True, (255, 255, 255)),
                (constraint_rect.right + 170, constraint_rect.top + 80))
    screen.blit(font.render(str(angle_A_red)+"°", True, (255, 255, 255)),
                (constraint_rect.right + 165, constraint_rect.top + 140))
    screen.blit(font.render(str(angle_D_red)+"°", True, (255, 255, 255)),
                (constraint_rect.right + 165, constraint_rect.top + 170))
    screen.blit(font.render(str(angle_C_red)+"°", True, (255, 255, 255)),
                (constraint_rect.right + 165, constraint_rect.top + 200))

    pygame.display.update()


# Quit Pygame
pygame.quit()
