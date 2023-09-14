# SBIR-STTR-Data
Total SBIR/STTR Award Amounts Through The Years

_Overview_
This project aims to visualize the growth of the SBIR/STTR funding programs over the years. The project was inspired by the data visualizations by DataIsBeautiful and 
serves as a practical application during my fellowship with AFWERX, an innovation and venture capital arm of the U.S. Air Force.

_Technical Stack_
Data Cleaning: Python (Pandas)
Data Visualization: Matplotlib, MoviePy
Animation: MoviePy
Data Source: SBIR.gov

**Challenges and Solutions**

_Large Dataset_
Challenge: The initial dataset was too large to be processed by Google Sheets or any freely available cloud services.

Solution: Used Python's Pandas library to efficiently filter out the necessary rows from the large dataset.

_Data Aggregation_
Challenge: Needed to sum the total awards for each year.

Solution: Utilized Python to group the data by year and calculate the sum of awards for each year.

_Data Visualizatio_
Challenge: Wanted to create a dynamic, animated line chart to better visualize the data WITH audio.

Solution: Used Matplotlib for plotting and its animation function to create the dynamic chart. Integrated MoviePy to add audio to the animation, providing a more engaging 
user experience.

_Business Impact_
This project serves as a valuable tool for understanding the historical trends in SBIR/STTR funding, enabling better decision-making for stakeholders involved in these 
programs.

_Future Work_
Integrate the visualization into a web application for easier access by stakeholders.

_Final Thoughts_
This was a fun and educational project, marking my first significant success in data analysis and visualization. I was able to not only clean and prepare the data but also 
to create a dynamic visualization, adding layers of complexity and insight to a static dataset.
