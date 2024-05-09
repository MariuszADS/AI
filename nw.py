import numpy as np

def vec2(x, y):
    return [x, y]

def dot2(a, b):
    return a[0]*b[0] + a[1]*b[1]

def len2(a):
    return np.sqrt(dot2(a, a))

def nor2(a):
    return a / len2(a)

def prn2(a):
    return f"({a[0]:.2f}, {a[1]:.2f})"

def vec3(x, y, z):
    return [x, y, z]

def dot3(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def len3(a):
    return np.sqrt(dot3(a, a))

def nor3(a):
    return a / len3(a)

def prn3(a):
    return f"({a[0]:.2f}, {a[1]:.2f}, {a[2]:.2f})"

def angle2(a, b):
    cos_theta = dot2(a, b) / (len2(a) * len2(b))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # Zabezpieczenie przed błędami numerycznymi
    return np.degrees(np.arccos(cos_theta))

def angle3(a, b):
    cos_theta = dot3(a, b) / (len3(a) * len3(b))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # Zabezpieczenie przed błędami numerycznymi
    return np.degrees(np.arccos(cos_theta))