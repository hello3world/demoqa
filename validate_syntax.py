#!/usr/bin/env python
"""Quick syntax validation of modified files."""
import sys

try:
    print("Importing pages.base_page...")
    from pages.base_page import BasePage

    print("✓ BasePage imported")

    print("Importing pages.elements.web_table_page...")
    from pages.elements.web_table_page import WebTablePage

    print("✓ WebTablePage imported")

    print("Importing pages.elements.elements_page...")
    from pages.elements.elements_page import ElementsPage

    print("✓ ElementsPage imported")

    print("Importing pages.elements.dynamic_properties_page...")
    from pages.elements.dynamic_properties_page import DynamicPropertiesPage

    print("✓ DynamicPropertiesPage imported")

    print("\nAll imports successful!")
    sys.exit(0)
except Exception as e:
    print(f"✗ Error: {e}", file=sys.stderr)
    import traceback

    traceback.print_exc()
    sys.exit(1)
