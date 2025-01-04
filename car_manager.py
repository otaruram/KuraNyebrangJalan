from turtle import Turtle
import random

# Daftar warna yang akan digunakan untuk mobil
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Jarak awal pergerakan mobil
STARTING_MOVE_DISTANCE = 5
# Increment (penambahan) kecepatan mobil setiap level naik
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        # List untuk menyimpan semua objek mobil
        self.all_cars = []
        # Kecepatan awal mobil
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Memberikan peluang 1/6 untuk membuat mobil baru di setiap iterasi
        random_chance = random.randint(1, 6)
        # Jika angka random adalah 1, maka buat mobil baru
        if random_chance == 1:
            # Membuat objek Turtle baru untuk mobil
            new_car = Turtle("square")
            # Mengatur ukuran mobil (memanjang horizontal)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # Mengangkat pena agar tidak meninggalkan jejak saat bergerak
            new_car.penup()
            # Memberikan warna acak dari daftar COLORS
            new_car.color(random.choice(COLORS))
            # Menentukan posisi y secara acak di layar
            random_y = random.randint(-250, 250)
            # Memposisikan mobil di sisi kanan layar (x=300) dengan y yang random
            new_car.goto(300, random_y)
            # Menambahkan mobil baru ke dalam list all_cars
            self.all_cars.append(new_car)

    def move_cars(self):
        # Menggerakkan setiap mobil yang ada dalam list all_cars
        for car in self.all_cars:
            # Menggerakkan mobil ke belakang (ke kiri) sesuai dengan kecepatan car_speed
            car.backward(self.car_speed)

    def level_up(self):
        # Meningkatkan kecepatan mobil dengan menambahkan MOVE_INCREMENT
        self.car_speed += MOVE_INCREMENT