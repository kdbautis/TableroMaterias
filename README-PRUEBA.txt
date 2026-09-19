TABLERO SEPARADO V1
===================

Estructura
----------
tablero.html
core.json
relation-metrics.json
evidence/<relationId>.json
servidor-local.py
iniciar-servidor.bat

1. PRUEBA LOCAL COMPLETA
------------------------
1) Descomprimir el ZIP.
2) Ejecutar iniciar-servidor.bat (requiere Python instalado).
3) Abrir:
   http://localhost:8000/tablero.html

No abrir tablero.html con doble clic (file://), porque fetch() queda sujeto a restricciones del navegador.

2. CONFIGURACION DE DATOS
-------------------------
Por defecto tablero.html busca los datos en el mismo origen y carpeta:
  ./core.json
  ./relation-metrics.json
  ./evidence/...

También acepta un origen distinto mediante query string:
  tablero.html?dataBaseUrl=https%3A%2F%2FEJEMPLO-DATOS

Esto permite usar el mismo HTML desde SharePoint y apuntarlo temporalmente a un servidor HTTPS externo.

3. SHAREPOINT + SERVIDOR LOCAL
------------------------------
Un HTML servido por SharePoint usa HTTPS. No es una prueba fiable apuntarlo directamente a:
  http://localhost:8000
porque el navegador puede bloquear contenido mixto (HTTPS -> HTTP). Además localhost siempre significa "la PC del usuario que está abriendo el tablero".

Para probar el HTML desde SharePoint usando los datos que están en tu PC, expón temporalmente este servidor mediante un túnel HTTPS (por ejemplo Cloudflare Tunnel o ngrok). El servidor-local.py ya envía Access-Control-Allow-Origin: * para permitir la prueba CORS.

Ejemplo conceptual:
  cloudflared tunnel --url http://localhost:8000

El túnel entregará una URL HTTPS parecida a:
  https://xxxx.trycloudflare.com

Entonces abre el HTML de SharePoint agregando:
  ?dataBaseUrl=https%3A%2F%2Fxxxx.trycloudflare.com

IMPORTANTE: esa URL temporal solo funciona mientras el servidor local y el túnel estén ejecutándose.

4. QUÉ SE CARGA
---------------
Al iniciar:
  core.json
  relation-metrics.json

Al abrir el detalle de Unidades o Resultados de una relación:
  evidence/<relationId>.json

La evidencia se conserva en memoria durante la sesión para no descargarla dos veces.

5. ALCANCE DE V1
----------------
COURSE_OUTLINES todavía permanece dentro de tablero.html deliberadamente. Se dejó así para validar primero la separación de datos y el lazy loading de evidence/ con el menor cambio posible. En una segunda versión puede extraerse también a archivos remotos bajo demanda.
