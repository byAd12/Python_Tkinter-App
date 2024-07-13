import subprocess
######################################################################################################
def mp4_mp3(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/vid_aud.py" func1 {i}', shell=True), app3.destroy()

def yt_ph_mp4(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/vid_aud.py" func2 {i}', shell=True), app3.destroy()
######################################################################################################
def png_jpg(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/img.py" func1 {i}', shell=True), app3.destroy()

def jpg_png(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/img.py" func2 {i}', shell=True), app3.destroy()

def jpg_bmp(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/img.py" func3 {i}', shell=True), app3.destroy()

def png_tiff(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/img.py" func4 {i}', shell=True), app3.destroy()
##################################################################################################
def dec_bin(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/calc.py" func1 {i}', shell=True), app3.destroy()

def dec_hex(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/calc.py" func2 {i}', shell=True), app3.destroy()

def hash(i, app3): # POR VALOR
    subprocess.Popen(f'start cmd /K python "./func/calc.py" func3 {i}', shell=True), app3.destroy()

def hash_archivo(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/calc.py" func4 {i}', shell=True), app3.destroy()

def bin_dec(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/calc.py" func5 {i}', shell=True), app3.destroy()
###################################################################################################
def contra(i, app3):
    subprocess.Popen(f'start cmd /K python "./func/otr.py" func1 {i}', shell=True), app3.destroy()

def cal(i, y, app3):
    subprocess.Popen(f'start cmd /K python "./func/otr.py" func2 {i} {y}', shell=True), app3.destroy()
######################################################################################################