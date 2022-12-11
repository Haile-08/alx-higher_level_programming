#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *po = (PyListObject *)p;
	
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", po->allocated);
	while (i < size)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(po->ob_item[i])->tp_name);
		i++;
	}
}
