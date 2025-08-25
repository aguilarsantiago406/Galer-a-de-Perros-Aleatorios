import urllib.request
import json

# Lista de razas
razas = [
    "affenpinscher","african","airedale","akita","appenzeller","australian",
    "bakharwal","basenji","beagle","bluetick","borzoi","bouvier","boxer",
    "brabancon","briard","buhund","bulldog","bullterrier","cattledog",
    "cavapoo","chihuahua","chippiparai","chow","clumber","cockapoo",
    "collie","coonhound","corgi","cotondetulear","dachshund","dalmatian",
    "dane","danish","deerhound","dhole","dingo","doberman","elkhound",
    "entlebucher","eskimo","finnish","frise","gaddi","germanshepherd",
    "greyhound","groenendael","havanese","hound","husky","keeshond",
    "kelpie","kombai","komondor","kuvasz","labradoodle","labrador",
    "leonberg","lhasa","malamute","malinois","maltese","mastiff",
    "mexicanhairless","mix","mountain","mudhol","newfoundland","otterhound",
    "ovcharka","papillon","pariah","pekinese","pembroke","pinscher",
    "pitbull","pointer","pomeranian","poodle","pug","puggle","pyrenees",
    "rajapalayam","redbone","retriever","ridgeback","rottweiler","saluki",
    "samoyed","schipperke","schnauzer","segugio","setter","sharpei",
    "sheepdog","shiba","shihtzu","spaniel","spitz","springer","stbernard",
    "terrier","tervuren","vizsla","waterdog","weimaraner","whippet","wolfhound"
]

def obtener_perro():
    url = "https://dog.ceo/api/breeds/image/random"
    with urllib.request.urlopen(url) as respuesta:
        data = json.loads(respuesta.read().decode())
        return data["message"]

# Genera el HTML completo
def generar_html(ruta_html):
    imagen_inicial = obtener_perro()
    opciones_html = "\n".join([f'<option value="{r}">{r.capitalize()}</option>' for r in razas])
    
    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galería De Perros</title>
    <style>
        body{{background-color: rgb(0, 13, 41);}}
        header {{width: 100%; text-align: center;}}
        h1 {{font-family: "Lucida Sans", sans-serif; font-weight: bold; color: rgb(0,182,122);}}
        button {{width: 200px; height: 40px; border: none; border-radius: 50px; cursor: pointer;}}
        .button {{display: flex; justify-content: center;}}
        .containerImage{{width: 400px; height: 400px; margin: auto;}}
        img{{width: 100%; height: 100%;}}
    </style>
</head>
<body>
    <header>
        <h1>Galería De Perros</h1>
    </header>

    <div class="button">
        <select id="razas">
            {opciones_html}
        </select>
    </div>

    <div class="button">
        <button id="btn">Mostrar Perro</button>
    </div>

    <div class="containerImage">
        <img id="imagen" src="{imagen_inicial}" alt="Imagen de perro"/>
    </div>

    <script>
        const btn = document.getElementById("btn");
        const img = document.getElementById("imagen");

        btn.addEventListener("click", () => {{
            const raza = document.getElementById("razas").value;
            fetch("https://dog.ceo/api/breed/" + raza + "/images/random")
                .then(res => res.json())
                .then(data => {{
                    img.src = data.message;
                }})
                .catch(error => console.error("Error:", error));
        }});
    </script>
</body>
</html>
"""
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ HTML generado en '{ruta_html}'")

if __name__ == "__main__":
    generar_html("index.html")
