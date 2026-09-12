# AllTheInfo

Mod de información para **Project Zomboid B42.20**, cliente puro y seguro en
multijugador. Enseña los números que el juego se guarda: las cifras exactas
encima de cada barra sin marcar, la ropa comparada con la que llevas puesta, lo
que sale de un crafteo, tiempos de cocinado y de quemado, generadores,
surtidores, construcciones, cultivos, heridas, rasgos, profesiones, habilidades
y los 26 moodles.

[En la Workshop de Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3781129962)
· [Read me in English](README.md)

---

## La regla que sostiene todo lo demás

**Cada cifra sale del código del propio juego, nunca de una estimación.** Si un
número no se puede rastrear hasta un campo o un método de `projectzomboid.jar`,
la fila no se imprime. Mejor una fila de menos que un número falso, porque el
jugador va a actuar sobre ese número en cuanto lo lea.

En la práctica eso significa que el trabajo no es sobre todo Lua. Es leer
bytecode decompilado para averiguar qué hace el juego de verdad y luego escribir
las cuatro líneas que lo cuentan. Dos ejemplos que acabaron como comentarios en
el código:

- La probabilidad de fallar una reparación es un punto más alta de lo que dice
  la fórmula. El juego tira `Rand.Next(100) <= fail` sobre un valor que sale de
  0 a 99, así que una probabilidad que las matemáticas recortan a 0 sigue
  fallando una vez de cada cien. El mod muestra la de verdad, no la de la
  fórmula.
- `ObjectTooltip.padLeft` es un campo público de Java, pero el binding de Lua
  solo expone métodos, así que leerlo devuelve `nil`. Como `checkFont()` lo
  fija a `MeasureStringX(font, "0")`, el mod lo deriva igual y cuadra con
  vanilla a cualquier escala de interfaz, en vez de clavar un número de píxeles.

Hay unos 205 hallazgos de este tipo documentados en las notas internas del
proyecto, cada uno verificado en bytecode antes de dejarle cambiar una sola
línea de salida.

## Cómo está montado

```
Core.lua        registro de proveedores, caché de 500 ms, formato y colores
Render.lua      el único archivo que dibuja, envuelve el tooltip de vanilla
providers/      17 archivos: cuerpo a cuerpo, armas de fuego, comida, ropa...
world/          generadores, cultivos, animales, trampas, pesca, construcciones
character/      habilidades, rasgos, salud, multiplicadores de XP, creación
Options.lua     172 interruptores individuales
SelfTest.lua    batería de pruebas en juego, desde la consola de depuración
```

Dos reglas duras mantienen las capas separadas, y están escritas en la cabecera
de `Core.lua`: **el núcleo nunca sabe qué es un objeto, y un proveedor nunca
dibuja.** Un proveedor es una función `fn(out, item, chr)` que añade filas;
dónde acaben esas filas en pantalla no es asunto suyo. Añadir un dato nuevo es
un archivo y una llamada a `AllInfo.register`.

Las funciones de vanilla se **envuelven, nunca se reemplazan**, para componer
con otros mods que enganchen el mismo tooltip en lugar de pelearse con ellos.

## Opciones

Cada línea que imprime el mod es un interruptor propio, 172 en total, repartidos
entre objetos, mundo, personaje y crafteo. No un interruptor por función, uno
por *línea*: si te molesta una fila de un tooltip, se va esa fila y no se va
nada más con ella.

Un interruptor apagado no es una fila escondida. Es un proveedor que no llega a
ejecutarse, así que apagar un área entera no cuesta nada mientras juegas.

## Traducciones

Diez idiomas: inglés, chino simplificado, ruso, español, portugués de Brasil,
alemán, turco, francés, japonés y polaco.

Solo inglés y español están escritos a mano. Los otros ocho los **genera**
`tools/i18n.py` a partir de tablas de frases en `tools/lang/`, y el generador se
niega a escribir si encuentra un fragmento que no conoce. Ese es el objetivo:
que una clave nueva en inglés no pueda colarse en un archivo traducido hablando
inglés en silencio.

La unidad de traducción no es la clave, es el fragmento con los números fuera:

```
"-15 climb chance"   ->   plantilla "{} climb chance",  números ["-15"]
```

Eso convierte 436 claves por idioma en unas 310 frases, mantiene la redacción
consistente en todas partes y hace imposible traducir mal una cifra, porque los
números pasan intactos. Añadir un idioma es un archivo y una línea.

Donde vanilla ya tiene una clave para algo (`Tooltip_weapon_Condition`,
`IGUI_perks_*`), el mod la reutiliza y hereda gratis los 29 idiomas del juego.

## Herramientas

Cuatro, porque el runtime del juego es mal sitio para enterarte de que te has
equivocado:

| Herramienta | Qué hace |
|---|---|
| `tools/LuaCheck.java` | Compila cada `.lua` con el compilador Kahlua del propio juego, que rechaza sintaxis que el Lua de referencia acepta, y cuenta locales por función. Kahlua admite 200 y revienta el archivo entero en la 201, así que avisa a las 150 |
| `tools/JarGrep.java` | Recorre `projectzomboid.jar` buscando toda clase que toque un campo o un método dado, para contrastar un cambio con los llamadores reales |
| `tools/i18n.py` | Genera y valida los ocho idiomas derivados |
| `tools/OptionAudit.py` | Audita los 172 interruptores sin abrir el juego: los que no apagan nada, ids que no existen, claves de traducción que falten en cualquiera de los diez idiomas, ids repetidos |

Encima de eso, `SelfTest.lua` corre dentro del juego desde la consola de
depuración. Apaga cada interruptor de tooltip sobre un objeto de muestra y
comprueba que las filas cambian, y dice por su nombre lo que no ha conseguido
probar.

## Estructura del repositorio

```
mod/42.20/      el mod tal cual se publica, 40 archivos Lua, unas 11k líneas
tools/          las cuatro herramientas de arriba, más las tablas de frases
```

`mod.info` tiene que vivir dentro de `mod/42.20/`, no en la raíz de la carpeta
del mod: B42 no detecta un mod plano.

## Instalación desde el código

Copiar `mod/` a `%USERPROFILE%\Zomboid\mods\AllInfo` y **cerrar el juego al
escritorio** antes de volver a abrirlo. Volver al menú principal no basta, el
Lua de los mods se lee una sola vez al arrancar.

## Licencia

MIT, ver [LICENSE](LICENSE).
