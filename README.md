# scan_tool
Herramienta que combina nmap y github

Descripción del Código
Este código realiza un escaneo de puertos en una dirección IP especificada y busca vulnerabilidades asociadas con los servicios encontrados mediante la API de GitHub.

Importaciones
os: Permite interactuar con el sistema operativo.
subprocess: Se usa para ejecutar comandos del sistema (aunque no se utiliza en el fragmento mostrado).
nmap: Biblioteca utilizada para escanear puertos.
requests: Para hacer solicitudes HTTP, en este caso, para acceder a la API de GitHub.
webbrowser: Permite abrir un navegador web.
re: Proporciona soporte para expresiones regulares, utilizado para validar direcciones IP.
Funciones
is_valid_ip(ip):

Verifica si una dirección IP tiene un formato válido (dos a tres dígitos separados por puntos).
Comprueba que cada octeto (parte de la IP) esté en el rango de 0 a 255.
scan_ports(ip):

Utiliza nmap para escanear la dirección IP proporcionada en busca de puertos abiertos y los servicios asociados.
Retorna una lista de puertos abiertos junto con el nombre del servicio y la versión que se está ejecutando.
search_github_vulnerabilities(version_info):

Toma una lista de versiones de servicios y busca repositorios en GitHub que mencionen vulnerabilidades relacionadas con esas versiones.
Devuelve una lista de URL de repositorios y la cantidad de estrellas (estrellas que indican popularidad).
create_html(open_ports):

Crea un documento HTML que muestra los resultados del escaneo de puertos.
Agrega enlaces a GitHub para cada vulnerabilidad encontrada, configurándolos para abrirse en una nueva pestaña.
save_html_file(html_content):

Guarda el contenido HTML generado en un archivo llamado resultados.html.
Flujo Principal
El programa comienza pidiendo al usuario que ingrese una dirección IP.
Valida la dirección IP utilizando is_valid_ip.
Si es válida, realiza el escaneo de puertos mediante scan_ports.
Crea el contenido HTML con los resultados y posibles vulnerabilidades llamando a create_html, luego guarda este contenido como un archivo HTML.
Finalmente, abre el archivo HTML en el navegador y reproduce un sonido (solo en Linux) como una notificación.

Enlace de youtube como funciona la herramienta

[![Alt text](https://img.youtube.com/vi/_O3bQBIGyLg/0.jpg)](https://www.youtube.com/watch?v=_O3bQBIGyLg)
