from turtle import Turtle

# Font yang akan digunakan untuk menampilkan skor
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        # Memanggil konstruktor kelas parent (Turtle)
        super().__init__()
        # Level awal game
        self.level = 1
        # Menyembunyikan turtle agar hanya teks yang ditampilkan
        self.hideturtle()
        # Mengangkat pena agar tidak meninggalkan jejak saat bergerak
        self.penup()
        # Memposisikan scoreboard di pojok kiri atas layar
        self.goto(-280, 250)
        # Menampilkan skor awal
        self.update_scoreboard()

    def update_scoreboard(self):
        # Membersihkan tampilan scoreboard sebelumnya
        self.clear()
        # Menulis teks "Level: {self.level}" di layar
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # Menaikkan level
        self.level += 1
        # Memperbarui tampilan scoreboard dengan level yang baru
        self.update_scoreboard()

    def game_over(self):
        # Memindahkan turtle ke tengah layar
        self.goto(0, 0)
        # Menulis teks "GAME OVER" di tengah layar
        self.write(f"GAME OVER", align="center", font=FONT)