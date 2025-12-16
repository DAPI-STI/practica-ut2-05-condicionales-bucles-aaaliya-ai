[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DhD_dIUD)
# Práctica 02.05 · Bucles y condicionales en Python (funciones + tests)

En esta práctica vas a resolver ejercicios sencillos de **condicionales** (`if / elif / else`)
y **bucles** (`for`, `while`) implementando funciones en Python.

La corrección se hace automáticamente con **pytest** (tests).  
Además, tendrás un archivo **`__main__.py`** para probar tus funciones “a mano” sin necesidad
de lanzar los tests.

---

## Objetivo

- Implementar funciones que utilicen **condicionales y bucles**.
- Comprobar que tu solución es correcta pasando **todos los tests**.
- Familiarizarte con una **estructura de proyecto real** en Python.

---

## Estructura del proyecto

Cuando abras el proyecto verás algo parecido a esto:

```text
practica_0205_bucles_condicionales/
├─ src/
│  ├─ __main__.py
│  ├─ ex01_password.py
│  ├─ ex02_safe_divide.py
│  ├─ ex03_even_odd.py
│  ├─ ex04_tax.py
│  ├─ ex05_years.py
│  └─ ex06_table.py
├─ test/
│  └─ test_practica_0205.py
├─ README.md
├─ requirements.txt
└─ .gitignore

¿Qué es cada carpeta / archivo?
1) src/ (tu código)

Aquí están los ejercicios.
Cada archivo exXX_....py contiene una función que debes completar.

Al principio, las funciones tienen algo como:

raise NotImplementedError(...)

Eso significa: “todavía no está hecho”.
Tu trabajo es sustituirlo por una implementación correcta.

✅ Regla principal: solo debes editar archivos dentro de src/.
2) test/ (los tests)

Aquí está test/test_practica_0205.py con todas las pruebas unitarias.

Un test es código que:

    llama a tus funciones

    comprueba que devuelven el resultado esperado

Si algo falla, pytest te dirá:

    qué test ha fallado

    qué se esperaba

    qué se obtuvo realmente

✅ Regla principal: NO modifiques los tests.
En evaluación automática, modificar los tests suele invalidar la entrega.
3) src/__main__.py (para probar sin tests)

Este archivo es un pequeño programa principal para hacer pruebas manuales.

Permite ejecutar:

python -m src

¿Qué significa esto?

    python -m src le dice a Python: “ejecuta el paquete src”.

    Al hacerlo, Python busca y ejecuta el archivo:

    src/__main__.py

Desde ahí puedes:

    probar funciones con tus propios ejemplos

    imprimir resultados por pantalla

    entender mejor qué hace tu código

🔎 Importante: __main__.py NO sustituye a los tests,
pero es muy útil para practicar y experimentar.
4) requirements.txt (dependencias)

Lista las librerías necesarias para el proyecto.
En esta práctica solo necesitas:

    pytest → para ejecutar los tests

5) .gitignore

Indica qué archivos no deben subirse al repositorio
(cachés, entornos virtuales, archivos temporales, etc.).
¿Qué debes hacer?

    En src/ tienes 6 ejercicios, cada uno con una función sin implementar.

    En test/test_practica_0205.py tienes todas las pruebas unitarias.

    Tu objetivo es hacer que TODOS los tests pasen.

Primeros pasos
1) Crear entorno virtual (opcional, recomendado)

python -m venv .venv

Activar:

Windows (PowerShell / CMD):

.venv\Scripts\activate

macOS / Linux:

source .venv/bin/activate

2) Instalar dependencias

pip install -r requirements.txt

Cómo trabajar durante la práctica
A) Ejecutar los tests (forma recomendada)

Ejecuta los tests con:

python -m pytest -q

    python -m pytest asegura que se use el Python activo

    -q (quiet) muestra una salida más limpia

Al principio es normal ver muchos fallos:
las funciones todavía no están implementadas.
B) Probar manualmente desde __main__.py

Si quieres probar tus funciones sin tests:

python -m src

Eso ejecuta src/__main__.py.
Puedes editar ese archivo para añadir llamadas a las funciones, por ejemplo:

from ex03_even_odd import is_even

print(is_even(7))

Flujo recomendado de trabajo

    Ejecuta los tests:

python -m pytest -q

Elige un ejercicio (por ejemplo src/ex03_even_odd.py).

Lee el docstring de la función.

Sustituye el NotImplementedError por tu solución.

Vuelve a ejecutar:

    python -m pytest -q

    Repite hasta que todos los tests pasen ✅

Consejos

    Si un test falla, lee el mensaje de error: da mucha información.

    Haz cambios pequeños y prueba a menudo.

    Si te atascas, prueba primero desde python -m src con ejemplos sencillos
    y luego valida con pytest.

Entrega

La entrega se evalúa automáticamente según el resultado de los tests.

Cuando todos los tests pasen, tendrás:

✅ Código correcto
✅ Uso de condicionales y bucles
✅ Proyecto organizado
✅ Verificación automática (como en proyectos reales)