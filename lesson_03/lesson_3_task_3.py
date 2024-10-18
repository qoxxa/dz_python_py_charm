from address import Address
from mailing import Mailing

mailing = Mailing(Address(107061, "Москва", "ул. Б. Черкизовская", 5, 10),
                  Address(195298, "Санкт-Петербург", "ул. Белорусская", 4, 15), '1000 рублей', 1308)

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost}")