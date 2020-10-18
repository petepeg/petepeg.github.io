# [Boids](https://github.com/petepeg/PyGame-Boids)
This was a quick single day project where I wanted to try and write Boids just based on my interpretation of the rules. I challenged myself not to look at any other implementations of Boids during the process. This turned out to be more difficult than I thought, and has taken much longer and undergone many revisions to make them flock to my satisfaction.
### [Narrative](./boids_narrative)
### [Code Review](https://youtu.be/z4UUNoUIevc)
## Rules
1. **Separation:** steer to avoid crowding local flock mates
2. **Alignment:** steer towards the average heading of local flock mates
3. **Cohesion:** steer to move towards the average position (center of mass) of local flock mates

![Boids](/PyGame-Boids/boids.gif)
