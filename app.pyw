import tkinter as tk
#from func.exec import mp4_mp3, yt_ph_mp4, png_jpg, jpg_png, jpg_bmp, png_tiff, dec_bin, dec_hex, hash, hash_archivo, contra, cal, bin_dec
#############################################################################################
# FUNCTIONS
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
# WINDOWS
def vid_aud(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi Function App")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "mp4_mp3": tk.Button(app3, text="Convert", command=lambda: mp4_mp3(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "yt_mp4":  tk.Button(app3, text="Download", command=lambda: yt_ph_mp4(entry.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Go back", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi Function App"), app2.geometry("300x370"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="VIDEO and AUDIO", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="MP4 - MP3", command=lambda: valor("mp4_mp3"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="YT - MP4", command=lambda: valor("yt_mp4"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="Go back", command=lambda: cerrar(app2, app), **back_button).pack(pady=10, padx=10)
    app2.mainloop()
####
def img(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi Function App")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "png_jpg": tk.Button(app3, text="Convert", command=lambda: png_jpg(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "jpg_png": tk.Button(app3, text="Convert", command=lambda: jpg_png(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "jpg_bmp": tk.Button(app3, text="Convert", command=lambda: jpg_bmp(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "png_tiff": tk.Button(app3, text="Convert", command=lambda: png_tiff(entry.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Go back", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi Function App"), app2.geometry("300x440"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="IMAGES", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="PNG - JPEG", command=lambda: valor("png_jpg"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="JPG - PNG", command=lambda: valor("jpg_png"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="JPG - BMP", command=lambda: valor("jpg_bmp"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="PNG - TIFF", command=lambda: valor("png_tiff"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="Go back", command=lambda: cerrar(app2, app), **back_button).pack(pady=10, padx=10)
    app2.mainloop()
####
def calc(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi Function App")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "dec_bin": tk.Button(app3, text="Convert", command=lambda: dec_bin(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "bin_dec": tk.Button(app3, text="Convert", command=lambda: bin_dec(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "dec_hex": tk.Button(app3, text="Convert", command=lambda: dec_hex(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "hash": tk.Button(app3, text="Hashear", command=lambda: hash(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "hash_archivo": tk.Button(app3, text="Hashear (Ruta)", command=lambda: hash_archivo(entry.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Go back", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi Function App"), app2.geometry("300x520"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="CALC", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="DECIMAL - BINARY", command=lambda: valor("dec_bin"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="BINARY - DECIMAL", command=lambda: valor("bin_dec"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="DECIMAL - HEXADECIMAL", command=lambda: valor("dec_hex"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="HASH (VALUE)", command=lambda: valor("hash"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="HASH (FILE)", command=lambda: valor("hash_archivo"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="Go back", command=lambda: cerrar(app2, app), **back_button).pack(pady=10, padx=10)
    app2.mainloop()
####
def otr(app):
    def valor(i):
        app3 = tk.Tk(); app3.title("Multi Function App")
        entry = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10)
        if i == "contra": tk.Button(app3, text="Generate by lenght", command=lambda: contra(entry.get(), app3)).pack(pady=10, padx=10)
        if i == "cal":
            entry2 = tk.Entry(app3, width=40); entry.pack(pady=10, padx=10), entry2.pack(pady=10, padx=10)
            tk.Button(app3, text="Show (1: Year, 2: Month)", command=lambda: cal(entry.get(), entry2.get(), app3)).pack(pady=10, padx=10)
        tk.Button(app3, text="Go back", command=lambda: cerrar(app3, "y")).pack(pady=10, padx=10)
        app3.mainloop()
    
    app.withdraw(); app2 = tk.Toplevel(); centrar(app2)
    app2.title("Multi Function App"), app2.geometry("300x300"), app2.resizable(False, False), app2.configure(bg="#282C34"), app2.attributes("-alpha", 0.95)
    
    tk.Label(app2, text="OTHER FUNCTIONS", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
    tk.Button(app2, text="PASSWORD", command=lambda: valor("contra"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="CALENDAR", command=lambda: valor("cal"), **button_z).pack(pady=10, padx=10)
    tk.Button(app2, text="Go back", command=lambda: cerrar(app2, app), **back_button).pack(pady=10, padx=10)
    app2.mainloop()
#############################################################################################
# MAIN WINDOW
app = tk.Tk(); centrar(app)
app.title("Multi Function App"), app.geometry("300x410"), app.resizable(False, False), app.configure(bg="#282C34"), app.attributes("-alpha", 0.95)
button_z = {"bg": "#61AFEF", "fg": "#FFFFFF", "font": ("Helvetica", 14, "bold"), "relief": "flat", "bd": 0, "highlightthickness": 0, "width": 25, "height": 2}
back_button = {"bg": "#FF0000", "fg": "#FFFFFF", "font": ("Helvetica", 12, "bold"), "relief": "flat", "bd": 0, "highlightthickness": 0, "width": 18, "height": 2}

tk.Label(app, text="FUNCTIONS", font=("Helvetica", 20, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=20)
tk.Button(app, text="VIDEO, AUDIO", command=lambda: vid_aud(app), **button_z).pack(pady=10, padx=10)
tk.Button(app, text="IMAGES", command=lambda: img(app), **button_z).pack(pady=10, padx=10)
tk.Button(app, text="CALC", command=lambda: calc(app), **button_z).pack(pady=10, padx=10)
tk.Button(app, text="OTHER", command=lambda: otr(app), **button_z).pack(pady=10, padx=10)
tk.Label(app, text="byAd12.pages.dev", font=("Arial", 10, "bold"), bg="#282C34", fg="#ABB2BF").pack(pady=5)
app.mainloop()
#############################################################################################
# byAd12 (adgimenezp@gmail.com)
