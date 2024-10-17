from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", 'Galaxy A55', '+79994002020'),
    Smartphone("Honor", 'Magic V3', '+79152001010'),
    Smartphone("Xiaomi", '13T Pro','+79010010101'),
    Smartphone("Apple", 'iPhone 15', '+79801130808'),
    Smartphone("Huawei", 'nova 11 Pro', '+79814558716')
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")