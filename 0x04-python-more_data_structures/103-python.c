#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t x, size;
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (x = 0; x < size; x++)
	{
		printf("Element %ld: %s\n", x, Py_TYPE(PyList_GetItem(p, x))->tp_name);
		if (strcmp(Py_TYPE(PyList_GetItem(p, x))->tp_name, "bytes") == 0)
			print_python_bytes(PyList_GetItem(p, x));
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects.
 * @p: PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, x;
	char *str;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", size + 1);
	for (x = 0; x <= size; x++)
		printf(" %02x", str[x] & 0xff);
	printf("\n");
}
