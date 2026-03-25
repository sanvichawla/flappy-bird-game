import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 40)

# ---------------- LOGIN SCREEN ----------------
username = ""
input_active = True

while input_active:
    screen.fill((30, 30, 60))

    title_font = pygame.font.Font(None, 60)
    title = title_font.render("FLAPPY BIRD", True, (255, 255, 0))
    screen.blit(title, (80, 100))

    sub_font = pygame.font.Font(None, 30)
    subtitle = sub_font.render("Enter Your Name", True, (255, 255, 255))
    screen.blit(subtitle, (120, 200))

    input_box = pygame.Rect(80, 250, 240, 50)
    pygame.draw.rect(screen, (255, 255, 255), input_box, border_radius=10)

    name_surface = sub_font.render(username, True, (0, 0, 0))
    screen.blit(name_surface, (input_box.x + 10, input_box.y + 10))

    instruction = sub_font.render("Press ENTER to Start", True, (0, 255, 0))
    screen.blit(instruction, (90, 330))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and username.strip() != "":
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                if len(username) < 12:
                    username += event.unicode

    pygame.display.update()

# ---------------- GAME SETUP ----------------
bird = pygame.Rect(100, 300, 25, 25)
velocity = 0
gravity = 0.5

pipes = []
gap = 150
spawn_timer = 0
score = 0
game_over = False

def create_pipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, 50, height)
    bottom = pygame.Rect(WIDTH, height + gap, 50, HEIGHT)
    return {"top": top, "bottom": bottom, "passed": False}

# ---------------- GAME LOOP ----------------
running = True
while running:
    screen.fill((135, 206, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                velocity = -8

    # ✅ Only run game logic if NOT game over
    if not game_over:

        velocity += gravity
        bird.y += int(velocity)

        # ✅ Boundary collision (TOP + BOTTOM)
        if bird.top <= 0 or bird.bottom >= HEIGHT:
            game_over = True

        spawn_timer += 1
        if spawn_timer > 90:
            pipes.append(create_pipe())
            spawn_timer = 0

        new_pipes = []
        for pipe in pipes:
            pipe["top"].x -= 3
            pipe["bottom"].x -= 3

            # Pipe collision
            if bird.colliderect(pipe["top"]) or bird.colliderect(pipe["bottom"]):
                game_over = True

            # Score (only once per pipe)
            if pipe["top"].x < bird.x and not pipe["passed"]:
                score += 1
                pipe["passed"] = True

            if pipe["top"].x > -50:
                new_pipes.append(pipe)

        pipes = new_pipes

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, (0, 255, 0), pipe["top"])
        pygame.draw.rect(screen, (0, 255, 0), pipe["bottom"])

    # Draw bird
    pygame.draw.circle(screen, (255, 255, 0), bird.center, 12)

    # Score display
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Player name
    name_text = font.render(f"Player: {username}", True, (0, 0, 0))
    screen.blit(name_text, (10, 40))

    # Game Over screen
    if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        final_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(over_text, (120, 250))
        screen.blit(final_text, (140, 300))

    pygame.display.update()
    clock.tick(60)
