import pygame, math

vector_sprites = {
    1 : ((0, 0), (5, 0), (5, 5), (0, 5)),
    2 : ((1, 0.5), (0, 0), (1, 3), (2, 0))
}

def scribe(sprite, pos, scale, angle, surface):
    try:
        sprite_dict = vector_sprites[sprite]

    except KeyError:
        print(f"{sprite} is not a valid sprite key")
        return

    adjusted_sprite = []
    for cord in sprite_dict:
        adjusted_sprite.append(((cord[0]*scale) + pos[0], (cord[1]*scale) + pos[1]))
    pygame.draw.lines(surface, (255, 255, 255), True, rotate_points(adjusted_sprite, angle))
  
    
def rotate_points(points, angle):
    
    center = get_center(points)
    rot_points = []

    for point in points:
        rotatedX = math.cos(angle) * (point[0] - center[0]) - math.sin(angle) * (point[1]-center[1]) + center[0]
        rotatedY = math.sin(angle) * (point[0]- center[0]) + math.cos(angle) * (point[1] - center[1]) + center[1]

        rot_points.append([rotatedX, rotatedY])
    
    return rot_points
    
def get_center(points):
        center = [0, 0]
        ### find the center of mass
        point_count = 0
        for point in points:
            center[0] += point[0]
            center[1] += point[1]
            point_count +=1

        center = [center[0]/point_count, center[1]/point_count]
        return center

    
    