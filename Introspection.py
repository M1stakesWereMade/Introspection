def introspection_info(obj):
    """
    Функция для интроспекции объекта. Возвращает информацию о типе, атрибутах, методах, модуле и других свойствах объекта.

    :param obj: Объект для анализа
    :return: Словарь с данными об объекте
    """
    import inspect

    obj_info = {
        "type": type(obj).__name__,
        "module": getattr(obj, "__module__", "Unknown"),
        "doc": inspect.getdoc(obj),
        "attributes": [],
        "methods": [],
    }

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name, None)
        if callable(attr):
            obj_info["methods"].append(attr_name)
        else:
            obj_info["attributes"].append(attr_name)

    return obj_info


number_info = introspection_info(42)
print(number_info)
