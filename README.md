**Guía para Ejecutar el Proyecto**

Este proyecto utiliza Flutter para el frontend, Python Flask para el backend, y MySQL como base de datos.
Requisitos Previos
**Frontend (Flutter)**
1.	Flutter SDK:
o	Descarga desde Flutter.dev.
o	Sigue las instrucciones de instalación para tu sistema operativo.
o	Agrega Flutter a tu variable de entorno PATH.
2.	Android Studio:
o	Descarga e instala desde Android Studio.
o	Configura un dispositivo virtual (AVD) con el emulador Pixel 6 API 33.
3.	Visual Studio Code:
o	Descarga e instala desde Visual Studio Code.
o	Instala las extensiones:
	Dart.
	Flutter.
4.	Verifica la instalación de Flutter:
o	Abre una terminal y ejecuta:
flutter doctor
o	Asegúrate de que todas las secciones estén marcadas como [✓].

**Backend (Python Flask)**
1.	Python:
o	Instala Python 3.8 o superior desde python.org.
o	Asegúrate de agregar Python a tu variable de entorno PATH.
2.	Entorno virtual:
o	Crea un entorno virtual en la carpeta del proyecto backend:
python -m venv venv
o	Activa el entorno virtual:
	Windows: venv\Scripts\activate
3.	Instalar dependencias:
o	Usa el archivo requirements.txt para instalar las dependencias:

pip install -r requirements.txt

5.	MySQL:
o	Instala MySQL desde MySQL.com.
o	Crea una base de datos según la configuración del backend.
o	Asegúrate de que las credenciales de acceso estén configuradas correctamente en config.py.

**Configuración del Proyecto**
**1. Backend**
1.	Navega a la carpeta del proyecto backend:
cd backend
2.	Inicia el servidor Flask:
python app.py
3.	Asegúrate de que el servidor esté corriendo en http://127.0.0.1:5000/.

**2. Frontend**
1.	Navega a la carpeta del proyecto Flutter.
2.	Asegúrate de abrir el archivo main.dart en Visual Studio Code.
Este archivo debe contener el punto de entrada de tu aplicación Flutter.

**3.	Configura el dispositivo:**
1.	Abre Android Studio.
2.	Ejecuta el emulador Pixel 6 API 33.
3.	Verifica que el emulador está activo.
   
**4.	Inicia la depuración:**
1.	En la parte superior derecha de Visual Studio Code, haz clic en el botón Start Debugging esto compilará y ejecutará el proyecto en el emulador seleccionado.
   
**5.	Verifica que la aplicación esté corriendo en el dispositivo virtual.**

**Notas Importantes**
1. Asegúrate de que el backend esté corriendo antes de iniciar el frontend.
2. 	Usa la URL http://10.0.2.2:5000/ en el frontend para conectarte al backend cuando uses un emulador de Android.
3. 	Si no se ejecuta el apk  entra a configuración, seguridad y luego desactiva Google Play Protect.
