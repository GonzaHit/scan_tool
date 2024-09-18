import os  
import subprocess  
import nmap  
import requests  
import webbrowser  
import re  # Importar módulo para expresiones regulares  

def is_valid_ip(ip):  
    # Expresión regular para validar dirección IP  
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')  
    if pattern.match(ip):  
        # Verificar que cada parte de la IP esté en el rango 0-255  
        octets = list(map(int, ip.split('.')))  
        return all(0 <= octet <= 255 for octet in octets)  
    return False  

def scan_ports(ip):  
    nm = nmap.PortScanner()  
    nm.scan(ip, arguments='-sV')  # Escaneo de puertos y versiones de servicios  
    ports_info = []  

    # Obtener todos los protocolos y sus puertos abiertos  
    for proto in nm[ip].all_protocols():  
        lport = nm[ip][proto].keys()  
        for port in lport:  
            service = nm[ip][proto][port]['name']  
            version = nm[ip][proto][port].get('version', 'N/A')  
            ports_info.append((port, service, version))  
            
    return ports_info  

def search_github_vulnerabilities(version_info):  
    search_results = []  
    base_url = 'https://api.github.com/search/repositories'  
   
    # Iterar sobre cada versión  
    for version in version_info:  
        version_query = f"vulnerabilities {version}"  
        response = requests.get(base_url, params={'q': version_query, 'sort': 'stars', 'order': 'desc'})  
        repos = response.json().get('items', [])  
        
        for repo in repos:  
            search_results.append((repo['html_url'], repo['stargazers_count']))  
   
    return search_results  

def create_html(open_ports):  
    html_content = "<html><head><title>Resultados de Escaneo</title></head><body>"  
    for port, service, version in open_ports:  
        html_content += f"<h3>Puerto: {port} - Servicio: {service} - Versión: {version}</h3>"  
        vulnerabilities = search_github_vulnerabilities([version])  # Enviamos una lista con la versión  
        if vulnerabilities:  
            html_content += "<ul>"  
            for repo_url, stars in vulnerabilities:  
                html_content += f"<li><a href='{repo_url}' target='_blank'>{repo_url} - Stars: {stars}</a></li>"  # target="_blank" añadido  
            html_content += "</ul>"  
        else:  
            html_content += "<p>No se encontraron vulnerabilidades.</p>"  
    html_content += "</body></html>"  
    return html_content  

def save_html_file(html_content):  
    with open("resultados.html", "w") as file:  
        file.write(html_content)  
        
if __name__ == "__main__":  
    while True:  # Bucle para asegurar una entrada válida  
        ip_address = input("Introduce la dirección IP a escanear: ")  
        if is_valid_ip(ip_address):  # Validar la IP  
            break  
        else:  
            print("La dirección IP ingresada no es válida. Inténtalo de nuevo.")  

    open_ports = scan_ports(ip_address)  
    html_content = create_html(open_ports)  
    save_html_file(html_content)  

    # Abrir el archivo en el navegador  
    webbrowser.open('resultados.html')  

    # Alarma sonora (en Windows; en Linux, puedes utilizar otra librería o comando)  
    os.system('play -nq -t alsa synth 1 sine 440')  # Reproducir un sonido en Linux