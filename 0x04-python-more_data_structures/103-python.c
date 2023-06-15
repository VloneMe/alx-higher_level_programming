#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - This fun prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	const char *type;

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - This fun prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	Py_ssize_t print_size = size > 10 ? 10 : size;

	printf("  first %zd bytes: ", print_size);
	for (i = 0; i < print_size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (print_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
