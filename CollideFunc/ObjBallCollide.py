def obj_ball_collide(type, obj, ball):
    #get circle point
    radius = ball.radius
    center = (ball.x, ball.y)
    offset = 4 
    top, bottom = (center[0], center[1] - radius - offset), (center[0], center[1] + radius + offset)
    left, right = (center[0] - radius - offset, center[1]), (center[0] + radius + offset, center[1])
    topleft, topright = (center[0] - radius//2 - offset, center[1] - radius//2 - offset), (center[0] + radius//2 + offset, center[1] - radius//2 - offset)
    bottomleft, bottomright = (center[0] - radius//2 - offset, center[1] + radius//2 + offset), (center[0] + radius//2 + offset, center[1] + radius//2 + offset)

    rect = obj.block
    if rect.collidepoint(top):
        if type == 'block':
            obj.damage(ball.damage)
        return 'top'
    elif rect.collidepoint(bottom):
        if type == 'block':
            obj.damage(ball.damage)
        return 'bottom'
    elif rect.collidepoint(left):
        if type == 'block':
            obj.damage(ball.damage)
        return 'left'
    elif rect.collidepoint(right):
        if type == 'block':
            obj.damage(ball.damage)
        return 'right'
    elif rect.collidepoint(topleft):
        if type == 'block':
            obj.damage(ball.damage)
        return 'topleft'
    elif rect.collidepoint(topright):
        if type == 'block':
            obj.damage(ball.damage)
        return 'topright'
    elif rect.collidepoint(bottomleft):
        if type == 'block':
            obj.damage(ball.damage)
        return 'bottomleft'
    elif rect.collidepoint(bottomright):
        if type == 'block':
            obj.damage(ball.damage)
        return 'bottomright'
    else:
        return 'none'