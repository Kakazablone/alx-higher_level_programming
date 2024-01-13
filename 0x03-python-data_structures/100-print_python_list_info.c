#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about pytohn lists
 *
 * @p: python object
**/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	if (!PyList_Check(p))
    {
        PyErr_SetString (PyExc_TypeError, "Object not found in list");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
