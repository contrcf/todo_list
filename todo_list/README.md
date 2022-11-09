# Precondiciones
Se asume que ya tiene Python 3+ instalado en su sistema. Si no, por favor, instalelo.  

Revisar este link acorde a su sistema operativo: 
[Python 3 Installation & Setup Guide](https://realpython.com/installing-python/)

Se asume que se tiene instalado Poetry
(https://python-poetry.org/docs/#installation)


# Instalación de ambiente virtual
Abra una terminal, y dirijase a la carpeta raiz del proyecto y ejecute el siguiente comando:

```
poetry env use python
```

# Instalacion de bibliotecas
Para instalar las bibliotecas necesarias, use este comando:
```
poetry install
```

¡Listo, la configuración está lista!

## Probando el codigo
Ingresar al folder src
```
cd todo_list_proyect/todo_list/src
```
Revisando comandos posibles a ejecutar
```
poetry run python -m to_do_list --help
```

Listar los archivos
```
poetry run python -m to_do_list list
```

Crear una nueva lista
```
(opcion 1) poetry run python -m to_do_list list -ln mi-lista

(opcion 2) poetry run python -m to_do_list list --listname mi-lista
```

Mostrar la lista
```
(opcion 1) poetry run python -m to_do_list show -ln mi_lista

(opcion 2) poetry run python -m to_do_list show --listname mi-lista
```


Agregar una tarea
```
(opcion 1) poetry run python -m to_do_list add -ln mi_lista_jevb -tn "Hacer ejercicio" -d "correr en el parque" -o "Jose"

(opcion 2) poetry run python -m to_do_list add --listname mi_lista_jevb --taskame "Hacer ejercicio" --description "correr en el parque" --owner "Jose"
```

Actualizar un campo
```
(opcion 1) poetry run python -m to_do_list update -ln mi_lista_jevb -i 0 -f status -c done

(opcion 2) poetry run python -m to_do_list update --listname --taskid 0 --field status --change done
```



## Ejecutar pruebas unitarias y de integracion
* Pruebas unitarias
```
pytest tests/unit/ -v
```

* Pruebas de integracion
```
pytest tests/integration/ -v
```
