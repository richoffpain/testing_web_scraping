import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

page = requests.get(url) # make the request and get back a status code
soup = BeautifulSoup(page.content, 'html.parser') # pass the content of the page as status code is successful and parse it
result = soup.find(id="ResultsContainer") # find the block that contains the jobs and focus and it
job_elements = result.find_all('div', class_='card-content') # get the list of the jobs in the container
# get an idea about the jobs
for each_job in job_elements:
    title = each_job.find('h2', class_='title')
    company = each_job.find('h3', class_='company')
    loc = each_job.find('p', class_='location')
    #print(title.get_text().strip())
    #print(company.text.strip())
    #print(loc.string.strip())
    print()
#print(result.prettify())

# now we will filter the jobs to only get python dev jobs
python_jobs = result.find_all('h2', string=lambda text: 'python' in text.lower())
element_python = [h2_el.parent.parent.parent for h2_el in python_jobs] # travel back to parent container that has all the information about the job  like title loc and company so we dont run into an error when trying to access one of this variable below
for n in element_python:
    title = n.find('h2', class_='title')
    company = n.find('h3', class_='company')
    loc = n.find('p', class_='location')
    """
        links = n.find_all('a')
        for link in links:
        link = link['href']
        print(link)
    """
    #link_job = n.find_all('a', string=lambda text: 'Apply' in text.lower())
    link_url = n.find_all('a')[1]['href']
    print(title.get_text().strip())
    print(company.get_text().strip())
    print(loc.string.strip())
    print(link_url)
    print()
    
    

