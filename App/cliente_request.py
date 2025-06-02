import requests

BASE_URL = "http://localhost:5000/"

def get_root():
    # Llamada GET al endpoint "/"
    resp = requests.get(f"{BASE_URL}/")
    resp.raise_for_status()                # Lanza excepción si el status ≠ 2xx
    return resp.json()                    # Devuelve: {"message": "¡Hola, mundo!"}

def get_item(item_id: int, q: str | None = None):
    # Llamada GET al endpoint "/items/{item_id}?q=..."
    params = {}
    if q is not None:
        params["q"] = q
    resp = requests.get(f"{BASE_URL}/items/{item_id}", params=params)
    resp.raise_for_status()
    return resp.json()  # Devuelve: {"item_id": 5, "q": "valor_de_q"} por ejemplo

def create_item(item_payload: dict):
    # Ejemplo de POST (si hubieras definido un POST en FastAPI)
    resp = requests.post(f"{BASE_URL}/items/", json=item_payload)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    # Ejecución de ejemplo
    print(get_root())                 # -> {'message': '¡Hola, mundo!'}
    print(get_item(42, q="ejemplo"))  # -> {'item_id': 42, 'q': 'ejemplo'}
