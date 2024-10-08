import sys
import os

package_dir = os.path.dirname(__file__)

print("Add package directory:", package_dir.split('\\')[-1], " to PYTHONPATH.")
sys.path.append(package_dir)

