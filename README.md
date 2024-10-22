# ObfuLS
Demo code for a lunch and learn session on tools for obfuscation and distribution of Python code.

Contains a tiny package for computing prime numbers, and notebooks with demos of using different tools for obfuscation and distribution of the code in the package.

## Obfuscation
We look at obfuscation of source code using [SOURCEdefencer](https://www.sourcedefender.co.uk/) and [PyArmor](https://pyarmor.dashingsoft.com/), and show why this might not be a good idea by demonstrating how the obfuscation can be reverse-engineered. For this, we look at [SourceRestorer](https://github.com/Lazza/SourceRestorer) and [PyArmor-Unpacker](https://github.com/Svenskithesource/PyArmor-Unpacker) in combination with [pycdc](https://github.com/zrax/pycdc).

## Distribution
For distribution, we look at the tools [PyInstaller](https://pyinstaller.org/en/stable/index.html) and [Nuitka](https://github.com/Nuitka/Nuitka). Both tools are suitable for code distribution, but we demonstrate that source code is easily recoverable from an executable generated with PyInstaller with a combination of [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) and pycdc. We also briefly look at performance improvements that are achieved with the executable generated with Nuitka.
