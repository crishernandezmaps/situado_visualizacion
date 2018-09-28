#  Herramienta para el procesamiento de imágenes recolectadas en trabajo etnográfico de campo <sup>[1](#foot01)</sup>

## Presentación
El [Instituto de la Vivienda de la Facultad de Arquitectura y Urbanismo](https://vivienda.uchilefau.cl/) de la [Universidad de Chile](http://www.uchile.cl/), ha creado para el proyecto Fondecyt Situado una herramienta de código abierto para el procesamiento de imágenes y la extracción y agregación de [metadata](https://es.wikipedia.org/wiki/Metadatos).

La siguiente herramienta de software esta creada pensando en las necesidades de procesamiento de imágenes recolectadas en trabajo de campo etnográfico. Se busca a través de esta pieza de software que los investigadores centren sus capacidades mas en la observación experta y menos en el procesamiento de datos, especialmente fotografías. 

Las fotografías representan en el trabajo de campo etnográfico una fuente muy rica de información, la cual por su inmediatez y sencillez en el rescate a través de teléfonos móviles, incrementa la capacidad narrativa y la profundidad de las observaciones. Asimismo, los sensores con los que cuenta un teléfono móvil entrega información adicional a la imagen, como fecha y hora de la captura y localización (coordenadas). 

Las coordenadas en particular permiten adherir otra componente relevante al análisis etnográfico, que es la espacialidad. El poder agregar el lugar al trabajo de campo, involucra distinciones para la identificación de patrones geográfico-culturales, indispensables para el estudio de lo urbano.

De especial interés también fue a la hora del desarrollo de esta herramienta, es la capacidad de agregar metadata adicional a las fotografías, lo que permite clasificarlas y generar diversos análisis adicionales.   

## Aspectos técnicos

### Lenguaje de Programación
Esta herramienta esta desarrollada en el lenguaje de programación [Python](https://www.python.org/) (versión 3.6.4). Las librerías utilizadas son:
- Numpy
- Pandas
- Fnmatch
- PIL
- IPTCInfo
- Json

El objetivo de la herramienta es la lectura de las fotografías alojadas localmente en el computador del investigador, la extracción de la metadata tanto [Exif](https://es.wikipedia.org/wiki/Exchangeable_image_file_format) como [Iptc](https://iptc.org/standards/photo-metadata/).




---
<a name="foot01">1</a>: Autoras(es): Carlos Lange, Michelle Cáceres, Cris Hernández.