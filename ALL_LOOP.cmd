@Echo off
title BECH.py Mmdrza.Com
Pushd "%~dp0"
start P2SH.cmd
start P2PKH.cmd
start P2WPKH.cmd
:loop
python BECH.py
goto loop