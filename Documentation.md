# VR Villa Experience Documentation

## 1. Design Choices
Building the VR Villa experience required a combination of technical decisions and aesthetic refinements aimed at creating an immersive and structured 3D environment. Here are the core design choices made during development:

*   **Framework Selection:** A-Frame was chosen as the primary engine due to its flexible Entity-Component-System (ECS) architecture, which simplified the integration of 3D models, textures, and interactive elements using standard web technologies.
*   **Architectural Layout:** The interior was designed with a realistic multi-room layout to delineate distinct zones, including a living room, bedroom, and kitchen. This approach helps structure the VR experience, making navigation intuitive for the user.
*   **Interactive Lighting:** A dynamic lighting system was implemented with interactable switches (Low, Medium, High). This interactivity deepens immersion, allowing users to experience the villa under different lighting conditions.
*   **Animated Pool & Water:** Rather than using a static texture, a custom water shader component (`ada-water.js`) was added. The dynamic wave physics significantly enhance the realism of the outdoor terrace and swimming pool area.
*   **Environmental Context:** To ground the villa in a realistic setting, surrounding elements like grass yards, large scale trees, a perimeter fence with a gate, and a parked vehicle were included to make the scene feel less empty and more engaging.

## 2. Technical Challenges & Solutions
Developing a web-based VR experience introduced several technical hurdles, primarily regarding performance and visual accuracy:

*   **Challenge: Interior Lighting Balance**
    *   *Issue:* Early iterations of the interior walls appeared excessively white and blown-out due to harsh lighting and reflective material properties.
    *   *Solution:* The interior wall geometries were rebuilt and the material shaders were refined to produce a warmer, softer appearance. Ambient and point lights were also re-calibrated so that distinct objects wouldn't lose their textured details under bright light.
*   **Challenge: Scene Optimization and Framerate**
    *   *Issue:* Loading multiple high-polygon 3D models (couches, trees, vehicles) initially impacted the VR performance and frame rates.
    *   *Solution:* Assets were carefully selected and scaled. Where possible, standard A-Frame primitives (boxes, cylinders, planes) were used to build up architectural features to save on polygon count. Repetitive layout operations (such as generating the large perimeter fence) were scripted externally to ensure precision without heavy manual DOM operations.
*   **Challenge: Deploying as a Structured VLE Deliverable**
    *   *Issue:* Organizing the project into a clean, hostable package that adhered to strict path requirements (e.g., `/Examination` routing).
    *   *Solution:* The project was restructured to isolate the necessary deliverables so they could be cleanly zipped, while modern hosting (like Vercel) allowed for route aliasing to meet the URL requirements without breaking asset paths.

## 3. Future Improvements
While the current villa establishes a strong foundation, the next iterations can introduce several enhancements:

*   **Advanced Physics and Collisions:** Introduce a physics engine (like Ammo.js or Cannon.js) to restrict player movement so they cannot walk through walls or furniture, enhancing the spatial realism.
*   **Spatial Audio:** Implement directional sound sources—such as the sound of splashing water near the pool, birds in the trees, or ambient music in the living room—to create a multi-sensory environment.
*   **More Interactivity:** Add functional doors that open on approach, interactive kitchen appliances, or grab-and-drop mechanics for smaller furniture items utilizing VR controllers.
*   **Texture Atlasing:** Combine multiple individual image textures into texture atlases. This would significantly reduce the number of HTTP requests during the initial load, leading to a faster and smoother start to the VR experience.
