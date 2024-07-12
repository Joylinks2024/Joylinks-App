from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import loc_url


async def afzaliklar():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="Davomi ➡", callback_data="davomi_1")
    return inline.add(inl_1)


async def afzaliklar_2():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga_1")
    inl_2 = InlineKeyboardButton(text="Davomi ➡", callback_data="davomi_2")
    return inline.row(inl_1, inl_2)


async def afzaliklar_3():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="⬅ Orqaga", callback_data="davomi_1")
    inl_2 = InlineKeyboardButton(text="Davomi ➡", callback_data="davomi_3")
    return inline.row(inl_1, inl_2)


async def afzaliklar_4():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="⬅ Orqaga", callback_data="davomi_2")
    inl_2 = InlineKeyboardButton(text="Davomi ➡", callback_data="davomi_4")
    return inline.row(inl_1, inl_2)


async def afzaliklar_5():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="⬅ Orqaga", callback_data="davomi_3")
    inl_2 = InlineKeyboardButton(text="Davomi ➡", callback_data="davomi_5")
    return inline.row(inl_1, inl_2)


async def afzaliklar_6():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="⬅ Orqaga", callback_data="davomi_4")
    inl_2 = InlineKeyboardButton(text="Davomi ➡", callback_data="davomi_6")
    return inline.row(inl_1, inl_2)


async def afzaliklar_7():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="⬅ Orqaga", callback_data="davomi_5")
    inl_2 = InlineKeyboardButton(text="✅ Ro'yxatdan o'tish", callback_data="royhatdan_otish_1")
    return inline.row(inl_1, inl_2)


async def kursga_yozilish(kurs_nomi: str):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="✅ Kursga Yozilish", callback_data=f"kurs|{kurs_nomi}")
    return inline.row(inl_1)


async def kursni_qabulqilish(order_id, tg_id):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="Qabul Qilish", callback_data=f"accept|{order_id}")
    inl_2 = InlineKeyboardButton(text="To'liq Ma'lumot 👨🏻‍💻", callback_data=f"info|{tg_id}")
    return inline.row(inl_1, inl_2)


async def kurs_qabulqilindi(tg_id):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="Korzinkaga Solindi ✅", callback_data=f"added_to_cart")
    inl_2 = InlineKeyboardButton(text="To'liq Ma'lumot 👨🏻‍💻", callback_data=f"info|{tg_id}")
    return inline.add(inl_1, inl_2)


async def user_get_super_admin(tg_id):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="To'liq Ma'lumot 👨🏻‍💻", callback_data=f"info|{tg_id}")
    inl_2 = InlineKeyboardButton(text="Admini Olib Tashlash", callback_data=f"rm_admin|{tg_id}")
    return inline.add(inl_1).add(inl_2)


async def user_get_info_1(tg_id):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="To'liq Ma'lumot 👨🏻‍💻", callback_data=f"info|{tg_id}")
    return inline.add(inl_1)


async def courses_taken(tg_id, order_id):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="To'liq Ma'lumot 👨🏻‍💻", callback_data=f"info|{tg_id}")
    inl_2 = InlineKeyboardButton(text="Korzinkaga Solish 🗑", callback_data=f"korzinka|{tg_id}|{order_id}")
    return inline.add(inl_1, inl_2)


async def user_get_info_2(order_id, tg_id):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="Qabul Qilish", callback_data=f"accept|{order_id}")
    inl_2 = InlineKeyboardButton(text="To'liq Ma'lumot 👨🏻‍💻", callback_data=f"info|{tg_id}")
    return inline.add(inl_1, inl_2)


async def send_google_location(url=loc_url):
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="Google Map 🗺", url=url)
    return inline.add(inl_1)


async def send_next_top_user(is_inl):
    if is_inl is True:
        inline = InlineKeyboardMarkup(row_width=True)
        inl_1 = InlineKeyboardButton(text="⬅", callback_data="back_top_users")
        inl_2 = InlineKeyboardButton(text="❌", callback_data="close_top_users")
        inl_3 = InlineKeyboardButton(text="➡", callback_data="next_top_users")
        return inline.row(inl_1, inl_2, inl_3)
    else:
        return None


async def send_next_top_user_2():
    inline = InlineKeyboardMarkup(row_width=True)
    inl_1 = InlineKeyboardButton(text="⬅", callback_data="back_top_users_2")
    inl_2 = InlineKeyboardButton(text="❌", callback_data="close_top_users")
    inl_3 = InlineKeyboardButton(text="➡", callback_data="next_top_users_2")
    return inline.row(inl_1, inl_2, inl_3)


async def create_check_sup_inl(title, invite_links):
    inline = InlineKeyboardMarkup(row_width=True)
    for name, invite_link in zip(title, invite_links):
        inl_1 = InlineKeyboardButton(text=name, url=invite_link)
        inline.add(inl_1)
    inl_2 = InlineKeyboardButton(text="Tasdiqlash", callback_data="check_subs")
    inline.add(inl_2)
    return inline
