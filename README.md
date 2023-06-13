# Discord Bot: 
* author: Saúl Sosa Díaz
* email: _alu0101404141@ull.edu.es_

## Resumen
En este repositorio se implementa un bot de Discord utilizando la librería Discord.py.
El bot, escrito en Python es una aplicación que utiliza la biblioteca Discord.py para interactuar con la API de Discord.
Para interactuar con la API de discord es necesario un token que se obtienene en el [portal de desarrolladores de Discord](https://discord.com/developers/applications).


## Dependencias:
Para ejecutar este programa son necesarias las siguientes librerías:
* [jokeapi](https://sv443.net/jokeapi/v2/): Es una API pública que proporciona una amplia colección de chistes y bromas en diferentes categorías.
```BASH
python3 pip install jokeapi
```

* [discord](https://discordpy.readthedocs.io/en/stable/): Se utiliza para interactuar con la API de Discord.
```BASH
python3 pip install discord.py
python3 -m pip install -U "discord.py[voice]"
```

* [PyNaCL](https://pypi.org/project/PyNaCl/): Se utiliza para el soporte de voz del bot.
```BASH
python3 pip install pynacl
```

## Ejecución 
El fichero `main` está en la carpeta /src, para ejecutar el programa ejecute el siguiente programa:

```BASH
python3 ./src/main.py
```

## Comandos
El bot tiene los siguientes comandos:
* **_help**: Muestra la lista de comandos disponibles.
* **_play <link>**: Pide al bot que reproduzca un audio con el link de youtube que se le pasen como parámetro. **Sin embargo el link es ignorado y reproduce [Never gonna give you up de Rick Asley](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)**
* **_joke**: Pide al bot que cuente un chiste.
* **_leave**: Pide al bot que abandone el canal de voz.


## Estructura de directorios
```
  .
  ├── src            # Código fuente
  ├── images         # Imágenes 
  └── audio          # Audio
```

## Referencias:
* [portal de desarrolladores de Discord](https://discord.com/developers/applications).
* [jokeapi](https://sv443.net/jokeapi/v2/).
* [discord](https://discordpy.readthedocs.io/en/stable/).
* [PyNaCL](https://pypi.org/project/PyNaCl/).
* [never gonna give you up](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley).


[Python website]: <https://www.python.org/downloads/>
