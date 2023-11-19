:: @echo off

rem Load Enviroment variable from .env file
for /f "delims=# tokens=1,*" %%a in ('findstr /v /r "^#" .env') do (
    set "%%a"
)

rem List of environment variables to check (add new with space)s
set L_VARIABLES=ES_DIR ES_CONFIG

rem Check each variable
for %%a in (%L_VARIABLES%) do (
    if not defined %%a (
        echo Error: %%a is not set
        exit /b 1
    )
)

rem Starting Elasticsearch with the specified configuration file
"%ES_DIR%\bin\elasticsearch.bat"