#!/bin/bash

# Activate the virtual environment
source env/bin/activate || source env/Scripts/activate

# Run the test suite
pytest test_app.py

# Capture the exit code
TEST_EXIT_CODE=$?

# Deactivate the virtual environment
deactivate

# Exit with the appropriate code
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "One or more tests failed. Please check the output above."
    exit 1
fi
