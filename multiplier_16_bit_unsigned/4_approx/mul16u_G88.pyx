from libc.stdint cimport *

cdef extern:
    uint32_t mul16u_G88(uint16_t A, uint16_t B)


cpdef int mul(int a,int b):
    return mul16u_G88(a,b)

