def collision(ball, ball2):
    x1, y1 = ball.coords
    x2, y2 = ball2.coords
    black_k = (y1 - y2) / (x1 - x2)
    black_b = y1 - black_k * x1
    i = ball.vel[0] - ball2.vel[0] + x1
    j = ball.vel[1] - ball2.vel[1] + y1
    orange_k = -(x1 - x2) / (y1 - y2)
    orange_b = j - orange_k * i
    x = (orange_b - black_b) / (black_k - orange_k)
    y = orange_k * x + orange_b
    x, y = x - x1, y - y1
    x3, y3 = i - x, j - y
