#!/usr/bin/env python3
"""
Global Youth Unemployment Analysis - Streamlit App Launcher

This script launches the interactive Streamlit web application for exploring
the global youth unemployment analysis and predictions.

Usage:
    python run_app.py

Requirements:
    - streamlit
    - pandas
    - plotly
    - All dependencies in requirements.txt

The app will be available at http://localhost:8501
"""

import subprocess
import sys
import os

def main():
    """Launch the Streamlit application"""

    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(script_dir, 'app', 'app.py')

    # Check if the app file exists
    if not os.path.exists(app_path):
        print(f"Error: App file not found at {app_path}")
        sys.exit(1)

    print("🌍 Global Youth Unemployment Analysis Dashboard")
    print("=" * 50)
    print("Launching Streamlit application...")
    print(f"App location: {app_path}")
    print("")
    print("The dashboard will open in your default web browser.")
    print("If it doesn't open automatically, visit: http://localhost:8501")
    print("")
    print("Press Ctrl+C to stop the application.")
    print("=" * 50)

    try:
        # Launch streamlit
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', app_path,
            '--server.headless', 'true',
            '--server.address', 'localhost',
            '--server.port', '8501'
        ], check=True)

    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching Streamlit: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Streamlit not found. Please install dependencies:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
