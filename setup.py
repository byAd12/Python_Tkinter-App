from cx_Freeze import setup, Executable

ejecutable = Executable(script="app.pyw", base=None)
setup(name="Multi_App", version="1.0", description="Aplicación con múltiples funciones", author="byAd12",
    options={"build_exe": {"include_files": ["func/"]}},
    executables=[ejecutable]
)