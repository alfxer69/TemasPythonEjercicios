Este es la documentacion del repositorio Web-Scraping.Python

Que es Web scraping:

Web scraping es una técnica empleada para extraer grandes cantidades de información
desde sitios web mediante programas automatizados. 
• Generalmente utilizaremos análisis HTML, interacción mediante APIs o manejo de páginas 
dinámicas con JavaScript. 
• En el campo del NLP, los datos son tan importantes como el algoritmo. El web scraping 
proporciona acceso a vastos recursos de texto que pueden ser utilizados para entrenar 
modelos de lenguaje, análisis de sentimientos, y más

Internet: un océano de datos

• Internet alberga una cantidad exponencialmente creciente de datos, con 
millones de GB de información generados cada día. 
• Estos datos son una mina de oro para los data scientists, existe multitud de datos 
abiertos que podemos utilizar. 
• La habilidad de transformar este océano de datos crudos en información útil y 
accionable es lo que hacen a los expertos en NLP tan valiosos.

Se calcula que entre el 80% y el 95% del contenido de Internet 
es inaccesible a través de búsquedas convencionales y 
requieren de métodos de extracción especializados

#Tipos de web scraping

• Existen multitud de tipos y técnicas de web scraping. Su elección dependerá de 
nuestras necesidades, la estructura del sitio web y el tipo de datos necesarios. 
• Tipos más importantes de web scraping: 
• Web scraping estático: No depende de interacciones complejas del usuario 
para mostrar su contenido. 
• Web scraping dinámico: Usa herramientas automáticas para interactuar con 
sitios webs que requieren acciones del usuario, como clicks o ingreso de 
información, para revelar la información. 
• API scraping: Extracción de datos a través de APIs públicas o privadas que los 
sitios web proporcionan para acceder programáticamente a su información.

Web scraping estático

El web scraping estático se refiere a la extracción de datos de páginas web que no 
requieren interacción del usuario para mostrar su contenido completo. Estos datos 
son accesibles directamente en el código HTML inicial de la página. 
• Proceso básico: 
1. Cargar el HTML de la página web mediante una petición HTTP. 
2. Parsear el HTML para extraer la información deseada utilizando herramientas 
específicas. 
• En Python las principales herramientas son: 
• Requests: Simplifica envío de solicitudes HTTP. 
• BeautifulSoup: Facilita el web scraping permitiendo el parseo de documentos 
HTML y XML.

Web scraping dinámico

El web scraping dinámico se refiere al conjunto de técnicas de extracción de 
datos de sitios web que cargan su contenido de manera asincrónica, 
generalmente mediante JavaScript. 
• A diferencia del scraping estático, donde el contenido ya está presente en el 
HTML inicial, el scraping dinámico puede requerir interacción con la página
(como hacer clic o desplazarse) para cargar los datos. 
• La idea es simular la interacción de un usuario real con la página para que se 
ejecuten todos los scripts necesarios y se revele el contenido oculto. 
• En Python la principal herramienta es Selenium.

Selenium

Selenium es una poderosa librería de Python para automatizar navegadores 
web, permitiendo hacer web scraping dinámico. 
• Selenium permite simular una amplia gama de interacciones humanas como 
clicks, ingreso de texto, y desplazamientos, lo que facilita la extracción de datos 
que de otro modo estarían inaccesibles. 
• Únicamente debe ser usado cuando sea necesario, generalmente se trata de 
una herramienta lenta en comparación con técnicas de scraping estáticas, 
ademas de requerir de un buen manejo de tiempos de espera y excepciones 
para ser efectivo.

Consideraciones éticas y legales

Al realizar web scraping, es crucial no solo considerar qué se puede hacer técnicamente, sino 
también qué se debería hacer desde una perspectiva ética y legal. 
• Consideraciones éticas: 
• Respeto por la privacidad: Evitar recolectar datos personales sin consentimiento, especialmente 
en jurisdicciones con regulaciones estrictas como el GDPR en Europa. 
• Impacto en los sitios web: Considerar el efecto del scraping en los recursos del servidor del sitio 
web, evitando causar una carga excesiva que podría degradar el servicio para otros usuarios. 
• Transparencia y uso de datos: Ser transparente sobre cómo se utilizan los datos extraídos y 
asegurarse de que su uso no infrinja los derechos de los individuos o entidades afectadas. 
• Consideraciones legales: 
• Cumplimiento de la ley: Familiarizarse con y adherirse a las leyes locales que regulan la 
extracción de datos, incluyendo leyes de derechos de autor y de privacidad. 
• Términos de servicio: Respetar los términos de servicio de los sitios web, que a menudo incluyen 
cláusulas específicas sobre la prohibición o limitación del scraping.

Buenas prácticas

Respeto a los términos de servicio: Antes de comenzar a hacer scraping, verifica y sigue los 
términos de servicio del sitio web, que pueden prohibir o limitar esta práctica. 
• Adherencia al archivo robots.txt: Consulta el archivo robots.txt del sitio para respetar las 
restricciones impuestas sobre el scraping de ciertas áreas del sitio web. 
• Gestión de la carga del servidor: Evita sobrecargar los servidores del sitio implementando 
retrasos entre solicitudes y evitando el scraping durante los picos de tráfico para minimizar el 
impacto en el rendimiento del servidor. 
• Privacidad y protección de datos: Asegúrate de proteger la privacidad y cumplir con las 
regulaciones de protección de datos como el GDPR, evitando recolectar y almacenar datos 
personales sin consentimiento. 
• Uso ético de los datos: Utiliza los datos recopilados de manera ética, para los fines permitidos, y 
mantén transparencia sobre cómo se utilizan estos datos. 
• Estrategias de extracción eficientes: Optimiza tus scripts de scraping usando técnicas de cacheo y 
seleccionando precisamente los datos a extraer para mejorar la eficiencia y reducir la carga en los 
recursos del sitio web.





