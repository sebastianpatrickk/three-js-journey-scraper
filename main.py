from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os


def click_button_and_scrape_links(url, ):
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # Go to the provided URL
    driver.get(url)

    input("Press Enter to continue...")

    # Find the button using its id and click it
    # driver.find_element(By.ID, button_id).click()
    print('clicked')

    # Get the HTML content of the page
    html = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the a tags with class 'cWBoni'
    links = soup.find_all('a', class_='cWBoni')

    # Initialize an empty list to store the objects
    link_objects = []

    # Loop through each link
    for link in links:
        # Get the href attribute of the link
        href = link.get('href')

        # Find the span tag with the specified classes within the link and get its text
        name = link.find('span', class_='sc-bdvvtL joBMCC sc-hKwDye boqnux sc-1vxxt31-3 hWmLfN').text

        # Create an object with the href and name and append it to the list
        link_objects.append({'link': href, 'name': name})

    # Filter out objects that do not contain "Three.js Journey" in the name
    filtered_objects = [obj for obj in link_objects if "Three.js Journey" in obj['name']]

    # Print the filtered list of objects
    for obj in filtered_objects:
        print(obj)

    # Create a new text file
    with open('output.txt', 'w') as file:
        # Write the array to the file
    
        file.write(str(filtered_objects))

    print("Array written to output.txt file.")


# Use the function
# click_button_and_scrape_links('https://vimeo.com/user105133586')

videos = [{'link': '/917152638', 'name': 'Three.js Journey Shaders Update (discount)'}, {'link': '/882839845', 'name': 'Three.js Journey 2023 November Update (discount)'}, {'link': '/880103452', 'name': '11 Materials Three.js Journey'}, {'link': '/880097103', 'name': '09 Debug UI Three.js Journey'}, {'link': '/880095099', 'name': '03 First Three.js project Three.js Journey'}, {'link': '/839468451', 'name': '58 Environment map (full) Three.js Journey'}, {'link': '/838604230', 'name': '58 Environment map Three.js Journey'}, {'link': '/763566298', 'name': '61 Portal Scene with R3F Three.js Journey'}, {'link': '/763565162', 'name': '66 Create a game with R3F Three.js Journey'}, {'link': '/763565132', 'name': '65 Physics with R3F Three.js Journey'}, {'link': '/763565105', 'name': '64 Fun and simple portfolio with R3F Three.js Journey'}, {'link': '/763565044', 'name': '63 Post-processing with R3F Three.js Journey'}, {'link': '/763565017', 'name': '62 Mouse events with R3F Three.js Journey'}, {'link': '/763564992', 'name': '60 3D Text with R3F Three.js Journey'}, {'link': '/763564947', 'name': '59 Load a Model with R3F Three.js Journey'}, {'link': '/763564880', 'name': '58 Environment and staging with R3F Three.js Journey'}, {'link': '/763564843', 'name': '57 Debug a R3F Application Three.js Journey'}, {'link': '/763564812', 'name': '56 R3F and Drei Three.js Journey'}, {'link': '/763564755', 'name': '55 First R3F Application Three.js Journey'}, {'link': '/763564715', 'name': '54 First React Application Three.js Journey'}, {'link': '/763564603', 'name': '53 What are React and React Three Fiber Three.js Journey'}, {'link': '/716318362', 'name': '52 Adding Details to the Scene Three.js Journey'}, {'link': '/716318335', 'name': '51 Importing and Optimizing the Scene Three.js Journey'}, {'link': '/716318262', 'name': '50 Baking and Exporting the Scene Three.js Journey'}, {'link': '/716318188', 'name': '49 Creating a Scene in Blender Three.js Journey'}, {'link': '/716318120', 'name': '48 Mixing HTML and WebGL Three.js Journey'}, {'link': '/716318061', 'name': '47 Intro and Loading Progress Three.js Journey'}, {'link': '/716318017', 'name': '46 Performance Tips Three.js Journey'}, {'link': '/716317976', 'name': '45 Post-Processing Three.js Journey'}, {'link': '/716317957', 'name': '31 Modified Materials Three.js Journey'}, {'link': '/716317909', 'name': '30 Animated Galaxy Three.js Journey'}, {'link': '/716317855', 'name': '29 Raging Sea Three.js Journey'}, {'link': '/716317802', 'name': '28 Shader Patterns Three.js Journey'}, {'link': '/716317756', 'name': '27 Shaders Three.js Journey'}, {'link': '/716317644', 'name': '26 Code Structuring for Bigger Projects Three.js Journey'}, {'link': '/716186965', 'name': '25 Realistic Render Three.js Journey'}, {'link': '/716186918', 'name': '23 Custom Models with Blender Three.js Journey'}, {'link': '/716186868', 'name': '21 Imported Models Three.js Journey'}, {'link': '/716186833', 'name': '20 Physics Three.js Journey'}, {'link': '/716186759', 'name': '19 Scroll Based Animation Three.js Journey'}, {'link': '/716186704', 'name': '19 Raycaster and Mouse Events Three.js Journey'}, {'link': '/716186630', 'name': '18 Galaxy Generator Three.js Journey'}, {'link': '/716186585', 'name': '17 Particles Three.js Journey'}, {'link': '/716186487', 'name': '16 Haunted House Three.js Journey'}, {'link': '/716186391', 'name': '15 Shadows Three.js Journey'}, {'link': '/716186348', 'name': '14 Lights Three.js Journey'}, {'link': '/716186283', 'name': '13 Go Live Three.js Journey'}, {'link': '/716186250', 'name': '12 3D Text Three.js Journey'}, {'link': '/716100578', 'name': '10 Textures Three.js Journey'}, {'link': '/716100511', 'name': '08 Geometries Three.js Journey'}, {'link': '/716100461', 'name': '07 Fullscreen and resizing Three.js Journey'}, {'link': '/716100402', 'name': '06 Cameras Three.js Journey'}, {'link': '/716100350', 'name': '05 Animations Three.js Journey'}, {'link': '/716004661', 'name': '02 What is WebGL and why use Three.js Three.js Journey'}, {'link': '/714923739', 'name': '04 Transform Objects Three.js Journey'}, {'link': '/714750748', 'name': '01 Introduction Three.js Journey'}]

def convert_videos_to_links(videos):
    # Initialize an empty list to store the converted links
    links = []

    # Loop through each video dictionary
    for video in videos:
        # Get the link and name from the dictionary
        link = video['link']
        name = video['name']

        # Create the HTML link with the provided URL and video link
        html_link = f'<a href="https://vimeo.com{link}" target="_blank">{name}</a>'

        # Append the HTML link to the list
        links.append(html_link)

    # Write the links to an HTML file
    with open('output.html', 'w') as file:
        # Write the HTML header
        file.write('<html><body>')

        # Loop through each link
        for link in links:
            # Write the link to the file
            file.write(link)

        # Write the HTML footer
        file.write('</body></html>')

    print("Links written to output.html file.")



convert_videos_to_links(videos)

