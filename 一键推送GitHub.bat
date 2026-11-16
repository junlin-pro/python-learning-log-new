@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "http_proxy="
set "https_proxy="
set "HTTP_PROXY="
set "HTTPS_PROXY="
set "GIT_TERMINAL_PROMPT="

echo ================================================
echo   Push python-learning-log to GitHub
echo ================================================
echo.
echo  If a window pops up asking you to sign in,
echo  click "Sign in with your browser" and authorize.
echo.
echo  Please DO NOT close this window until it ends.
echo.

for /L %%i in (1,1,3) do (
  echo --- Attempt %%i of 3 ---
  git push -u origin main
  if not errorlevel 1 goto done
  echo.
  echo [retry] waiting 5 seconds...
  timeout /t 5 >nul
  echo.
)

echo [FAILED] All 3 attempts failed.
echo.
echo  Next step: switch to phone hotspot and run this again.
goto end

:done
echo.
echo [SUCCESS] Uploaded. Open your repo page and refresh:
echo https://github.com/junlin-pro/python-learning-log-new

:end
echo.
pause
