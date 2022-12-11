#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t s, i = 0;
	
	s = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", Py_REFCNT(p));
	while (i < s)
	{
		printf("Element %li: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
