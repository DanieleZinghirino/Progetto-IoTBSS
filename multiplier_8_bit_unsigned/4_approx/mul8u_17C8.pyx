from libc.stdint cimport *

cdef extern:
    uint16_t mul8u_17C8(uint8_t A, uint8_t B)


cpdef int mul(int a,int b):
    return mul8u_17C8(a,b)

