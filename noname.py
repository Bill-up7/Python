import turtle
import random
import sqlite3

# -----------------------------
# Database setup
# -----------------------------
conn = sqlite3.connect('highscores.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player TEXT NOT NULL,
    score INTEGER NOT NULL
)
''')
conn.commit()

# -----------------------------
# Game setup
# -----------------------------
wn = turtle.Screen()
wn.title("Collect the Coins Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Player setup
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.goto(0, 0)

# Coin setup
coin = turtle.Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.speed(0)
coin.goto(random.randint(-250, 250), random.randint(-250, 250))

# Score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-280, 260)
score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# -----------------------------
# Functions
# -----------------------------
def go_up():
    y = player.ycor()
    player.sety(y + 20)

def go_down():
    y = player.ycor()
    player.sety(y - 20)

def go_left():
    x = player.xcor()
    player.setx(x - 20)

def go_right():
    x = player.xcor()
    player.setx(x + 20)

def check_collision():
    global score
    if player.distance(coin) < 20:
        score += 10
        coin.goto(random.randint(-250, 250), random.randint(-250, 250))
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# -----------------------------
# Keyboard bindings
# -----------------------------
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# -----------------------------
# Main game loop
# -----------------------------
def game_loop():
    check_collision()
    wn.ontimer(game_loop, 100)

game_loop()

# -----------------------------
# On close, save high score
# -----------------------------
def save_score():
    player_name = wn.textinput("Game Over", "Enter your name for the high score:")
    if player_name:
        c.execute("INSERT INTO scores (player, score) VALUES (?, ?)", (player_name, score))
        conn.commit()
    conn.close()

wn.mainloop()
save_score()
