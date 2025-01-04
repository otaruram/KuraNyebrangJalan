from turtle import Turtle

# Posisi awal player
STARTING_POSITION = (0, -280)
# Jarak pergerakan player setiap kali tombol panah atas ditekan
MOVE_DISTANCE = 10
# Koordinat y garis finish
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        # Memanggil konstruktor kelas parent (Turtle)
        super().__init__()
        # Mengatur bentuk turtle menjadi gambar kura-kura
        self.shape("turtle")
        # Mengangkat pena agar tidak meninggalkan jejak saat bergerak
        self.penup()
        # Memindahkan player ke posisi awal
        self.go_to_start()
        # Mengatur arah hadap turtle ke atas (90 derajat)
        self.setheading(90)

    def go_up(self):
        # Menggerakkan turtle ke depan sejauh MOVE_DISTANCE
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Memindahkan turtle ke posisi awal yang didefinisikan di STARTING_POSITION
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Memeriksa apakah posisi y turtle sudah melewati garis finish
        if self.ycor() > FINISH_LINE_Y:
            # Jika sudah melewati, mengembalikan True
            return True
        else:
            # Jika belum melewati, mengembalikan False
            return False