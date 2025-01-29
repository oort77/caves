# Prehistoric Caves Map

## Overview
This project visualizes prehistoric caves in Northern Israel using **Folium**, a Python library for interactive maps. It maps significant archaeological cave sites with markers categorized by historical periods:
- Lower Paleolithic
- Middle Paleolithic
- Upper Paleolithic
- Natufian culture

The generated map allows users to toggle different layers based on periods, helping visualize human occupation over time.

## Features
- **Interactive Map**: Users can explore cave locations with popups providing historical period details.
- **Categorization by Period**: Caves are grouped into layers based on their historical period.
- **Layer Control**: Users can toggle between period-based cave layers.
- **Automatic Centering**: The map is centered based on the mean latitude and longitude of the caves.
- **Optimized View**: The map bounds fit all cave locations for a better viewing experience.

## Installation
### Prerequisites
Ensure you have Python installed along with the required package:
```sh
pip install folium
```

## Usage
1. **Run the script**:
   ```sh
   python script.py
   ```
2. **Open the generated map**:
   - The script creates an interactive `map.html` file.
   - Open `map.html` in any web browser to explore the caves.

## Example Output
When opening `map.html`, users will see an interactive map with toggles for each period, displaying cave locations with detailed popups.

## Future Enhancements
- **Custom Styling**: Improve marker icons and colors for each period.
- **Additional Data**: Include more prehistoric sites across different regions.
- **Advanced Interactivity**: Implement time-slider or heatmaps for better data representation.

## License
This project is released under the MIT License.

---
**Author:** oort77

