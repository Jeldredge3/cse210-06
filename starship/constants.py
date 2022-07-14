from game.shared.color import Color

# ===== Game Settings ===== #
FRAME_RATE = 15
COLUMNS = 60
ROWS = 30
CELL_SIZE = 30
FONT_SIZE = 30
MAX_X = 1280
MAX_Y = 960

CAPTION = "STARSHIP"
START_HITPOINTS = 200
RESPAWN_HITPOINTS = 200
MAX_HITPOINTS = 600
START_LIVES = 3
MAX_LIVES = 6
MAX_UPGRADES = 2
PLAYER_Y_LIMIT = MAX_Y
RATE_OF_FIRE = 1.00
MAX_BULLETS = 50
MAX_BULLET_DISTANCE = 30

SHOW_UPDATES_IN_TERMINAL = False
SHOW_CONSOLE_LOG = True
ALLOW_CHEATS = True

# ===== Colors ===== #
WHITE = Color(255, 255, 255)
GRAY = Color(131,139,139)
BLACK = Color(30,30,30)

RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0,0,255)

ORANGE = Color(255,128,0)
PURPLE = Color(125,38,205)
LIME = Color(192,255,62)
PINK = Color(255,105,180)
BROWN = Color(160,82,45)
CYAN = Color(0,245,255)
TEAL = Color(0,128,128)

BRONZE = Color(255,160,122)
SILVER = Color(238,233,233)
GOLD = Color(255,193,37)

FIRE0 = Color(255,165,0)
FIRE1 = Color(255,140,0)
FIRE2 = Color(255,69,0)
FIRE3 = Color(205,38,38)