# Sistema de Gestión Hospitalaria con Django ORM

Este proyecto es una demostración práctica del uso del Mapeo Objeto-Relacional (ORM) de Django para construir un sistema básico de gestión hospitalaria. Se enfoca en la creación de modelos, la realización de migraciones y la ejecución de consultas para manipular datos de médicos, pacientes y citas.

---

## Prueba del Sistema de Gestión Hospitalaria

A continuación, una imagen de prueba mostrando una consulta a la base de datos a través del shell interactivo de Django.

![Prueba de sistema de la gestión hospitalaria](https://github.com/user-attachments/assets/b5eb8d75-7a8f-4845-9b2f-781f57b95ec0)

---

## Análisis del ORM de Django

### ¿Qué pasa con las citas cuando se elimina un médico?

Cuando se elimina un **médico** del sistema, todas sus **citas** asociadas también se eliminan automáticamente.

Esto sucede por la configuración `on_delete=models.CASCADE` que establecimos en el modelo `Cita`:

```python
# gestion/models.py
class Cita(models.Model):
    # ...
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="citas")
    # ...
```

### ¿Qué ventajas tiene usar el ORM en lugar de SQL puro?

Usar el ORM de Django para gestionar la base de datos de nuestro hospital tiene ventajas clave sobre escribir consultas SQL a mano:


Más Rápido y Simple: Escribir Medico.objects.filter(especialidad="Cardiología") es mucho más rápido, legible y menos propenso a errores que redactar SELECT * FROM gestion_medico WHERE especialidad = 'Cardiología';. El código se siente como Python natural, no como un lenguaje diferente incrustado.

Seguridad Automática 🔐: El ORM nos protege automáticamente contra ataques de inyección SQL. Cuando filtramos pacientes o médicos, Django se asegura de que ninguna entrada maliciosa pueda dañar nuestra base de datos, algo de lo que tendríamos que preocuparnos constantemente con SQL puro.

Independencia de la Base de Datos: Hoy usamos SQLite, pero mañana el hospital podría necesitar una base de datos más potente como PostgreSQL. Con el ORM, no tendríamos que cambiar ni una sola línea de nuestro código de consulta. Django se encarga de "traducir" nuestro código Python al lenguaje SQL específico de la base de datos que estemos usando.

Código Más Limpio y Mantenible: Las relaciones entre modelos son muy claras. Por ejemplo, para obtener todas las citas de un paciente, simplemente escribimos paciente.citas.all(). En SQL, esto requeriría una operación JOIN más compleja y verbosa, haciendo el código más difícil de leer y mantener a largo plazo.
