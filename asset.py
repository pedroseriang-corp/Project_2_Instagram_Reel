# Author : Pedro Seriang
# Email  : pedroseriangcorp@gmail.com

import pygame
import time

# Inisialisasi Pygame
pygame.init()

# Ubah ukuran layar dan pengaturan tampilan itu disini
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Instagram @Pedro_Seriang')

# Untuk definisi warna background dan teks itu disini ubahnya 
black = (0, 0, 0)
white = (255, 255, 255)

# Pengaturan font dan ukuran
font_size = 25
font = pygame.font.SysFont('Arial', font_size)

# Fungsi untuk menampilkan teks dengan efek "mengetik"
def display_text(text, delay=50):
    screen.fill(black)  # Membersihkan layar dengan warna hitam
    x, y = 10, 10       # Posisi awal teks
    for i in range(len(text) + 1):
        # Menangani event untuk keluar dari program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        # Menampilkan teks satu per satu
        rendered_text = font.render(text[:i], True, white)
        screen.fill(black)
        screen.blit(rendered_text, (x, y))
        pygame.display.flip()
        pygame.time.delay(delay)
    
    # Memberi jeda setelah teks selesai ditampilkan
    pygame.time.delay(2000)

# Fungsi utama yang menampilkan daftar pesan secara bergantian
def main():
    running = True
    messages = [
        # Tambahkan kata-kata baru kamu di sini maksud saya lirik lebih tepatnya
        "You're just like an angel",
        "Your skin makes me cry",
        "You float like a feather",
        "In a beautiful world",
        "I wish I was special",
    ]
    
    # Bagian ini fungsinya menampilkan setiap pesan dalam messages dengan efek "mengetik"
    for message in messages:
        # Menangani event keluar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        display_text(message)  # Tampilkan pesan dengan efek mengetik
    
    # Menutup Pygame
    pygame.quit()

# Menjalankan fungsi utama jika skrip dijalankan secara langsung
if __name__ == '__main__':
    main()
