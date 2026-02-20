import trimesh
import sys

def measure(path):
    try:
        scene = trimesh.load(path, force='scene')
        extents = scene.extents
        print(f"{path}: {extents}")
    except Exception as e:
        print(f"Failed {path}: {e}")

measure('assets/Fence End.glb')
measure('assets/Gate.glb')
measure('assets/Swimming pool.glb')
measure('assets/Terrano.glb')
measure('assets/Tree.glb')
