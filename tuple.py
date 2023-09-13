import sys
import platform
import time

a = [1, 2, 3, 4]
b = ['a', 'b', 'c']

t = tuple(zip(a, b))
print(t)
print(t[0])
print(t[0][0])
print(t[0][1])

# test TUPLE memory
a_list = [1, 2, 3, 4]
a_tuple = (1, 2, 3, 4)
print(sys.getsizeof(a_list), "bytes")
print(sys.getsizeof(a_tuple), "bytes")
print("----------------------------------")

# Test performance
v_list = list(range(1000))
v_tuples = tuple(range(1000))


# LIST performance
start = time.time_ns()
for i in range(len(v_list)):
    a = v_list[i]
end = time.time_ns()
print("Total time for LIST :", end - start)

# TUPLE performance
start = time.time_ns()
for i in range(len(v_tuples)):
    b = v_tuples[i]
end = time.time_ns()
print("Total time for TUPLE :", end - start)
