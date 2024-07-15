# Initialize the occupancy grid
grid_size = (100, 100)  # Example grid size
occupancy_grid = np.zeros(grid_size)

def update_occupancy_grid(fgmask, occupancy_grid):
    # Resize fgmask to match the grid size
    resized_mask = cv2.resize(fgmask, grid_size)
    
    # Update occupancy grid
    occupancy_grid[resized_mask > 0] = 1  # Mark occupied cells
    occupancy_grid[resized_mask == 0] = 0  # Mark free cells

# Read frames in a loop and update the occupancy grid
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    fgmask = fgbg.apply(frame)
    update_occupancy_grid(fgmask, occupancy_grid)
    
    # Display the occupancy grid
    cv2.imshow('Occupancy Grid', occupancy_grid * 255)  # Scale for visualization
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
