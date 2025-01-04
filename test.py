from fasthtml.common import *

app = FastHTML()

@app.get("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    serve(host="0.0.0.0", port=8000)
    