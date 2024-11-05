# Author : Pedro Seriang
# Email  : pedroseriangcorp@gmail.com

import pygame  # Mengimpor modul pygame
import time

# Inisialisasi pygame
pygame.init()

# Menentukan ukuran layar tampilan
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Definisi warna yang akan digunakan
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Pengaturan font dan ukuran teks
font_size = 30
font = pygame.font.Font(None, font_size)

# Daftar lirik yang akan ditampilkan secara bergantian
lyrics = [
    "You're just like an angel",
    "Your skin makes me cry",
    "You float like a feather",
    "In a beautiful world",
    "I wish I was special",
]

# Membuat clock untuk mengatur frame rate (FPS)
clock = pygame.time.Clock()

# Fungsi untuk menampilkan teks dengan efek fade in (muncul perlahan) dan fade out (menghilang perlahan)
def display_text(text, fade_in_duration=1, fade_out_duration=1):
    # Mulai dengan transparansi alpha 0 (tidak terlihat)
    alpha = 0
    # Render teks menjadi surface yang dapat ditampilkan di layar
    text_surface = font.render(text, True, GREEN)
    # Mendapatkan posisi teks di tengah layar
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))

    # Fade In (Muncul perlahan)
    for _ in range(fade_in_duration * 60):  # 60 FPS
        # Memeriksa jika pengguna menekan tombol "QUIT" untuk keluar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Meningkatkan nilai alpha untuk membuat teks lebih terlihat
        alpha += 255 / (fade_in_duration * 60)
        alpha = min(alpha, 255)  # Pastikan alpha tidak melebihi 255
        text_surface.set_alpha(alpha)  # Set transparansi pada teks
        screen.fill(BLACK)  # Mengisi layar dengan warna hitam
        screen.blit(text_surface, text_rect)  # Menampilkan teks di layar
        pygame.display.flip()  # Memperbarui tampilan layar
        clock.tick(60)  # Menunggu sesuai FPS

    # Menunggu sejenak agar teks dapat terlihat jelas sebelum menghilang
    pygame.time.wait(1000)

    # Fade Out (Menghilang perlahan)
    for _ in range(fade_out_duration * 60):  # 60 FPS
        # Memeriksa event untuk keluar dari aplikasi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Mengurangi nilai alpha untuk membuat teks semakin transparan
        alpha -= 255 / (fade_out_duration * 60)
        alpha = max(alpha, 0)  # Pastikan alpha tidak kurang dari 0
        text_surface.set_alpha(alpha)  # Set transparansi pada teks
        screen.fill(BLACK)  # Mengisi layar dengan warna hitam
        screen.blit(text_surface, text_rect)  # Menampilkan teks di layar
        pygame.display.flip()  # Memperbarui tampilan layar
        clock.tick(60)  # Menunggu sesuai FPS

# Fungsi utama untuk menampilkan setiap baris lirik dengan efek fade in dan fade out
def show_lyrics():
    running = True  # Menandakan program sedang berjalan
    for line in lyrics:  # Iterasi melalui setiap baris lirik
        if not running:  # Jika sudah tidak berjalan, keluar dari loop
            break
        for event in pygame.event.get():  # Mengecek event "QUIT" di awal setiap lirik
            if event.type == pygame.QUIT:
                running = False  # Menghentikan loop jika pengguna keluar
        
        # Menampilkan lirik dengan efek fade in dan fade out
        display_text(line)

    pygame.quit()  # Menutup jendela Pygame setelah loop selesai

# Menjalankan program jika file ini dieksekusi langsung
if __name__ == "__main__":
    show_lyrics()