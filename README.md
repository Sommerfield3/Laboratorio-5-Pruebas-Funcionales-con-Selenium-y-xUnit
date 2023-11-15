# Laboratorio-5-Pruebas-Funcionales-con-Selenium-y-xUnit

Inicialmente se debe ejecutar el chromedriver.exe dentro de la carpeta DriverC en orden de permitirle al script enviar los comandos escritos en este.
Se uso el driver para la versión 119.0.6045.105 compatible con la versión usada para las pruebas (119.0.6045.125). A la fecha esta versión del driver se encuentra disponible en el siguiente enlace: https://googlechromelabs.github.io/chrome-for-testing/#stable

# Casos de prueba:
Usamos el método de Clases de Equivalencia para generar los casos de prueba, donde "a" es el primer valor, "b" el segundo valor a ingresar.

| Escenario de Prueba |  Valores de Prueba | Resultado Esperado |
| ------------------- | ------------------ | ------------------ |
| Caso válido         | a=50,b=10          |          5         |
| Caso Inválido       | a=50,b=15          |          5         |
| Caso Inválido       | a=50,b=-10         |          5         |

# Script:
El script presenta 2 casos de prueba básicos basados en el formato de pruebas para la página (se creó una función de prueba para casos genéricos: test_percentage_calculation).

# Resultado:

![image](https://github.com/Sommerfield3/Laboratorio-5-Pruebas-Funcionales-con-Selenium-y-xUnit/assets/104087488/e9d936d6-2510-4b0c-9807-c71cfda7020d)
