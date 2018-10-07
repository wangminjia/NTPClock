
def convert(src, dst, n):
    count = 0x01
    s = 0x01;
    for i in range(n):
        tmp = src[i]
        for j in range(8):
            if (i < 8):
                index = 2 * j
            else:
                index = 2 * j + 1
            if (tmp & count) == count:
                dst[index] = dst[index] | s
            else:
                dst[index] = dst[index] & (~s)
            if (count == 0x80):
                count = 0x01
            else:
                count <<= 1
        if s == 0x80:
            s = 0x01
        else:
            s <<= 1
