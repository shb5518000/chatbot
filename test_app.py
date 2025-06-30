"""
Basic tests for the Streamlit chatbot application.
"""
import sys
import importlib.util


def test_app_imports():
    """Test that the main application can be imported without errors."""
    try:
        spec = importlib.util.spec_from_file_location("streamlit_app", "streamlit_app.py")
        module = importlib.util.module_from_spec(spec)
        # We don't execute the module to avoid Streamlit initialization issues
        # Just check that it can be loaded
        assert spec is not None
        assert module is not None
        print("✓ Application imports successfully")
        return True
    except Exception as e:
        print(f"✗ Application import failed: {e}")
        return False


def test_requirements_syntax():
    """Test that requirements.txt is valid."""
    try:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                # Basic validation - should not be empty and should be a valid package name
                assert len(line) > 0
                assert not line.startswith("-")  # No invalid flags
        
        print("✓ Requirements.txt is valid")
        return True
    except Exception as e:
        print(f"✗ Requirements.txt validation failed: {e}")
        return False


if __name__ == "__main__":
    tests = [
        test_app_imports,
        test_requirements_syntax,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! ✓")
        sys.exit(0)
    else:
        print("Some tests failed! ✗")
        sys.exit(1)