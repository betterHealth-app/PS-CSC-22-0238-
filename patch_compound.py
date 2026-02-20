import re

html = """
      <!-- Natural Compound Elements -->
      <!-- Global Ambient Space Lighting to fix Dim Outer Shadows -->
      <a-light type="ambient" color="#cccccc" intensity="0.5"></a-light>
      <a-light type="directional" color="#ffffff" intensity="0.6" position="-10 20 15" shadow="cast: true"></a-light>

      <!-- Green Grass Yard -->
      <a-plane id="grass-yard" position="0 0.1 0" rotation="-90 0 0" scale="250 250 1" material="color: #4CAF50; roughness: 1; metalness: 0"></a-plane>

      <!-- Parking Lot / Driveway -->
      <a-plane id="driveway" position="8.5 0.12 15" rotation="-90 0 0" scale="8 15 1" material="color: #888888; roughness: 0.9; metalness: 0"></a-plane>

      <!-- The Car -->
      <a-entity id="family-car" gltf-model="#car-model" position="8.5 0.15 15" rotation="0 180 0" scale="2 2 2" shadow="cast: true; receive: true"></a-entity>

      <!-- The Swimming Pool -->
      <a-entity id="swimming-pool" gltf-model="#pool-model" position="-18 0.3 -22.0" rotation="0 0 0" scale="0.15 0.15 0.15" shadow="cast: true; receive: true"></a-entity>

      <!-- Trees -->
      <a-entity gltf-model="#tree-model" position="25 0.00 30" rotation="0 45 0" scale="3 3 3" shadow="cast: true; receive: true"></a-entity>
      <a-entity gltf-model="#tree-model" position="-25 0.00 30" rotation="0 135 0" scale="3.5 3.5 3.5" shadow="cast: true; receive: true"></a-entity>
      <a-entity gltf-model="#tree-model" position="-28 0.00 -12" rotation="0 225 0" scale="2.8 2.8 2.8" shadow="cast: true; receive: true"></a-entity>
      <a-entity gltf-model="#tree-model" position="15 0.00 -25" rotation="0 315 0" scale="3 3 3" shadow="cast: true; receive: true"></a-entity>
      <a-entity gltf-model="#tree-model" position="-15 0.00 35" rotation="0 0 0" scale="4 4 4" shadow="cast: true; receive: true"></a-entity>
      <a-entity gltf-model="#tree-model" position="30 0.00 5" rotation="0 90 0" scale="5 5 5" shadow="cast: true; receive: true"></a-entity>
      <a-entity gltf-model="#tree-model" position="-35 0.00 0" rotation="0 -90 0" scale="6 6 6" shadow="cast: true; receive: true"></a-entity>

      <!-- Fence Perimeter -->
      <a-entity id="perimeter-fence">
        <!-- Front Gate -->
        <a-entity gltf-model="#gate-model" position="0 0.15 45" rotation="0 0 0" scale="0.003 0.003 0.003"></a-entity>
"""

# Back fence at z=-40
for x in range(-38, 42, 4):
    html += f'        <a-entity gltf-model="#fence-end-model" position="{x} 0.15 -40" rotation="0 180 0" scale="3 3 3"></a-entity>\n'

# Front fence at z=45 (excluding gate)
for x in range(-38, -2, 4):
    html += f'        <a-entity gltf-model="#fence-end-model" position="{x} 0.15 45" rotation="0 0 0" scale="3 3 3"></a-entity>\n'
for x in range(4, 42, 4):
    html += f'        <a-entity gltf-model="#fence-end-model" position="{x} 0.15 45" rotation="0 0 0" scale="3 3 3"></a-entity>\n'

# Left fence at x=-40
for z in range(-38, 44, 4):
    html += f'        <a-entity gltf-model="#fence-end-model" position="-40 0.15 {z}" rotation="0 90 0" scale="3 3 3"></a-entity>\n'

# Right fence at x=40
for z in range(-38, 44, 4):
    html += f'        <a-entity gltf-model="#fence-end-model" position="40 0.15 {z}" rotation="0 -90 0" scale="3 3 3"></a-entity>\n'

html += """      </a-entity>
    </a-scene>"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace existing compound block
pattern = r'<!-- Natural Compound Elements -->.*?</a-scene>'
new_content = re.sub(pattern, html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html to fix dim walls, move trees, and resize compound!")

