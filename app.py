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
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --primary: #3498db;
            --secondary: #2ecc71;
            --dark: #2c3e50;
            --light: #ecf0f1;
            --accent: #e74c3c;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            background: linear-gradient(135deg, #0a192f 0%, #1a3a5f 100%);
            color: var(--light);
            font-family: 'Poppins', sans-serif;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
        }}
        
        h1 {{
            font-size: 2.8rem;
            font-weight: 700;
            background: linear-gradient(to right, var(--secondary), var(--primary));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            display: inline-block;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }}
        
        .subtitle {{
            font-size: 1.2rem;
            color: #bdc3c7;
            margin-bottom: 20px;
        }}
        
        .controls {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            background: rgba(255, 255, 255, 0.08);
            padding: 20px;
            border-radius: 15px;
            box-shadow: var(--shadow);
        }}
        
        .select-wrapper {{
            position: relative;
            flex: 1;
            min-width: 250px;
        }}
        
        .select-wrapper::after {{
            content: "▼";
            font-size: 0.8rem;
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            pointer-events: none;
            color: var(--primary);
        }}
        
        #razas {{
            width: 100%;
            padding: 12px 20px;
            border: none;
            border-radius: 50px;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 1rem;
            appearance: none;
            outline: none;
            cursor: pointer;
            transition: var(--transition);
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.15);
        }}
        
        #razas:hover {{
            background: rgba(255, 255, 255, 0.15);
        }}
        
        #razas option {{
            background: #2c3e50;
            color: white;
        }}
        
        #btn {{
            padding: 12px 30px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: var(--shadow);
        }}
        
        #btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }}
        
        #btn:active {{
            transform: translateY(0);
        }}
        
        .image-container {{
            display: flex;
            justify-content: center;
            margin-bottom: 30px;
        }}
        
        .image-wrapper {{
            width: 100%;
            max-width: 500px;
            height: 400px;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            position: relative;
            transition: var(--transition);
        }}
        
        .image-wrapper:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
        }}
        
        #imagen {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }}
        
        #imagen:hover {{
            transform: scale(1.02);
        }}
        
        .loader {{
            display: none;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 50px;
            height: 50px;
            border: 5px solid rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            border-top: 5px solid var(--primary);
            animation: spin 1s linear infinite;
        }}
        
        @keyframes spin {{
            0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
            100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
        }}
        
        .breed-name {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
            padding: 20px 15px 10px;
            color: white;
            font-weight: 600;
            text-align: center;
            text-transform: capitalize;
        }}
        
        footer {{
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            color: #95a5a6;
            font-size: 0.9rem;
        }}
        
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2.2rem;
            }}
            
            .controls {{
                flex-direction: column;
            }}
            
            .image-wrapper {{
                height: 300px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Galería De Perros</h1>
            <p class="subtitle">Descubre hermosas imágenes de perros por raza</p>
        </header>
        
        <div class="controls">
            <div class="select-wrapper">
                <select id="razas">
                    {opciones_html}
                </select>
            </div>
            <button id="btn">
                <i class="fas fa-paw"></i> Mostrar Perro
            </button>
        </div>
        
        <div class="image-container">
            <div class="image-wrapper">
                <div class="loader" id="loader"></div>
                <img id="imagen" src="{imagen_inicial}" alt="Imagen de perro"/>
                <div class="breed-name" id="breed-name">Random</div>
            </div>
        </div>
        
        <footer>
            <p>© 2023 Galería de Perros - Todas las imágenes son proporcionadas por Dog API</p>
        </footer>
    </div>

    <script>
        const btn = document.getElementById("btn");
        const img = document.getElementById("imagen");
        const loader = document.getElementById("loader");
        const breedName = document.getElementById("breed-name");
        const select = document.getElementById("razas");
        
        // Mostrar nombre de la raza inicial
        breedName.textContent = "Random";
        
        btn.addEventListener("click", () => {{
            const raza = select.value;
            // Mostrar loader
            loader.style.display = "block";
            img.style.opacity = "0.5";
            
            breedName.textContent = raza;
            
            fetch("https://dog.ceo/api/breed/" + raza + "/images/random")
                .then(res => res.json())
                .then(data => {{
                    img.src = data.message;
                    // Ocultar loader cuando la imagen se cargue
                    img.onload = function() {{
                        loader.style.display = "none";
                        img.style.opacity = "1";
                    }}
                }})
                .catch(error => {{
                    console.error("Error:", error);
                    loader.style.display = "none";
                    img.style.opacity = "1";
                }});
        }});
        
        // Mejorar la experiencia con la tecla Enter
        select.addEventListener("keyup", (event) => {{
            if (event.key === "Enter") {{
                btn.click();
            }}
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
