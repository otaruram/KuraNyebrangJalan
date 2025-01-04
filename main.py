import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Inisialisasi layar
screen = Screen()
screen.setup(width=600, height=600)
# Mematikan animasi default agar pergerakan lebih halus dan dapat dikontrol dengan screen.update()
screen.tracer(0)

# Membuat objek player, car_manager, dan scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Mendengarkan input keyboard
screen.listen()
# Mengikat tombol panah atas dengan fungsi go_up pada objek player
screen.onkey(player.go_up, "Up")

# Variabel untuk mengontrol jalannya game
game_is_on = True

# Loop utama game
while game_is_on:
    # Memberikan jeda waktu agar game tidak berjalan terlalu cepat
    time.sleep(0.1)
    # Memperbarui tampilan layar setelah setiap iterasi loop
    screen.update()

    # Membuat mobil baru secara periodik
    car_manager.create_car()
    # Menggerakkan semua mobil yang ada
    car_manager.move_cars()

    # Mendeteksi tabrakan dengan mobil
    # Melakukan iterasi pada setiap mobil yang ada di car_manager
    for car in car_manager.all_cars:
        # Memeriksa jarak antara player dan mobil. Jika kurang dari 20, dianggap bertabrakan
        if car.distance(player) < 20:
            # Menghentikan game
            game_is_on = False
            # Menampilkan pesan game over di scoreboard
            scoreboard.game_over()

    # Mendeteksi keberhasilan menyeberang garis finish
    if player.is_at_finish_line():
        # Mengembalikan player ke posisi awal
        player.go_to_start()
        # Meningkatkan kecepatan mobil (level up)
        car_manager.level_up()
        # Meningkatkan level di scoreboard
        scoreboard.increase_level()

# Menutup window ketika diklik
screen.exitonclick()