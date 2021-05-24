import requests
from bs4 import BeautifulSoup
import time

def scraper():
    """
    Scrape timesjobs.com,
    filter jobs with date posted,
    allow user to filter out the unfamiliar skills he/she have,
    save the info in a file.txt with index 
    """
    print('Put some skill that you are not familiar with')
    unfamiliar_skill = input('>')
    print(f'filtering out {unfamiliar_skill}')

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35')
    soup = BeautifulSoup(html_text.text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text # the text is inside another span tag
        if 'today' in published_date: # filtering out with published date in order to scrape other information
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip() # strip to remove whitespace at the beginning and end of the string
            keyskills = job.find('span', class_ = 'srp-skills').text.strip()
            more_info = job.header.h2.a['href'] # to find link to description
            if unfamiliar_skill not in keyskills:
                with open(f'posts/{index}.txt', 'w') as f:
                   f.write(f'Company Name: {company_name} \n')
                   f.write(f'Required skills: {keyskills} \n')
                   f.write(f'Published date: {published_date} \n')
                   f.write(f'Link: {more_info}')
                print(f'file saved: {index}')
                
            

                # print(f'Company Name: {company_name}')
                # print(f'Required skills: {keyskills}')
                # print(f'Published date: {published_date}')
                # print(f'Link: {more_info}')
            

if __name__ == '__main__':
    while True:
        scraper()
        time_wait = 10 
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60) # wait for 10 minutes and run again