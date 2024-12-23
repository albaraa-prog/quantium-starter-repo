@echo off

REM Activate the virtual environment
call env\Scripts\activate

REM Run the tests
pytest test_app.py
set TEST_EXIT_CODE=%ERRORLEVEL%

REM Deactivate the virtual environment
deactivate

REM Exit with the appropriate code
if %TEST_EXIT_CODE%==0 (
    echo All tests passed successfully!
    exit /b 0
) else (
    echo One or more tests failed. Please check the output above.
    exit /b 1
)
