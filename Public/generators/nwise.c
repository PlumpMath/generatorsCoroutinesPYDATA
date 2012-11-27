#include <Python.h>

typedef struct {
	PyObject_HEAD
	int idx;
	PyObject *values[3];
	PyObject *source;
	iternextfunc source_next;
} nwise;

static PyObject *
nwise_new(PyTypeObject *type, PyObject *args) {
	PyObject *source, *source_it;
	nwise *obj;

	if (!PyArg_UnpackTuple(args, "gen", 1, 1, &source))
		return NULL;

	source_it = PyObject_GetIter(source);
	if (source_it == NULL)
		return NULL;

	obj = (nwise *)type->tp_alloc(type, 0);
	if (obj == NULL) {
		Py_DECREF(source_it);
		return NULL;
	}
	obj->idx = 0;
	obj->source = source_it;
	obj->source_next = obj->source->ob_type->tp_iternext; 
	obj->values[obj->idx] = (obj->source_next)(obj->source);
	obj->idx = (obj->idx + 1)%3;
	obj->values[obj->idx] = (obj->source_next)(obj->source);
	obj->idx = (obj->idx + 1)%3;
	obj->values[obj->idx] = (obj->source_next)(obj->source);
	obj->idx = (obj->idx + 1)%3;

	return (PyObject *)obj;
}

PyObject* nwise_iter(PyObject *self) {
	Py_INCREF(self);
	return self;
}

PyObject* nwise_iternext(PyObject *self) {
	PyObject *res;
	nwise *_self = (nwise*)self;

	PyObject *first, *second, *third;
	first  = _self->values[(_self->idx+0)%3];
	second = _self->values[(_self->idx+1)%3];
	third  = _self->values[(_self->idx+2)%3];
	if (first == NULL || second == NULL || third == NULL) {
		PyErr_SetNone(PyExc_StopIteration);
		return NULL;
	}
	res = PyTuple_Pack(3, first, second, third );

	_self->values[_self->idx] = (_self->source_next)(_self->source);
	_self->idx = (_self->idx + 1)%3;
	
	return res;
}

PyObject* nwise_send(PyObject *self, PyObject *args) {

	PyObject *source;
	PyObject *res;

	if (!PyArg_UnpackTuple(args, "send", 1, 1, &source))
		return NULL;

	nwise *_self = (nwise*)self;
	_self->source = source;
	
	res = (_self->ob_type->tp_iternext)((PyObject*)_self);
	return res;
}

static PyMethodDef nwise_methods[] = {
    {"send", (PyCFunction)nwise_send, METH_VARARGS, "restart with new source" },
    {NULL}  /* Sentinel */
};

static PyTypeObject nwise_type = {
	PyObject_HEAD_INIT(NULL)
	.tp_name      = "nwise.nwise",
	.tp_basicsize = sizeof(nwise),
	.tp_flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_ITER,
	.tp_doc       = "",
	.tp_iter      = (getiterfunc)nwise_iter,
	.tp_iternext  = (iternextfunc)nwise_iternext,
	.tp_new       = (newfunc)nwise_new,
	.tp_methods   = nwise_methods,
};

static PyMethodDef module_methods[] = {
	{NULL} /* Sentinel */
};

PyMODINIT_FUNC
initnwise(void) {
	PyObject* m;

	if (PyType_Ready(&nwise_type) < 0)  return;
	Py_INCREF(&nwise_type);

	m = Py_InitModule("nwise", module_methods);
	PyModule_AddObject(m, "nwise", (PyObject *)&nwise_type);
}
