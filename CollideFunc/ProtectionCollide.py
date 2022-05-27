from Constans.Valuable import HEIGHT, PROTECTION_HEIGHT

def protection_collide(ball):
    #get circle point
    radius = ball.radius
    center = (ball.x, ball.y)
    offset = 4
    bottom = (center[0], center[1] + radius + offset)

    if bottom[1] >= HEIGHT - PROTECTION_HEIGHT:
        return 'bottom'
    else:
        return 'none'