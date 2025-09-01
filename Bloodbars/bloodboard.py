import tkinter as tk
import random
import time

# -----------------------------
# Dodge the Falling Blocks
# -----------------------------
# Controls:
#   ← →  : Move
#   P    : Pause/Resume
#   R    : Restart after Game Over
#
# Goal:
#   Survive as long as possible by dodging falling blocks.
#   Your score increases over time; higher difficulty ramps automatically.
# -----------------------------

WIDTH, HEIGHT = 600, 420
GROUND_Y = HEIGHT - 20
PLAYER_W, PLAYER_H = 40, 14
PLAYER_SPEED = 7

OB_MIN_W, OB_MAX_W = 24, 64
OB_MIN_H, OB_MAX_H = 16, 28
OB_MIN_V, OB_MAX_V = 3, 7

SPAWN_INTERVAL_START = 900   # ms
SPAWN_INTERVAL_MIN = 280     # ms
DIFFICULTY_RAMP_MS = 6000    # lower spawn interval every N ms
SPAWN_STEP = 40

TICK_MS = 16                 # ~60 FPS

class Game:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Dodge the Falling Blocks — Tkinter")
        root.resizable(False,False )

        self.frame = tk.Frame(root, bg="#090942")
        self.frame.pack(fill=tk.BOTH, expand=True)

        topbar = tk.Frame(self.frame, bg="#0f0f12")
        topbar.pack(fill=tk.X)
        self.score_var = tk.StringVar(value="Score: 0")
        self.status_var = tk.StringVar(value="← → move | P pause | R restart")
        self.lbl_score = tk.Label(topbar, textvariable=self.score_var, fg="#e8e8ef", bg="#0f0f12", font=("Segoe UI", 12, "bold"))
        self.lbl_score.pack(side=tk.LEFT, padx=10, pady=8)
        self.lbl_status = tk.Label(topbar, textvariable=self.status_var, fg="#a9abb3", bg="#0f0f12", font=("Segoe UI", 10))
        self.lbl_status.pack(side=tk.RIGHT, padx=10)

        self.canvas = tk.Canvas(self.frame, width=WIDTH, height=HEIGHT, bg="#111216", highlightthickness=0)
        self.canvas.pack(padx=12, pady=10)

        # Ground
        self.canvas.create_rectangle(0, GROUND_Y, WIDTH, HEIGHT, fill="#1c1e23", outline="")

        # Player
        start_x = WIDTH // 2
        self.player = self.canvas.create_rectangle(0, 0, PLAYER_W, PLAYER_H, fill="#62a5ff", outline="")
        self.canvas.move(self.player, start_x - PLAYER_W // 2, GROUND_Y - PLAYER_H - 3)

        # Movement state
        self.moving_left = False
        self.moving_right = False

        # Game state
        self.obstacles = []
        self.score = 0
        self.running = True
        self.game_over = False
        self.last_spawn_time = time.time()
        self.spawn_interval = SPAWN_INTERVAL_START
        self.last_ramp = time.time()
        self.last_tick_time = time.time()

        # Bindings
        root.bind('<KeyPress-Left>', self.on_key_down)
        root.bind('<KeyPress-Right>', self.on_key_down)
        root.bind('<KeyRelease-Left>', self.on_key_up)
        root.bind('<KeyRelease-Right>', self.on_key_up)
        root.bind('<KeyPress-p>', self.toggle_pause)
        root.bind('<KeyPress-P>', self.toggle_pause)
        root.bind('<KeyPress-r>', self.restart)
        root.bind('<KeyPress-R>', self.restart)

        self.loop()

    # ---------------------- Input ----------------------
    def on_key_down(self, e):
        if self.game_over:
            return
        if e.keysym == 'Left':
            self.moving_left = True
        elif e.keysym == 'Right':
            self.moving_right = True

    def on_key_up(self, e):
        if e.keysym == 'Left':
            self.moving_left = False
        elif e.keysym == 'Right':
            self.moving_right = False

    def toggle_pause(self, _=None):
        if self.game_over:
            return
        self.running = not self.running
        self.status_var.set("PAUSED — press P to resume" if not self.running else "← → move | P pause | R restart")

    # ---------------------- Game Logic ----------------------
    def loop(self):
        now = time.time()

        if self.running and not self.game_over:
            self.update_player()
            self.maybe_spawn(now)
            self.update_obstacles()
            self.check_collisions()
            self.update_score(now)
            self.ramp_difficulty(now)

        self.root.after(TICK_MS, self.loop)

    def update_player(self):
        vx = 0
        if self.moving_left:
            vx -= PLAYER_SPEED
        if self.moving_right:
            vx += PLAYER_SPEED
        if vx == 0:
            return

        x1, y1, x2, y2 = self.canvas.coords(self.player)
        nx1 = max(0, x1 + vx)
        nx2 = min(WIDTH, x2 + vx)
        # prevent shrinking when clamped
        if nx1 <= 0 and vx < 0:
            vx = -x1
        elif nx2 >= WIDTH and vx > 0:
            vx = WIDTH - x2
        self.canvas.move(self.player, vx, 0)

    def maybe_spawn(self, now):
        if (now - self.last_spawn_time) * 1000 >= self.spawn_interval:
            self.spawn_obstacle()
            self.last_spawn_time = now

    def spawn_obstacle(self):
        w = random.randint(OB_MIN_W, OB_MAX_W)
        h = random.randint(OB_MIN_H, OB_MAX_H)
        x = random.randint(0, WIDTH - w)
        y = -h - 2
        vy = random.randint(OB_MIN_V, OB_MAX_V)
        color = random.choice(["#ff6b6b", "#ffd93d", "#6bff95", "#b195ff", "#ff9ecd"])
        oid = self.canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline="")
        self.obstacles.append({"id": oid, "vy": vy})

    def update_obstacles(self):
        to_remove = []
        for ob in self.obstacles:
            self.canvas.move(ob["id"], 0, ob["vy"])
            x1, y1, x2, y2 = self.canvas.coords(ob["id"])
            if y1 > HEIGHT:
                to_remove.append(ob)
        for ob in to_remove:
            self.canvas.delete(ob["id"])
            self.obstacles.remove(ob)

    def rects_overlap(self, a, b):
        ax1, ay1, ax2, ay2 = a
        bx1, by1, bx2, by2 = b
        return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

    def check_collisions(self):
        p = self.canvas.coords(self.player)
        for ob in self.obstacles:
            if self.rects_overlap(p, self.canvas.coords(ob["id"])):
                self.end_game()
                return

    def update_score(self, now):
        # Score based on survival time and dodged blocks
        self.score += 1
        self.score_var.set(f"Score: {self.score}")

    def ramp_difficulty(self, now):
        if (now - self.last_ramp) * 1000 >= DIFFICULTY_RAMP_MS:
            self.spawn_interval = max(SPAWN_INTERVAL_MIN, self.spawn_interval - SPAWN_STEP)
            self.last_ramp = now

    def end_game(self):
        self.game_over = True
        self.running = False
        self.status_var.set("Game Over — press R to restart")
        # Overlay
        self.overlay = self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#000000", stipple="gray25", outline="")
        self.canvas.tag_raise(self.overlay)
        msg = self.canvas.create_text(WIDTH//2, HEIGHT//2 - 10, text="GAME OVER", fill="#ffffff", font=("Segoe UI", 24, "bold"))
        sub = self.canvas.create_text(WIDTH//2, HEIGHT//2 + 24, text="Press R to Restart", fill="#d0d0d0", font=("Segoe UI", 12))
        self.canvas.tag_raise(msg)
        self.canvas.tag_raise(sub)

    def restart(self, _=None):
        if not self.game_over:
            return
        # Clear obstacles and overlay
        for ob in self.obstacles:
            self.canvas.delete(ob["id"])
        self.obstacles.clear()
        for item in self.canvas.find_all():
            # keep ground and player only
            pass
        
        
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, GROUND_Y, WIDTH, HEIGHT, fill="#1c1e23", outline="")
        
        self.player = self.canvas.create_rectangle(0, 0, PLAYER_W, PLAYER_H, fill="#62a5ff", outline="")
        self.canvas.move(self.player, WIDTH//2 - PLAYER_W//2, GROUND_Y - PLAYER_H - 3)

        
        self.moving_left = False
        self.moving_right = False
        self.score = 0
        self.score_var.set("Score: 0")
        self.status_var.set("← → move | P pause | R restart")
        self.game_over = False
        self.running = True
        self.last_spawn_time = time.time()
        self.spawn_interval = SPAWN_INTERVAL_START
        self.last_ramp = time.time()


def main():
    root = tk.Tk()
    Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()
