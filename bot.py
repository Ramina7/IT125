import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

API_TOKEN = "8566240485:AAHrbviiOwfj609S7h-nzxbgT1C5CsYDv8c"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

orders = {}
order_id = 1


class OrderFSM(StatesGroup):
    name = State()
    product = State()
    time = State()
    delete_id = State()
    edit_id = State()
    edit_name = State()
    edit_product = State()
    edit_time = State()


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить заказ")],
        [KeyboardButton(text="📖 Посмотреть заказы")],
        [KeyboardButton(text="✏️ Изменить заказ")],
        [KeyboardButton(text="❌ Удалить заказ")]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Используй команду /basket")


@dp.message(Command("basket"))
async def basket(message: Message):
    await message.answer("Меню заказов:", reply_markup=keyboard)


@dp.message(F.text == "➕ Добавить заказ")
async def add_order(message: Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(OrderFSM.name)


@dp.message(OrderFSM.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Что вы хотите заказать?")
    await state.set_state(OrderFSM.product)


@dp.message(OrderFSM.product)
async def get_product(message: Message, state: FSMContext):
    await state.update_data(product=message.text)
    await message.answer("К какому времени доставить заказ?")
    await state.set_state(OrderFSM.time)


@dp.message(OrderFSM.time)
async def get_time(message: Message, state: FSMContext):
    global order_id
    data = await state.get_data()

    orders[order_id] = {
        "name": data["name"],
        "product": data["product"],
        "time": message.text
    }

    await message.answer(
        f"Заказ добавлен\n"
        f"ID: {order_id}\n"
        f"Имя: {data['name']}\n"
        f"Заказ: {data['product']}\n"
        f"Время: {message.text}"
    )

    order_id += 1
    await state.clear()


@dp.message(F.text == "📖 Посмотреть заказы")
async def view_orders(message: Message):
    if not orders:
        await message.answer("Заказов нет")
        return

    text = "Все заказы:\n\n"
    for oid, order in orders.items():
        text += (
            f"ID: {oid}\n"
            f"Имя: {order['name']}\n"
            f"Заказ: {order['product']}\n"
            f"Время: {order['time']}\n\n"
        )

    await message.answer(text)


@dp.message(F.text == "❌ Удалить заказ")
async def delete_order(message: Message, state: FSMContext):
    await message.answer("Введите ID заказа")
    await state.set_state(OrderFSM.delete_id)


@dp.message(OrderFSM.delete_id)
async def confirm_delete(message: Message, state: FSMContext):
    oid = int(message.text)

    if oid in orders:
        del orders[oid]
        await message.answer("Заказ удалён")
    else:
        await message.answer("Заказ не найден")

    await state.clear()


@dp.message(F.text == "✏️ Изменить заказ")
async def edit_order(message: Message, state: FSMContext):
    await message.answer("Введите ID заказа")
    await state.set_state(OrderFSM.edit_id)


@dp.message(OrderFSM.edit_id)
async def edit_get_id(message: Message, state: FSMContext):
    oid = int(message.text)

    if oid not in orders:
        await message.answer("Заказ не найден")
        await state.clear()
        return

    await state.update_data(edit_id=oid)
    await message.answer("Введите новое имя")
    await state.set_state(OrderFSM.edit_name)


@dp.message(OrderFSM.edit_name)
async def edit_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите новый заказ")
    await state.set_state(OrderFSM.edit_product)


@dp.message(OrderFSM.edit_product)
async def edit_product(message: Message, state: FSMContext):
    await state.update_data(product=message.text)
    await message.answer("Введите новое время")
    await state.set_state(OrderFSM.edit_time)


@dp.message(OrderFSM.edit_time)
async def edit_time(message: Message, state: FSMContext):
    data = await state.get_data()
    orders[data["edit_id"]] = {
        "name": data["name"],
        "product": data["product"],
        "time": message.text
    }

    await message.answer("Заказ обновлён")
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
