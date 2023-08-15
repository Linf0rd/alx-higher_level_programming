#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: Pointer to the Python object.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, x;
	PyObject *obj;
	PyTypeObject *type;

	size = PyList_Size(p);
	print("[*] Size of the Python List = &ld\n", size);
	obj = PyList_GetItem(p, 0);
	type = obj->ob_type;
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (x = 0; x < size; x++)
	{
		obj = PyList_GetItem(p, x);
		type = obj->ob_type;
		print("Element %ld: %s\n", x, type->tp_name);
	}
}
