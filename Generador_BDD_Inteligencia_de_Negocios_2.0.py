import pandas as pd
import numpy as np
from faker import Faker

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


def generate_producto_y_categoria():
    productos_categorias = {
        "Carne molida 500gr": ("Carnes", 5.99),
        "Pollo entero": ("Carnes", 8.99),
        "Papas fritas": ("Vegetales", 2.49),
        "Arroz 1kg": ("Granos y cereales", 3.99),
        "Leche descremada": ("Lácteos", 2.99),
        "Manzanas": ("Frutas", 1.99),
        "Pasta de dientes": ("Cuidado personal", 3.49),
        "Aceite de oliva 500ml": ("Aceites y condimentos", 6.99),
        "Pan integral": ("Panadería", 2.29),
        "Yogur natural": ("Lácteos", 1.79),
        "Huevos docena": ("Huevos", 3.99),
        "Cereal de desayuno": ("Cereales", 4.49),
        "Atún en lata": ("Conservas", 1.99),
        "Galletas de chocolate": ("Snacks", 2.79),
        "Salsa de tomate": ("Salsas", 1.49),
        "Café molido 250g": ("Café y té", 5.99),
        "Agua mineral 2L": ("Bebidas", 1.29),
        "Jabón líquido 1L": ("Limpieza del hogar", 3.99),
        "Detergente en polvo": ("Limpieza del hogar", 4.99),
        "Cepillo de dientes": ("Cuidado personal", 2.49),
        "Pañuelos faciales": ("Artículos de baño", 1.99),
        "Papel higiénico": ("Artículos de baño", 3.49),
        "Lechuga": ("Vegetales", 1.29),
        "Tomate": ("Vegetales", 1.99),
        "Filete de salmón": ("Pescados y mariscos", 9.99),
        "Pasta penne 500g": ("Pasta", 1.79),
        "Mantequilla": ("Lácteos", 3.29),
        "Queso fresco": ("Lácteos", 4.99),
        "Aceitunas en frasco": ("Aceites y condimentos", 2.99),
        "Cerveza pack 6": ("Bebidas alcohólicas", 7.99),
        "Vino tinto reserva": ("Vinos", 12.99),
        "Refresco de cola 2L": ("Bebidas", 1.49),
        "Jugo de naranja 1L": ("Bebidas", 2.49),
        "Helado de vainilla 1L": ("Helados", 3.99),
        "Cereal para gatos": ("Mascotas", 6.99),
        "Pañales desechables": ("Bebés", 8.99),
        "Salsa picante": ("Salsas", 2.29),
        "Canela molida": ("Especias", 1.99),
        "Crema de manos": ("Cuidado personal", 4.49),
        "Shampoo": ("Cuidado personal", 3.99),
        "Acondicionador": ("Cuidado personal", 4.29),
        "Gel de ducha": ("Cuidado personal", 3.49),
        "Desodorante en barra": ("Cuidado personal", 2.99),
        "Mermelada de fresa": ("Desayunos y untables", 3.49),
        "Miel de abeja": ("Desayunos y untables", 5.99),
        "Cereal de arroz": ("Cereales", 3.49),
        "Aceitunas rellenas": ("Aceites y condimentos", 2.79),
        "Gaseosa de limón 2L": ("Bebidas", 1.99),
        "Cerveza artesanal": ("Bebidas alcohólicas", 9.99),
        "Vino blanco semiseco": ("Vinos", 10.99),
        "Crema corporal": ("Cuidado personal", 6.49),
        "Gel de aloe vera": ("Cuidado personal", 5.99),
        "Salsa de soja": ("Salsas", 3.49),
        "Té verde en hojas": ("Café y té", 4.99),
        "Café instantáneo": ("Café y té", 7.99),
        "Pan de molde": ("Panadería", 2.49),
        "Tortillas de maíz": ("Panadería", 1.99),
        "Cereal para perros": ("Mascotas", 8.99),
        "Comida para gatos en lata": ("Mascotas", 1.79),
        "Comida para perros en lata": ("Mascotas", 2.29),
        "Snacks para perros": ("Mascotas", 3.99),
        "Snacks para gatos": ("Mascotas", 2.99),
        "Pastas para modelar": ("Juguetes", 4.99),
        "Bloques de construcción": ("Juguetes", 12.99),
        "Muñeca de trapo": ("Juguetes", 8.99),
        "Pelota de fútbol": ("Deportes", 5.99),
        "Balón de baloncesto": ("Deportes", 7.99),
        "Raqueta de tenis": ("Deportes", 19.99),
        "Baraja de cartas": ("Juegos de mesa", 1.99),
        "Rompecabezas de 1000 piezas": ("Juegos de mesa", 14.99),
        "Juego de ajedrez": ("Juegos de mesa", 29.99),
        "Puzzle de madera": ("Juegos de mesa", 9.99),
        "Pistola de agua": ("Juguetes", 3.99),
        "Lápices de colores": ("Material escolar", 2.99),
        "Cuaderno de dibujo": ("Material escolar", 4.49),
        "Mochila escolar": ("Material escolar", 12.99),
        "Tijeras de punta roma": ("Material escolar", 1.99),
        "Pegamento escolar": ("Material escolar", 1.49),
        "Papel de regalo": ("Material escolar", 3.99),
        "Jabón en barra": ("Limpieza del hogar", 1.79),
        "Desinfectante de manos": ("Limpieza del hogar", 2.99),
        "Limpiador de baño": ("Limpieza del hogar", 3.49),
        "Ambientador de aire": ("Limpieza del hogar", 2.49),
        "Esponja de cocina": ("Limpieza del hogar", 1.29),
        "Detergente para lavavajillas": ("Limpieza del hogar", 5.49),
        "Leche condensada": ("Lácteos", 2.49),
        "Leche evaporada": ("Lácteos", 1.99),
        "Crema agria": ("Lácteos", 2.99),
        "Cacao en polvo": ("Café y té", 3.99),
        "Margarina": ("Lácteos", 2.49),
        "Queso rallado": ("Lácteos", 3.99),
        "Salchichas": ("Embutidos", 4.99),
        "Jamón de pavo": ("Embutidos", 3.49),
        "Salami": ("Embutidos", 5.99),
        "Paleta de cerdo": ("Embutidos", 7.99),
        "Sopa instantánea": ("Conservas", 1.29),
        "Salmón ahumado": ("Pescados y mariscos", 11.99),
        "Filete de pescado": ("Pescados y mariscos", 10.99),
        "Cereal para bebés": ("Bebés", 4.99),
        "Compota de manzana": ("Bebés", 2.99),
        "Toallitas húmedas": ("Bebés", 3.49),
        "Detergente para bebés": ("Bebés", 5.99),
        "Aceite de bebé": ("Bebés", 4.49),
        "Crema para pañal": ("Bebés", 3.99),
        "Pañales de tela": ("Bebés", 15.99),
        "Talco para bebés": ("Bebés", 2.49),
        "Champú para bebés": ("Bebés", 4.99),
        "Aceite de cocina": ("Aceites y condimentos", 2.99),
        "Vinagre de manzana": ("Aceites y condimentos", 3.49),
        "Mostaza": ("Aceites y condimentos", 1.99),
        "Kétchup": ("Salsas", 2.49),
        "Mayonesa": ("Salsas", 2.99),
        "Pasta de tomate": ("Salsas", 1.49),
        "Crema de cacahuate": ("Desayunos y untables", 4.99),
        "Mantequilla de almendra": ("Desayunos y untables", 6.49),
        "Mermelada de frutas": ("Desayunos y untables", 3.99),
        "Crema de avellana": ("Desayunos y untables", 5.99),
        "Chocolate en polvo": ("Desayunos y untables", 3.49),
        "Cereal de trigo": ("Cereales", 3.99),
        "Cereal de maíz": ("Cereales", 2.99),
        "Cereal de avena": ("Cereales", 4.49),
        "Cereal de centeno": ("Cereales", 4.99),
        "Galletas de avena": ("Galletas", 2.49),
        "Galletas saladas": ("Galletas", 1.99),
        "Galletas de mantequilla": ("Galletas", 3.49),
        "Galletas de arroz": ("Galletas", 2.79),
        "Galletas integrales": ("Galletas", 2.99),
        "Caramelos de menta": ("Dulces y chocolates", 1.49),
        "Caramelos de fruta": ("Dulces y chocolates", 1.99),
        "Chocolate con leche": ("Dulces y chocolates", 3.49),
        "Chocolate negro": ("Dulces y chocolates", 3.99),
        "Chocolate blanco": ("Dulces y chocolates", 4.49),
        "Goma de mascar": ("Dulces y chocolates", 1.29),
        "Pastillas de menta": ("Dulces y chocolates", 1.79),
        "Caramelo de caramelo": ("Dulces y chocolates", 1.99),
        "Pastel de chocolate": ("Repostería", 8.99),
        "Pastel de vainilla": ("Repostería", 7.99),
        "Galletas de chocolate": ("Repostería", 3.49),
        "Pastel de zanahoria": ("Repostería", 9.99),
        "Tarta de manzana": ("Repostería", 10.99),
        "Croissant de chocolate": ("Panadería", 1.99),
        "Croissant de almendra": ("Panadería", 2.49),
        "Croissant de mantequilla": ("Panadería", 2.29),
        "Croissant de queso": ("Panadería", 2.99),
        "Croissant de jamón y queso": ("Panadería", 3.49),
        "Croissant de chocolate y almendra": ("Panadería", 2.99),
        "Pan de ajo": ("Panadería", 2.49),
        "Pan de centeno": ("Panadería", 2.99),
        "Pan de espelta": ("Panadería", 3.49),
        "Pan de cebolla": ("Panadería", 2.79),
        "Pan de nueces": ("Panadería", 3.99),
        "Pan de pasas": ("Panadería", 3.49),
        "Pan de avena": ("Panadería", 3.29),
        "Pan de maíz": ("Panadería", 2.99),
        "Pan de trigo": ("Panadería", 2.79),
        "Pan de centeno y pasas": ("Panadería", 3.49),
        "Pan de centeno y nueces": ("Panadería", 3.79),
        "Pan de espelta y semillas": ("Panadería", 4.29),
        "Pan de cebolla y pasas": ("Panadería", 3.99),
        "Pan de nueces y pasas": ("Panadería", 4.49),
        "Pan de avena y pasas": ("Panadería", 4.29),
        "Pan de maíz y nueces": ("Panadería", 3.99),
        "Pan de trigo y nueces": ("Panadería", 3.79),
        "Pan de nueces y almendra": ("Panadería", 4.29),
        "Pan de avena y almendra": ("Panadería", 4.49),
        "Pan de espelta y almendra": ("Panadería", 4.99),
        "Pan de cebolla y almendra": ("Panadería", 4.79),
        "Pan de nueces y maíz": ("Panadería", 4.29),
        "Pan de pasas y maíz": ("Panadería", 4.49),
        "Pan de trigo y maíz": ("Panadería", 4.79)}
    producto = np.random.choice(list(productos_categorias.keys()))
    categoria = productos_categorias[producto]
    return producto, categoria

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
    'ID_Sucursal': generate_unique_ids(7000),  # Clave primaria
    'Nombre': [generate_sucursal() for _ in range(7000)],
    'Region': [generate_region() for _ in range(7000)],
    'Comuna': [generate_comuna() for _ in range(7000)]
})

# Definir la tabla Dim_Producto
Dim_Producto = pd.DataFrame({
    'ID_Producto': generate_unique_ids(7000),  # Clave primaria
    'Nombre': [generate_producto_y_categoria()[0] for _ in range(7000)], 
    'Categoría': [generate_producto_y_categoria()[1] for _ in range(7000)],
    'Precio': [generate_producto_y_categoria()[2] for _ in range(7000)]
})

# Definir la tabla Dim_Cliente
Dim_Cliente = pd.DataFrame({
    'ID_Cliente': generate_unique_ids(7000),  # Clave primaria
    'Nombre': generate_random_names(7000),
    'Apellido': generate_random_last_names(7000),
    'Frecuencia_Compra': [np.random.randint(1, 11) for _ in range(7000)]
})

# Definir la tabla Dim_Promocion
Dim_Promocion = pd.DataFrame({
    'ID_Promocion': generate_unique_ids(7000),  # Clave primaria
    'Nombre': [choose_promotion() for _ in range(7000)],
})

# Definir la tabla Dim_Personal
Dim_Personal = pd.DataFrame({
    'ID_Personal': generate_unique_ids(7000),  # Clave primaria
    'Nombre': generate_random_names(7000),
    'Apellido':generate_random_last_names(7000),
    'Cargo': [choose_cargo() for _ in range(7000)],
})

Fact_Ventas_Diarias = pd.DataFrame({
    'ID_Venta': generate_unique_ids(7000),  # Clave primaria
    'ID_Sucursal': np.random.choice(Dim_Sucursal['ID_Sucursal'], 7000),
    'ID_Producto': np.random.choice(Dim_Producto['ID_Producto'], 7000),
    'ID_Cliente': np.random.choice(Dim_Cliente['ID_Cliente'], 7000),
    'ID_Promocion': np.random.choice(Dim_Promocion['ID_Promocion'], 7000),
    'ID_Personal': np.random.choice(Dim_Personal['ID_Personal'], 7000),
    'Cantidad': np.random.randint(1, 100, 7000),  # Ejemplo de generación de cantidades aleatorias
    'Precio': np.random.uniform(1, 1000, 7000),  # Ejemplo de generación de precios aleatorios
    'Hora_Transaccion': pd.date_range(start='2024-01-01', end='2024-12-31', periods=7000)  # Ejemplo de generación de fechas aleatorias
})

# Crear un objeto ExcelWriter
with pd.ExcelWriter('TheRealDatabasexd.xlsx') as writer:
    # Escribir cada DataFrame en una hoja separada
    pd.DataFrame(Dim_Sucursal).to_excel(writer, index=False, sheet_name='Sucursal')
    pd.DataFrame(Dim_Producto).to_excel(writer, index=False, sheet_name='Producto')
    pd.DataFrame(Dim_Cliente).to_excel(writer, index=False, sheet_name='Datos de Clientes')
    pd.DataFrame(Dim_Promocion).to_excel(writer, index=False, sheet_name='Tipo Promoción')
    pd.DataFrame(Dim_Personal).to_excel(writer, index=False, sheet_name='Datos del Personal')
    pd.DataFrame(Fact_Ventas_Diarias).to_excel(writer, index=False, sheet_name='Ventas Diarias')
