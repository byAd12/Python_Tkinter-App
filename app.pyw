import tkinter as tk
from func.exec import mp4_mp3, yt_ph_mp4, png_jpg, jpg_png, jpg_bmp, png_tiff, dec_bin, dec_hex, hash, hash_archivo, contra, cal, bin_dec
#############################################################################################
# FUNCIONES DE LAS VENTANAS
def cerrar(secondary_window, main_window):
    secondary_window.destroy()
    main_window.deiconify() if main_window != "y" else print("y")

def centrar(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = 10
    window.geometry(f"+{x}+{y}")
#############################################################################################
# VENTANAS
def vid_aud(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi funciones")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "mp4_mp3": tk.Button(app3, text="Convertir", command=lambda: mp4_mp3(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "yt_mp4":  tk.Button(app3, text="Descargar", command=lambda: yt_ph_mp4(entry.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Volver", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi funciones"), app2.geometry("300x370"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="VÍDEO Y AUDIO", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="MP4 a MP3", command=lambda: valor("mp4_mp3"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="YT a MP4", command=lambda: valor("yt_mp4"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="Volver", command=lambda: cerrar(app2, app), **botón_volver).pack(pady=10, padx=10)
    app2.mainloop()
####
def img(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi funciones")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "png_jpg": tk.Button(app3, text="Convertir", command=lambda: png_jpg(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "jpg_png": tk.Button(app3, text="Convertir", command=lambda: jpg_png(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "jpg_bmp": tk.Button(app3, text="Convertir", command=lambda: jpg_bmp(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "png_tiff": tk.Button(app3, text="Convertir", command=lambda: png_tiff(entry.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Volver", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi funciones"), app2.geometry("300x440"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="IMÁGENES", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="PNG a JPEG", command=lambda: valor("png_jpg"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="JPG a PNG", command=lambda: valor("jpg_png"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="JPG a BMP", command=lambda: valor("jpg_bmp"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="PNG a TIFF", command=lambda: valor("png_tiff"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="Volver", command=lambda: cerrar(app2, app), **botón_volver).pack(pady=10, padx=10)
    app2.mainloop()
####
def calc(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi funciones")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "dec_bin": tk.Button(app3, text="Convertir", command=lambda: dec_bin(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "bin_dec": tk.Button(app3, text="Convertir", command=lambda: bin_dec(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "dec_hex": tk.Button(app3, text="Convertir", command=lambda: dec_hex(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "hash": tk.Button(app3, text="Hashear", command=lambda: hash(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "hash_archivo": tk.Button(app3, text="Hashear (Ruta)", command=lambda: hash_archivo(entry.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Volver", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi funciones"), app2.geometry("300x520"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="CÁLCULOS", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="DECIMAL a BINARIO", command=lambda: valor("dec_bin"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="BINARIO a DECIMAL", command=lambda: valor("bin_dec"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="DECIMAL a HEXADECIMAL", command=lambda: valor("dec_hex"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="HASH (VALOR)", command=lambda: valor("hash"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="HASH (ARCHIVO)", command=lambda: valor("hash_archivo"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="Volver", command=lambda: cerrar(app2, app), **botón_volver).pack(pady=10, padx=10)
    app2.mainloop()
####
def otr(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi funciones")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "contra": tk.Button(app3, text="Generar por longitud", command=lambda: contra(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "cal":
            entry2 = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10), entry2.pack(pady=10, padx=10)
            tk.Button(app3, text="Mostrar (1: Año, 2: Mes)", command=lambda: cal(entry.get(), entry2.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Volver", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi funciones"), app2.geometry("300x300"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="OTRAS FUNCIONES", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="CONTRASEÑA", command=lambda: valor("contra"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="CALENDARIO", command=lambda: valor("cal"), **botón1).pack(pady=10, padx=10)
    tk.Button(app2, text="Volver", command=lambda: cerrar(app2, app), **botón_volver).pack(pady=10, padx=10)
    app2.mainloop()
#############################################################################################
# VENTANA PRINCIPAL
app = tk.Tk(); centrar(app)
app.title("Multi funciones"), app.geometry("300x410"), app.resizable(False, False), app.configure(bg="#282C34"), app.attributes("-alpha", 0.95)
botón1 = {"bg": "#61AFEF", "fg": "#FFFFFF", "font": ("Helvetica", 14, "bold"), "relief": "flat", "bd": 0, "highlightthickness": 0, "width": 25, "height": 2}
botón_volver = {"bg": "#FF0000", "fg": "#FFFFFF", "font": ("Helvetica", 12, "bold"), "relief": "flat", "bd": 0, "highlightthickness": 0, "width": 18, "height": 2}

tk.Label(app, text="FUNCIONES", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
tk.Button(app, text="VÍDEO Y AUDIO", command=lambda: vid_aud(app), **botón1).pack(pady=10, padx=10)
tk.Button(app, text="IMÁGENES", command=lambda: img(app), **botón1).pack(pady=10, padx=10)
tk.Button(app, text="CÁLCULOS", command=lambda: calc(app), **botón1).pack(pady=10, padx=10)
tk.Button(app, text="OTRAS", command=lambda: otr(app), **botón1).pack(pady=10, padx=10)
tk.Label(app, text="byAd12.pages.dev", font=("Arial", 10, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=5)
app.mainloop()
#############################################################################################
# Hecho por byAd12 (adgimenezp@gmail.com)
