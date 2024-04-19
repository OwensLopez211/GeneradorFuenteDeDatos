import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

def generate_unique_ids(n):
    ids = np.random.choice(range(1, 100000), n, replace=False)
    return ids

def generate_random_names(n):
    nombres = [fake.name() for _ in range(n)]
    return nombres

def generate_random_last_names(n):
    apellidos = [fake.last_name() for _ in range(n)]
    return apellidos

def generate_region():
    regiones = ['Región de Arica y Parinacota', 'Región de Tarapacá', 'Región de Antofagasta', 'Región de Atacama',
                'Región de Coquimbo', 'Región de Valparaíso', 'Región Metropolitana de Santiago', 'Región del Libertador General Bernardo O\'Higgins',
                'Región del Maule', 'Región de Ñuble', 'Región del Biobío', 'Región de La Araucanía', 'Región de Los Ríos',
                'Región de Los Lagos', 'Región de Aysén del General Carlos Ibáñez del Campo', 'Región de Magallanes y de la Antártica Chilena']
    region = np.random.choice(regiones)
    return region

def generate_comuna():
    comuna = [ "Arica",
    "Putre",
    "Iquique",
    "Alto Hospicio",
    "Antofagasta",
    "Calama",
    "Copiapó",
    "Vallenar",
    "La Serena",
    "Coquimbo",
    "Valparaíso",
    "Viña del Mar",
    "Santiago",
    "Maipú",
    "Rancagua",
    "San Fernando",
    "Talca",
    "Curicó",
    "Chillán",
    "Bulnes",
    "Concepción",
    "Talcahuano",
    "Temuco",
    "Angol",
    "Valdivia",
    "La Unión",
    "Puerto Montt",
    "Osorno",
    "Coyhaique",
    "Chile Chico",
    "Punta Arenas",
    "Puerto Natales"]
    comuna = np.random.choice(comuna)
    return comuna

def generate_sucursal():
    nombre_sucursal = [ 'TotalPro Central',
'TotalPro Mega',
'TotalPro Express',
'TotalPro City',
'TotalPro Plus',
'TotalPro Maxi',
'TotalPro Super',
'TotalPro Market',
'TotalPro Select',
'TotalPro Prime'
    ]
    nombre_sucursal = np.random.choice(nombre_sucursal)
    return nombre_sucursal


def generate_producto_y_categoria_precio():
    productos_categorias_precio = {
        "Carne molida 500gr": ("Carnes", "4990"),
        "Pollo entero": ("Carnes", "8990"),
        "Papas fritas": ("Vegetales", "2490"),
        "Arroz 1kg": ("Granos y cereales", "3990"),
        "Leche descremada": ("Lácteos", "2990"),
        "Manzanas": ("Frutas", "1990"),
        "Pasta de dientes": ("Cuidado personal", "3490"),
        "Aceite de oliva 500ml": ("Aceites y condimentos", "6990"),
        "Pan integral": ("Panadería", "2290"),
        "Yogur natural": ("Lácteos", "1790"),
        "Huevos docena": ("Huevos", "3990"),
        "Cereal de desayuno": ("Cereales", "4490"),
        "Atún en lata": ("Conservas", "1990"),
        "Galletas de chocolate": ("Snacks", "2790"),
        "Salsa de tomate": ("Salsas", "1490"),
        "Café molido 250g": ("Café y té", "5990"),
        "Agua mineral 2L": ("Bebidas", "1290"),
        "Jabón líquido 1L": ("Limpieza del hogar", "3990"),
        "Detergente en polvo": ("Limpieza del hogar", "4990"),
        "Cepillo de dientes": ("Cuidado personal", "2490"),
        "Pañuelos faciales": ("Artículos de baño", "1990"),
        "Papel higiénico": ("Artículos de baño", "3490"),
        "Lechuga": ("Vegetales", "1290"),
        "Tomate": ("Vegetales", "1990"),
        "Filete de salmón": ("Pescados y mariscos", "9990"),
        "Pasta penne 500g": ("Pasta", "1790"),
        "Mantequilla": ("Lácteos", "3290"),
        "Queso fresco": ("Lácteos", "4990"),
        "Aceitunas en frasco": ("Aceites y condimentos", "2990"),
        "Cerveza pack 6": ("Bebidas alcohólicas", "7990"),
        "Vino tinto reserva": ("Vinos", "12990"),
        "Refresco de cola 2L": ("Bebidas", "1490"),
        "Jugo de naranja 1L": ("Bebidas", "2490"),
        "Helado de vainilla 1L": ("Helados", "3990"),
        "Cereal para gatos": ("Mascotas", "6990"),
        "Pañales desechables": ("Bebés", "8990"),
        "Salsa picante": ("Salsas", "2290"),
        "Canela molida": ("Especias", "1990"),
        "Crema de manos": ("Cuidado personal", "4490"),
        "Shampoo": ("Cuidado personal", "3990"),
        "Acondicionador": ("Cuidado personal", "4290"),
        "Gel de ducha": ("Cuidado personal", "3490"),
        "Desodorante en barra": ("Cuidado personal", "2990"),
        "Mermelada de fresa": ("Desayunos y untables", "3490"),
        "Miel de abeja": ("Desayunos y untables", "5990"),
        "Cereal de arroz": ("Cereales", "3490"),
        "Aceitunas rellenas": ("Aceites y condimentos", "2790"),
        "Gaseosa de limón 2L": ("Bebidas", "1990"),
        "Cerveza artesanal": ("Bebidas alcohólicas", "9990"),
        "Vino blanco semiseco": ("Vinos", "10990"),
        "Crema corporal": ("Cuidado personal", "6490"),
        "Gel de aloe vera": ("Cuidado personal", "5990"),
        "Salsa de soja": ("Salsas", "3490"),
        "Té verde en hojas": ("Café y té", "4990"),
        "Café instantáneo": ("Café y té", "7990"),
        "Pan de molde": ("Panadería", "2490"),
        "Tortillas de maíz": ("Panadería", "1990"),
        "Cereal para perros": ("Mascotas", "8990"),
        "Comida para gatos en lata": ("Mascotas", "1790"),
        "Comida para perros en lata": ("Mascotas", "2290"),
        "Snacks para perros": ("Mascotas", "3990"),
        "Snacks para gatos": ("Mascotas", "2990"),
        "Pastas para modelar": ("Juguetes", "4990"),
        "Bloques de construcción": ("Juguetes", "12990"),
        "Muñeca de trapo": ("Juguetes", "8990"),
        "Pelota de fútbol": ("Deportes", "5990"),
        "Balón de baloncesto": ("Deportes", "7990"),
        "Raqueta de tenis": ("Deportes", "19990"),
        "Baraja de cartas": ("Juegos de mesa", "1990"),
        "Rompecabezas de 1000 piezas": ("Juegos de mesa", "14990"),
        "Juego de ajedrez": ("Juegos de mesa", "29990"),
        "Puzzle de madera": ("Juegos de mesa", "9990"),
        "Pistola de agua": ("Juguetes", "3990"),
        "Lápices de colores": ("Material escolar", "2990"),
        "Cuaderno de dibujo": ("Material escolar", "4490"),
        "Mochila escolar": ("Material escolar", "12990"),
        "Tijeras de punta roma": ("Material escolar", "1990"),
        "Pegamento escolar": ("Material escolar", "1490"),
        "Papel de regalo": ("Material escolar", "3990"),
        "Jabón en barra": ("Limpieza del hogar", "1790"),
        "Desinfectante de manos": ("Limpieza del hogar", "1990"),
        "Limpiador multiusos": ("Limpieza del hogar", "4990"),
        "Limpiador de vidrios": ("Limpieza del hogar", "3490"),
        "Esponja abrasiva": ("Limpieza del hogar", "1990"),
        "Bayeta de microfibra": ("Limpieza del hogar", "2490"),
        "Quitamanchas en spray": ("Limpieza del hogar", "3990"),
        "Cepillo para inodoro": ("Limpieza del hogar", "1990"),
        "Desengrasante": ("Limpieza del hogar", "5990"),
        "Limpiador de suelos": ("Limpieza del hogar", "4490"),
        "Bolsas de basura (rollo)": ("Limpieza del hogar", "2990"),
        "Trapo de limpieza (unidad)": ("Limpieza del hogar", "1490"),
        "Papel de cocina (rollo)": ("Limpieza del hogar", "3990"),
        "Esponja para lavar platos": ("Limpieza del hogar", "2290"),
        "Detergente para ropa delicada": ("Limpieza del hogar", "6990"),
        "Aromatizante para ropa": ("Limpieza del hogar", "4490"),
        "Limpiador de alfombras": ("Limpieza del hogar", "7990"),
        "Fregona de microfibra": ("Limpieza del hogar", "3490"),
        "Limpiador de horno": ("Limpieza del hogar", "8990"),
        "Desatascador de tuberías": ("Limpieza del hogar", "4990"),
        "Blanqueador": ("Limpieza del hogar", "3490"),
        "Cepillo para polvo": ("Limpieza del hogar", "1990"),
        "Insecticida en spray": ("Limpieza del hogar", "5990"),
        "Ambientador en aerosol": ("Limpieza del hogar", "2490"),
        "Velas aromáticas": ("Decoración", "1990"),
        "Espejo de cuerpo entero": ("Decoración", "9990"),
        "Jarrón decorativo": ("Decoración", "3490"),
        "Cojín decorativo": ("Decoración", "1990"),
        "Lámpara de pie": ("Decoración", "8990"),
        "Marco de fotos": ("Decoración", "1490"),
        "Cortinas opacas": ("Decoración", "5990"),
        "Alfombra de salón": ("Decoración", "7990"),
        "Mesa auxiliar": ("Muebles", "4990"),
        "Silla plegable": ("Muebles", "2990"),
        "Estante de pared": ("Muebles", "3990"),
        "Mesa de centro": ("Muebles", "6990"),
        "Taburete de bar": ("Muebles", "3990"),
        "Sillón reclinable": ("Muebles", "12990"),
        "Cama individual": ("Muebles", "7990"),
        "Mesa de comedor": ("Muebles", "14990"),
        "Sofá de dos plazas": ("Muebles", "15990"),
        "Armario de tela": ("Muebles", "5990"),
        "Escritorio de ordenador": ("Muebles", "8990"),
        "Silla de oficina": ("Muebles", "6990"),
        "Cama de matrimonio": ("Muebles", "12990"),
        "Cuna de bebé": ("Muebles", "9990"),
        "Mesa de noche": ("Muebles", "4990"),
        "Mesa de estudio": ("Muebles", "7990"),
        "Sofá cama": ("Muebles", "18990"),
        "Sillón giratorio": ("Muebles", "10990"),
        "Mesa de cocina": ("Muebles", "5990"),
        "Cómoda con cajones": ("Muebles", "11990"),
        "Mesa de jardín": ("Muebles", "9990"),
        "Silla de jardín": ("Muebles", "4990"),
        "Tumbona de jardín": ("Muebles", "7990"),
        "Sombrilla para jardín": ("Muebles", "3990"),
        "Estantería para libros": ("Muebles", "6990"),
        "Armario de cocina": ("Muebles", "14990"),
        "Cajonera de baño": ("Muebles", "7990"),
        "Banco de entrada": ("Muebles", "8990"),
        "Mueble de televisión": ("Muebles", "9990"),
        "Cama litera": ("Muebles", "16990"),
        "Escritorio de trabajo": ("Muebles", "10990"),
        "Mesa de estudio para niños": ("Muebles", "4990"),
        "Silla de estudio para niños": ("Muebles", "2990"),
        "Juguetero de tela": ("Muebles", "3990"),
        "Organizador de zapatos": ("Muebles", "2990"),
        "Perchero de pie": ("Muebles", "4990"),
        "Estante para zapatos": ("Muebles", "1990"),
        "Soporte para TV": ("Muebles", "5990"),
        "Mesa plegable": ("Muebles", "3990"),
        "Silla plegable de playa": ("Muebles", "1990"),
        "Estante para vinos": ("Muebles", "2990"),
        "Mesa de picnic": ("Muebles", "9990"),
        "Mesa de actividades para bebé": ("Muebles", "5990"),
        "Silla alta para bebé": ("Muebles", "4990"),
        "Cambiador de pañales": ("Muebles", "7990"),
        "Jaula para pájaros": ("Mascotas", "8990"),
        "Acuario de cristal": ("Mascotas", "12990"),
        "Terrario para reptiles": ("Mascotas", "14990"),
        "Hamaca para gatos": ("Mascotas", "5990"),
        "Rascador para gatos": ("Mascotas", "4990"),
        "Bebedero automático para mascotas": ("Mascotas", "3990"),
        "Comedero automático para mascotas": ("Mascotas", "4490"),
        "Casa para perros": ("Mascotas", "6990"),
        "Transportín para mascotas": ("Mascotas", "7990"),
        "Correa para perros": ("Mascotas", "2490"),
        "Collar para perros": ("Mascotas", "1990"),
        "Arnés para perros": ("Mascotas", "2990"),
        "Cama para perros": ("Mascotas", "4990"),
        "Ropa para mascotas": ("Mascotas", "3490"),
        "Juguete para perros (pelota)": ("Mascotas", "1990"),
        "Juguete para gatos (ratón de peluche)": ("Mascotas", "1490"),
        "Comedero para pájaros": ("Mascotas", "990"),
        "Bebedero para pájaros": ("Mascotas", "890"),
        "Comedero para peces": ("Mascotas", "1290"),
        "Columpio para pájaros": ("Mascotas", "1490"),
        "Casita para pájaros": ("Mascotas", "1990"),
        "Filtro para acuario": ("Mascotas", "2990"),
        "Calentador para acuario": ("Mascotas", "3490"),
        "Luz LED para acuario": ("Mascotas", "1990"),
        "Termómetro para acuario": ("Mascotas", "990"),
        "Decoración para acuario": ("Mascotas", "1490"),
        "Comida para peces tropicales (bote)": ("Mascotas", "990"),
        "Comida para peces de agua fría (bote)": ("Mascotas", "1090"),
        "Comida para peces de fondo (bote)": ("Mascotas", "1190"),
        "Comida para pájaros (bolsa)": ("Mascotas", "1490"),
        "Arena para gatos (saco)": ("Mascotas", "4990"),
        "Lecho higiénico para roedores (bolsa)": ("Mascotas", "3990"),
        "Jaula para roedores": ("Mascotas", "5990"),
        "Rueda para roedores": ("Mascotas", "1490"),
        "Túnel para roedores": ("Mascotas", "990"),
        "Bebedero para roedores": ("Mascotas", "990"),
        "Comedero para roedores": ("Mascotas", "890"),
        "Heno para roedores (bolsa)": ("Mascotas", "1490"),
        "Snacks para roedores (bolsa)": ("Mascotas", "990"),
        "Transportín para roedores": ("Mascotas", "4990"),
        "Casa para roedores": ("Mascotas", "1990"),
        "Juguete para roedores": ("Mascotas", "1490"),
        "Collar antipulgas para perros": ("Mascotas", "2990"),
        "Champú para mascotas": ("Mascotas", "3490"),
        "Spray antiparasitario para mascotas": ("Mascotas", "3990"),
        "Juguete para perros (hueso de goma)": ("Mascotas", "2490"),
        "Cepillo para gatos": ("Mascotas", "1990"),
        "Arena para gatos (saco de sílice)": ("Mascotas", "5990"),
        "Jaula para conejos": ("Mascotas", "6990"),
        "Comedero automático para peces": ("Mascotas", "3490"),
        "Tijeras para mascotas": ("Mascotas", "1990"),
        "Ropa para perros (abrigo)": ("Mascotas", "4990"),
        "Cortauñas para mascotas": ("Mascotas", "1490"),
        "Rascador para gatos (torre)": ("Mascotas", "8990"),
        "Bolso transportín para gatos": ("Mascotas", "3990"),
        "Transportín para pájaros": ("Mascotas", "4990"),
        "Jaula para hámster": ("Mascotas", "2990"),
        "Casa para tortugas": ("Mascotas", "9990"),
        "Correa extensible para perros": ("Mascotas", "3490"),
        "Chaleco salvavidas para perros": ("Mascotas", "5990"),
        "Hueso de cuero para perros": ("Mascotas", "1990"),
        "Pelota para perros (resistente)": ("Mascotas", "2490"),
        "Juguete para gatos (caña con plumas)": ("Mascotas", "1990"),
        "Cepillo para caballos": ("Mascotas", "3490"),
        "Pienso para caballos (saco)": ("Mascotas", "9990"),
        "Collar para pájaros": ("Mascotas", "990"),
        "Vestido para mascotas": ("Mascotas", "4990"),
        "Pañales para mascotas": ("Mascotas", "3990"),
        "Disfraz para mascotas": ("Mascotas", "3490"),
        "Correa de cuero para perros": ("Mascotas", "4990"),
        "Snacks para peces (bolsa)": ("Mascotas", "990"),
        "Cepillo para conejos": ("Mascotas", "1990"),
        "Hamaca para hámster": ("Mascotas", "1490"),
        "Jaula para pájaros grande": ("Mascotas", "11990"),
        "Arena para gatos aglomerante": ("Mascotas", "7990"),
        "Saco de heno para roedores": ("Mascotas", "4990")}
    producto = np.random.choice(list(productos_categorias_precio.keys()))
    categoria, precio = productos_categorias_precio[producto]
    return producto, categoria, precio

def choose_promotion():
    promocion = ['Tarjeta TotalPro Premium',
    'Tarjeta TotalPro Basic',
    'Tarjeta American express',
    'Sin promoción']
    promocion = np.random.choice(promocion)
    return promocion

def choose_cargo():
    nombre_sucursal = [ 'Gerente',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Trabajador Interno',
'Jefe de area',
'Jefe de area',
'Jefe de area',
'Trabajador externo',
'Trabajador externo',
'Trabajador externo',
'Trabajador externo',
'Trabajador externo'
    ]
    nombre_sucursal = np.random.choice(nombre_sucursal)
    return nombre_sucursal


# Definir la tabla Dim_Sucursal
Dim_Sucursal = pd.DataFrame({
    'ID_Sucursal': generate_unique_ids(12000),  # Clave primaria
    'Nombre': [generate_sucursal() for _ in range(12000)],
    'Region': [generate_region() for _ in range(12000)],
    'Comuna': [generate_comuna() for _ in range(12000)]
})

# Definir la tabla Dim_Producto
Dim_Producto = pd.DataFrame({
    'ID_Producto': generate_unique_ids(12000),  # Clave primaria
    'Nombre': [generate_producto_y_categoria_precio()[0] for _ in range(12000)], 
    'Categoría': [generate_producto_y_categoria_precio()[1] for _ in range(12000)],
    'Precio': [generate_producto_y_categoria_precio()[2] for _ in range(12000)],
    'Stock':[random.randint(15, 90) for _ in range(12000)]
})


# Definir la tabla Dim_Cliente
Dim_Cliente = pd.DataFrame({
    'ID_Cliente': generate_unique_ids(12000),  # Clave primaria
    'Nombre': generate_random_names(12000),
    'Apellido': generate_random_last_names(12000),
    'Frecuencia_Compra': [np.random.randint(1, 11) for _ in range(12000)]
})

# Definir la tabla Dim_Promocion
Dim_Promocion = pd.DataFrame({
    'ID_Promocion': generate_unique_ids(12000),  # Clave primaria
    'Nombre': [choose_promotion() for _ in range(12000)],
})

# Definir la tabla Dim_Personal
Dim_Personal = pd.DataFrame({
    'ID_Personal': generate_unique_ids(12000),  # Clave primaria
    'Nombre': generate_random_names(12000),
    'Apellido':generate_random_last_names(12000),
    'Cargo': [choose_cargo() for _ in range(12000)],
})

Fact_Ventas_Diarias = pd.DataFrame({
    'ID_Venta': generate_unique_ids(12000),  # Clave primaria
    'ID_Sucursal': np.random.choice(Dim_Sucursal['ID_Sucursal'], 12000),
    'ID_Producto': np.random.choice(Dim_Producto['ID_Producto'], 12000),
    'ID_Cliente': np.random.choice(Dim_Cliente['ID_Cliente'], 12000),
    'ID_Promocion': np.random.choice(Dim_Promocion['ID_Promocion'], 12000),
    'ID_Personal': np.random.choice(Dim_Personal['ID_Personal'], 12000),
    'Cantidad de productos': np.random.randint(1, 100, 12000),  # Ejemplo de generación de cantidades aleatorias
    'Precio': np.random.uniform(15000, 250000, 12000),  # Ejemplo de generación de precios aleatorios
    'Hora_Transaccion': pd.date_range(start='2024-01-01', end='2024-12-31', periods=12000)  # Ejemplo de generación de fechas aleatorias
})

# Generación de precios unitarios en pesos chilenos
precio_unitario = np.random.uniform(1000, 4000, len(Fact_Ventas_Diarias))

# Ajuste de precio total en función de la cantidad de productos
Fact_Ventas_Diarias['Precio'] = precio_unitario * Fact_Ventas_Diarias['Cantidad de productos']

# Crear un objeto ExcelWriter
with pd.ExcelWriter('BD_TotalPro.xlsx') as writer:
    # Escribir cada DataFrame en una hoja separada
    pd.DataFrame(Dim_Sucursal).to_excel(writer, index=False, sheet_name='Sucursal')
    pd.DataFrame(Dim_Producto).to_excel(writer, index=False, sheet_name='Producto')
    pd.DataFrame(Dim_Cliente).to_excel(writer, index=False, sheet_name='Datos de Clientes')
    pd.DataFrame(Dim_Promocion).to_excel(writer, index=False, sheet_name='Tipo Promoción')
    pd.DataFrame(Dim_Personal).to_excel(writer, index=False, sheet_name='Datos del Personal')
    pd.DataFrame(Fact_Ventas_Diarias).to_excel(writer, index=False, sheet_name='Ventas Diarias')
