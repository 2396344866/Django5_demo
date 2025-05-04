#### 1. 启动 Django shell
```bash
python manage.py shell
```

#### 2. 启动 Django shell
```bash
from phone.models import Phone
import random
phones_info = [
    {
        "name": "iPhone 15 Pro",
        "brand": "Apple",
        "price": 8999.00,
        "processor": "A16 Bionic",
        "camera_mp": 48,
        "battery_capacity": 3274,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "Galaxy S23 Ultra",
        "brand": "Samsung",
        "price": 9699.00,
        "processor": "Snapdragon 8 Gen 2",
        "camera_mp": 200,
        "battery_capacity": 5000,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "Vivo S4",
        "brand": "Vivo",
        "price": 5861.03,
        "processor": "A15 Bionic",
        "camera_mp": 135,
        "battery_capacity": 4660,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "Xiaomi 11",
        "brand": "Xiaomi",
        "price": 4175.38,
        "processor": "Kirin 9000",
        "camera_mp": 38,
        "battery_capacity": 4358,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "Vivo 1",
        "brand": "Vivo",
        "price": 4137.07,
        "processor": "Snapdragon 7 Gen 1",
        "camera_mp": 157,
        "battery_capacity": 4520,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "OnePlus Ace1",
        "brand": "OnePlus",
        "price": 5940.10,
        "processor": "Snapdragon 7 Gen 1",
        "camera_mp": 33,
        "battery_capacity": 4426,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "OPPO 6",
        "brand": "OPPO",
        "price": 2963.74,
        "processor": "Tensor G2",
        "camera_mp": 199,
        "battery_capacity": 5618,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "Xiaomi 13",
        "brand": "Xiaomi",
        "price": 3703.96,
        "processor": "A14 Bionic",
        "camera_mp": 186,
        "battery_capacity": 5357,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "Xiaomi 12",
        "brand": "Xiaomi",
        "price": 3185.83,
        "processor": "Snapdragon 8 Gen 2",
        "camera_mp": 99,
        "battery_capacity": 4614,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    },
    {
        "name": "Huawei 57",
        "brand": "Huawei",
        "price": 3875.24,
        "processor": "Snapdragon 8 Gen 2",
        "camera_mp": 173,
        "battery_capacity": 5342,
        "performance": random.randint(6, 9),
        "appearance": random.randint(6, 9),
        "user_demand": random.randint(6, 9),
        "age_group": random.choice(["18 - 25", "25 - 35", "35 - 45"]),
        "gender": random.choice(["male", "female", "unisex"])
    }
]
for phone in phones_info:
    try:
        Phone.objects.create(
            name=phone["name"],
            brand=phone["brand"],
            price=phone["price"],
            processor=phone["processor"],
            camera_mp=phone["camera_mp"],
            battery_capacity=phone["battery_capacity"],
            performance=phone["performance"],
            appearance=phone["appearance"],
            user_demand=phone["user_demand"],
            age_group=phone["age_group"],
            gender=phone["gender"]
        )
    except Exception as e:
        print(f"创建记录 {phone['name']} 时出错: {e}")
        import traceback
        traceback.print_exc()


**iPhone 15 Pro**：价格 $8999.00，处理器 A16 Bionic，摄像头像素 48MP，电池容量 3274mAh。 
**Galaxy S23 Ultra**：价格 $9699.00，处理器 Snapdragon 8 Gen 2，摄像头像素 200MP，电池容量 5000mAh。  
**Vivo S4**：价格 $5861.03，处理器 A15 Bionic，摄像头像素 135MP，电池容量 4660mAh。
**Xiaomi 11**：价格 $4175.38，处理器 Kirin 9000，摄像头像素 38MP，电池容量 4358mAh。
**Vivo 1**：价格 $4137.07，处理器 Snapdragon 7 Gen 1，摄像头像素 157MP，电池容量 4520mAh。  
**OnePlus Ace1**：价格 $5940.10，处理器 Snapdragon 7 Gen 1，摄像头像素 33MP，电池容量 4426mAh。  
**OPPO 6**：价格 $2963.74，处理器 Tensor G2，摄像头像素 199MP，电池容量 5618mAh。  
**Xiaomi 13**：价格 $3703.96，处理器 A14 Bionic，摄像头像素 186MP，电池容量 5357mAh。   
**Xiaomi 12**：价格 $3185.83，处理器 Snapdragon 8 Gen 2，摄像头像素 99MP，电池容量 4614mAh。 
**Huawei 57**：价格 $3875.24，处理器 Snapdragon 8 Gen 2，摄像头像素 173MP，电池容量 5342mAh。  
```



#### 3. 在 python manage.py shell 中运行的代码
```bash
from phone.models import Phone
import random
brands = ["Apple", "Samsung", "Xiaomi", "Huawei", "OPPO", "Vivo", "OnePlus", "Google"]
apple_suffixes = ["SE", "XR", "Plus"]
samsung_suffixes = ["FE", "Lite", "Ultra"]
xiaomi_suffixes = ["Pro", "Ultra", "Lite"]
huawei_suffixes = ["Mate", "P", "Nova"]
oppo_suffixes = ["Find X", "Reno"]
vivo_suffixes = ["X", "S"]
oneplus_suffixes = ["Nord", "Ace"]
google_suffixes = ["Pixel"]
processors = [
    "A15 Bionic", "A14 Bionic", "Snapdragon 8 Gen 2", "Snapdragon 7 Gen 1", "Snapdragon 6 Gen 1",
    "Dimensity 9000", "Dimensity 8100", "Kirin 9000", "Tensor G2"
]
genders = ["male", "female", "unisex"]
num_records = 2000
for i in range(num_records):
    brand = random.choice(brands)
    if brand == "Apple":
        suffix = random.choice(apple_suffixes) if random.random() < 0.3 else ""
        name = f"iPhone {random.randint(11, 15)} {suffix}".strip()
    elif brand == "Samsung":
        suffix = random.choice(samsung_suffixes) if random.random() < 0.3 else ""
        name = f"Galaxy S{random.randint(21, 23)} {suffix}".strip()
    elif brand == "Xiaomi":
        suffix = random.choice(xiaomi_suffixes) if random.random() < 0.3 else ""
        name = f"Xiaomi {random.randint(11, 13)} {suffix}".strip()
    elif brand == "Huawei":
        suffix = random.choice(huawei_suffixes) if random.random() < 0.3 else ""
        name = f"Huawei {suffix} {random.randint(50, 60)}".strip()
    elif brand == "OPPO":
        suffix = random.choice(oppo_suffixes) if random.random() < 0.3 else ""
        name = f"OPPO {suffix} {random.randint(1, 10)}".strip()
    elif brand == "Vivo":
        suffix = random.choice(vivo_suffixes) if random.random() < 0.3 else ""
        name = f"Vivo {suffix} {random.randint(1, 10)}".strip()
    elif brand == "OnePlus":
        suffix = random.choice(oneplus_suffixes) if random.random() < 0.3 else ""
        name = f"OnePlus {suffix} {random.randint(1, 3)}".strip()
    elif brand == "Google":
        suffix = random.choice(google_suffixes) if random.random() < 0.3 else ""
        name = f"Google {suffix} {random.randint(6, 8)}".strip()
    price = round(random.uniform(2000, 6000), 2)
    processor = random.choice(processors)
    camera_mp = random.randint(12, 200)
    battery_capacity = random.randint(4000, 6000)
    performance = random.randint(6, 9)
    appearance = random.randint(6, 9)
    user_demand = random.randint(6, 9)
    age_group = random.choice(["18-25", "25-35", "35-45"])
    gender = random.choice(genders)
    try:
        Phone.objects.create(
            name=name,
            brand=brand,
            price=price,
            processor=processor,
            camera_mp=camera_mp,
            battery_capacity=battery_capacity,
            performance=performance,
            appearance=appearance,
            user_demand=user_demand,
            age_group=age_group,
            gender=gender
        )
    except Exception as e:
        print(f"创建记录 {name} 时出错: {e}")
        import traceback
        traceback.print_exc()
print(f"成功创建 {num_records} 条手机数据")
```