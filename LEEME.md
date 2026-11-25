# Tarjeta de Control Personal - Golf Croquet

App simple para marcar, por equipo, en qué vuelta (1 a 10) se pasó cada uno
de los 6 aros (A.I a A.VI) y ver el TOTAL (suma de vueltas — como en golf,
menos es mejor).

## Cómo se usa la app
1. Escribís el número de EQUIPO.
2. Por cada aro (A.I ... A.VI) tocás el número de vuelta en la que lo pasaste.
   Si te equivocás, tocás el mismo número de nuevo para deseleccionarlo.
3. Cuando completás los 6 aros, el TOTAL se calcula solo.
4. "Nueva tarjeta" limpia todo para el próximo equipo.

## Probarla en la PC (sin generar el APK)
Necesitás Python y Kivy instalados:
```
pip install kivy
python main.py
```

## Generar el APK gratis (sin instalar Android SDK)
Este proyecto incluye un workflow de GitHub Actions que compila el APK
automáticamente en los servidores de GitHub (gratis, dentro del uso normal
de una cuenta personal). Pasos:

1. Creá un repositorio nuevo en GitHub (puede ser privado).
2. Subí TODO el contenido de esta carpeta (incluida la carpeta oculta
   `.github`) a ese repositorio.
3. Entrá a la pestaña "Actions" del repositorio en GitHub. Debería
   dispararse solo el workflow "Build APK" (o lo iniciás manualmente con
   "Run workflow").
4. Esperá a que termine (la primera vez tarda bastante, 15-30 minutos,
   porque descarga el Android SDK/NDK).
5. Cuando termine, abrí el workflow finalizado y bajá el archivo llamado
   "tarjeta-croquet-apk" desde la sección "Artifacts". Ahí está tu .apk.
6. Pasás ese .apk al celular (por USB, Drive, WhatsApp, etc.) y lo instalás
   habilitando "Instalar apps de origen desconocido" si Android lo pide.

## Archivos del proyecto
- `main.py` — código de la app (Kivy)
- `buildozer.spec` — configuración de empaquetado Android
- `.github/workflows/build.yml` — automatización que genera el APK
