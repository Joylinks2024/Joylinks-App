from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNELS_IDS = env.list("CHANNELS_IDS")

DJANGO_API = env.str("DJANGO_API")

loc_url = env.str("loc_url")

STIKER_ID = env.str("STIKER_ID")
