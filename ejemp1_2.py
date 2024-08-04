from fastapi import FastAPI

app = FastAPI()

@app.get("/saludar")
def saludar(nombre: str = "Munco"):
    return {"mensaje": f"Hola, {nombre}!"}