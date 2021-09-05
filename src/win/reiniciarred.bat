@echo off
wmic path win32_networkadapter where index=7 call disable
timeout /T 3 /NOBREAK
wmic path win32_networkadapter where index=7 call enable
