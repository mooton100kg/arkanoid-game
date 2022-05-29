from Constans.Valuable import WIDTH
from Constans.Sound import COLLIDE_SOUND

def border_collide(ball):
    #get circle point
    radius = ball.radius
    center = (ball.x, ball.y)
    offset = 4
    top= (center[0], center[1] - radius - offset)
    left, right = (center[0] - radius - offset, center[1]), (center[0] + radius + offset, center[1])

    if top[1] <= 0:
        COLLIDE_SOUND.play()
        return 'top'
    elif left[0] <= 0:
        COLLIDE_SOUND.play()
        return 'left'
    elif right[0] >= WIDTH:
        COLLIDE_SOUND.play()
        return 'right'
    else:
        return 'none'