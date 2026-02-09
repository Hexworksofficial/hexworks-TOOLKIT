import subprocess
import sys
import os

if len(sys.argv) < 5:
    print("Usage: convert_mesh.exe <blender_path> <addon_path> <input_mesh> <output_fbx>")
    input("Press Enter to exit...")
    sys.exit(1)

BLENDER_PATH = os.path.abspath(sys.argv[1])
ADDON_PATH = os.path.abspath(sys.argv[2])
INPUT_MESH = os.path.abspath(sys.argv[3])
OUTPUT_FBX = os.path.abspath(sys.argv[4])

SCRIPT_PATH = os.path.join(os.path.dirname(sys.argv[0]), "auto_mesh_to_fbx.py")

try:
    result = subprocess.run([
        BLENDER_PATH,
        "--background",
        "--python", SCRIPT_PATH,
        "--", ADDON_PATH, INPUT_MESH, OUTPUT_FBX
    ], check=True)
except subprocess.CalledProcessError as e:
    print("Blender returned an error!")
    print(e)
    input("Press Enter to exit...")
    sys.exit(1)

print("Conversion complete!")
input("Press Enter to exit...")
