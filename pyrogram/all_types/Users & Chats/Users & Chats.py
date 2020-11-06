#class pyrogram.types.User
#https://docs.pyrogram.org/api/types/User#pyrogram.types.User

message.from_user.id                  # (int) - Уникальный идентификатор этого пользователя или бота.
message.from_user.is_self             # (bool, необязательно ) - Истина, если этим пользователем являетесь вы сами.
message.from_user.is_contact          # (bool, необязательно ) - Истина, если этот пользователь находится в ваших контактах.
message.from_user.is_mutual_contact   # (bool, необязательно ) - Истина, если у вас обоих есть контакт друг с другом.
message.from_user.is_deleted          # (bool, необязательно ) - Истина, если этот пользователь удален.
message.from_user.is_bot              # (bool, необязательно ) - Истина, если этот пользователь является ботом.
message.from_user.is_verified         # (bool, необязательно ) - Истина, если этот пользователь был проверен Telegram.
message.from_user.is_restricted       # (bool, необязательно ) - Истина, если этот пользователь был ограничен. Только боты. Подробную информацию см. В разделе constration_reason .
message.from_user.is_scam             # (bool, необязательно ) - Истина, если этот пользователь был отмечен как мошенник.
message.from_user.is_support          # (bool, необязательно ) - Истина, если этот пользователь входит в группу поддержки Telegram.
message.from_user.first_name          # (str, необязательно ) - имя пользователя или бота.
message.from_user.last_name           # (str, необязательно ) - фамилия пользователя или бота.
message.from_user.status              # (str, необязательно ) - последнее посещение и статус пользователя в сети. Может быть одним из следующих: « онлайн », пользователь сейчас в сети. « Offline », пользователь сейчас не в сети. « Недавно », пользователь со скрытым временем последнего посещения, который был в сети от 1 секунды до 2–3 дней назад. « Within_week », пользователь со скрытым временем последнего посещения , который был в сети 2-3–7 дней назад. « Within_month », пользователь со скрытым временем последнего посещения , который был в сети от 6-7 дней до месяца назад. « Long_time_ago », заблокированный пользователь или пользователь со скрытым временем последнего посещения , который был в сети более месяца назад. Нет , для ботов.
message.from_user.last_online_date    # (int, необязательно ) - Дата последнего подключения пользователя к сети. Доступно только в случае статуса « офлайн »
message.from_user.next_offline_date   # (int, необязательно ) - Дата, когда пользователь автоматически перейдет в автономный режим. Доступно только в случае статуса « онлайн ».
message.from_user.username            # (str, необязательно ) - Имя пользователя или бота.
message.from_user.language_code       # (str, необязательно ) - языковой тег IETF языка пользователя
message.from_user.dc_id               # (int, необязательно ) - DC, назначенный пользователю или боту (дата-центр). Доступно только в том случае, если пользователь установил публичную фотографию профиля. Обратите внимание, что эта информация является приблизительной; он основан на том, где Telegram хранит изображения профиля пользователя, и никоим образом не сообщает вам местоположение пользователя (т. е. пользователь может уехать далеко, но все равно будет подключаться к назначенному ему DC). Больше информации в FAQ .
message.from_user.phone_number        # (str, необязательно ) - номер телефона пользователя
message.from_user.photo               # (ChatPhoto, необязательно ) - текущая фотография профиля пользователя или бота. Подходит только для скачивания.
message.from_user.restrictions        # (List of Restriction, необязательно ) - список причин, по которым этот бот может быть недоступен для некоторых пользователей. Это поле доступно только в том случае, если is_restricted имеет значение True.
message.from_user.mention             # (str, property) – создать текстовое упоминание для этого пользователя. Вы можете использовать, user.mention()чтобы упомянуть пользователя, используя его имя (стилизованное с использованием html) или другое имя. Чтобы выбрать другой стиль («html» или «md» / «уценка»), используйте .user.mention("another name")user.mention(style="md")