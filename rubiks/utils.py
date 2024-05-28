""" Utility functions for Rubik's cube """__all__ = ["assertAngle", "R", "Rx", "Ry", "Rz"]import numpy as npallowedRotations = [0, 90, 180, -90, 270]def cln(value: float) -> 'float | int':    retval = 0 if abs(value) < 1e-2 else round(value, 2)    return retvaldef degToRad(deg: int) -> 'float':    retval = deg * np.pi / 180    return retvaldef radToDeg(rad: float) -> 'int':    retval = rad * 180 / np.pi    return retvaldef cpos(deg):    return np.cos(degToRad(deg))def spos(deg):    return np.sin(degToRad(deg))    def cneg(deg):    return -1 * cpos(deg)def sneg(deg):    return -1 * spos(deg)def assertAngle(phi: int) -> 'None':    assert isinstance(phi, (int, np.int64)), f"Phi [{phi}, {type(phi)}] is not an int"    assert phi in allowedRotations, f"phi [{phi}] is not allowed: {allowedRotations}"def R(phi: int) -> 'np.array':    return np.array([[cln(cpos(phi)), cln(sneg(phi))],                     [cln(spos(phi)), cln(cpos(phi))]])def Rx(phi: int) -> 'np.array':    assertAngle(phi)    return np.array([[1, 0, 0],                     [0, cln(cpos(phi)), cln(sneg(phi))],                     [0, cln(spos(phi)), cln(cpos(phi))]])def Ry(phi: int) -> 'np.array':    assertAngle(phi)    return np.array([[cln(cpos(phi)), 0, cln(spos(phi))],                     [0, 1, 0],                     [cln(sneg(phi)), 0, cln(cpos(phi))]])def Rz(phi: int) -> 'np.array':    assertAngle(phi)    return np.array([[cln(cpos(phi)), cln(sneg(phi)), 0],                     [cln(spos(phi)), cln(cpos(phi)), 0],                     [0, 0, 1]])