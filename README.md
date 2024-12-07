# Guía para Ejecutar el Proyecto

Este proyecto utiliza **Flutter** para el frontend, **Python Flask** para el backend, y **MySQL** como base de datos.

---

## Requisitos Previos

### Frontend (Flutter)
1. **Flutter SDK**:
   - Descarga desde [Flutter.dev](https://flutter.dev).
   - Sigue las instrucciones de instalación para tu sistema operativo.
   - Agrega Flutter a tu variable de entorno `PATH`.

2. **Android Studio**:
   - Descarga e instala desde [Android Studio](https://developer.android.com/studio).
   - Configura un dispositivo virtual (AVD) con el emulador Pixel 6 API 33.

3. **Visual Studio Code**:
   - Descarga e instala desde [Visual Studio Code](https://code.visualstudio.com).
   - Instala las extensiones:
     - **Dart**.
     - **Flutter**.

4. **Verifica la instalación de Flutter**:
   - Abre una terminal y ejecuta:
     ```bash
     flutter doctor
     ```
   - Asegúrate de que todas las secciones estén marcadas como `[✓]`.

---

### Backend (Python Flask)
1. **Python**:
   - Instala Python 3.8 o superior desde [python.org](https://www.python.org).
   - Asegúrate de agregar Python a tu variable de entorno `PATH`.

2. **Entorno virtual**:
   - Crea un entorno virtual en la carpeta del proyecto backend:
     ```bash
     python -m venv venv
     ```
   - Activa el entorno virtual:
     - En Windows:
       ```bash
       venv\Scripts\activate
       ```

3. **Instalar dependencias**:
   - Usa el archivo `requirements.txt` para instalar las dependencias:
     ```bash
     pip install -r requirements.txt
     ```

4. **MySQL**:
   - Instala MySQL desde [MySQL.com](https://www.mysql.com).
   - Crea una base de datos según la configuración del backend.
   - Asegúrate de que las credenciales de acceso estén configuradas correctamente en `config.py`.

---

## Configuración del Proyecto

### 1. Backend
1. Navega a la carpeta del proyecto backend:
   ```bash
   cd backend
2. Inicia el servidor Flask:
    ```bash
   python app.py
4. Asegúrate de que el servidor esté corriendo en http://127.0.0.1:5000/.

## 2. Frontend
1. Navega a la carpeta del proyecto Flutter.

2. Asegúrate de abrir el archivo **main.dart** en Visual Studio Code. Este archivo debe contener el punto de entrada de tu aplicación Flutter.

3. Configura el dispositivo:
* Abre Android Studio.
* Ejecuta el emulador **Pixel 6 API 33**.
* Verifica que el emulador está activo.

4. Inicia la depuración:
* En la parte superior derecha de Visual Studio Code, haz clic en el botón **Start Debugging** esto compilará y ejecutará el proyecto en el emulador seleccionado.

5. Verifica que la aplicación esté corriendo en el dispositivo virtual.

## Notas Importantes
* Asegúrate de que el backend esté corriendo antes de iniciar el frontend.
* Usa la URL http://10.0.2.2:5000/ en el frontend para conectarte al backend cuando uses un emulador de Android.
* Si no se ejecuta el apk  entra a configuración, seguridad y luego desactiva Google Play Protect.
