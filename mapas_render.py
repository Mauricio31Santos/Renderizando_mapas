import folium

# Cria o mapa #

mapa1 = folium.Map(
    location=[-23.711263550794243, -46.6609725287771],
    tiles='Stamen Terrain', #estilo do mapa
    zoom_start=16

    
)

# adicionar marcador no mapa #

folium.Marker(
    [-23.711263550794243, -46.6609725287771],
    popup='<i>Jardim Apura</i>',
    tooltip='Click aqui'
).add_to(mapa1)

# Salva html do mapa #

mapa1.save(r',\mapa2.html')