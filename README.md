# Analysis of Job Offers

![GitHub last commit](https://img.shields.io/github/last-commit/alexaiung/job_scraper_and_analyzer)

![Project Cover](https://source.unsplash.com/featured/1280x720)

> This project aims to analyse job opportunities related to the field of data analysis. They were collected through web scraping of Linkedin, treated, and analysed. It is a useful dataset to understand what is expected when a company searches for a employee in the field, what they usually understand as related to it, and to focus in your job searching. I intend to expand the project so that people in other areas can also find useful insights in their areas.

## Prerequisites
If you intend to test the scraper in your machine, make sure you have the following dependencies installed:
- Selenium
- Pandas
- Numpy

## How to run the project
git clone https://github.com/alexaiung/job_scraper_and_analyzer

pip install requirements.txt

## Composition of the Dataset
The jobs opportunities found in the linkedin site were transformed accordingly, making it easier to analyze it. After cleaning, we have 1538 records and 19 columns. We also derived a secondary dataframe with information about all the skills associated with those 1538 job opportunities, which led us to 2667 rows, i. e. skills required.

## Initial Exploratory Analysis and Data Cleaning

### Wordcount
![Top-15 words most mentioned](<../images/top-15 words.png>)
The top-15 words most mentioned in jobs positions related to data analysis are the following. The top-5 words are pretty related to the field: words 1 and 3 to 5 are just the english and portuguese words for data analyst. It is interesting, however, the relevance of the word 'engineer', showing that a lot of companies that search for data-related profesionals are actually looking for data engineers. This is also relevant in the case of the word 'developer', showing a strong connection between the fields. The only word related directly to a specific hard skill is 'python'.

### Type of workplace
![Type of Workplace frequency](<../images/type_workplace.png>)
Though inplace and hybrid modalities of work are more frequent, there is a relative proximity between the 3 categories. That is to say that there is a diversity in the types of jobs available.

### Level
![Alt text](../images/level.png)
More than half the jobs are offered to senior-level professionals ('pleno-sênior'). After that, there is the assistant level with approximately a quarter of the jobs. The rest of the opportunities are for junior and estagiary level, but they are the minority. Executive and director levels were ommited because there were not a lot of them available.

### Worktype
![Alt text](../images/worktype.png)
Almost all jobs are full-time. There is a relevant amount of jobs classified as 'contract', but they could also be full-time. The remaining types are very non representative.

### Location
![Alt text](../images/city_state_general.png)
The city of São Paulo and São Paulo state are the main locations that the job offers are related. The second place is very distant from it, which is pretty understandable. São Paulo is the main economical center of Brazil. Besides that, since data analyst jobs don't necessarily need the proximity of the professional, the companies might be located there and offer opportunities for all the country. The remaining top cities and states are also those which the most prominent economy - namely, those in the southeast and southern region of Brazil. The presence of the northeastern state of Bahia and its capital, Salvador, is relevant since it shows a state outer of the main economical region; its presence, however, is very low compared to São Paulo and Rio de Janeiro.

## Skills Analysis

The following graph shows the most asked skills in the jobs analysed. It is interesting that most of them are not hard skills, but soft ones like communication, analytical skills, problem solving, and generic ones like data analysis, databases, computer science etc. SQL and Python are the most relevant hard skills, followed by Excel, Java and Microsoft Office.

![Alt text](../images/skills.png)

If we look the top-10 most asked skills by the type of workplace, we see that:
- Remote jobs asks for English, SQL, Python, Computer Science, and Data Science
- In-person and hybrid jobs asks for analytical skills, communication, data analysis, and problem solving
- All of the types asks for database skill.

![Alt text](<../images/top-10 skills type_workplace.png>)

Computer Science and Data Science are more specialized jobs; companies are more willing to rely on this knowledge when they hire someone who works remotely. They also asks for english since they must be international companies. In-person and hybrid jobs asks more frequently for themes related to convivence in a company - namely, data analysis is best done when you are immersed in a work environment. You also have more need for a good communication and problem solving when dealing with other employees.

### Skills categorization

Using ChatGPT, we created a classification of the most required skills in four categories.
Analytical skills are the more required. The main skills categorized as such are:

![Alt text](<../images/skills by category.png>)

![Alt text](../images/skill_category_habilidades_analiticas.png)

Technologies are the following. It is interesting the relevance of database skill, something that people intending to enter the data analysis market should focus. Microsoft Excel and Office are still very required - Excel still is, after all, the main data analysis tool in the market, even if there are more sophisticated technologies.

![Alt text](../images/skill_category_tecnologias.png)

In the communication category, it is important to know how to communicate - something very usual in most of the jobs. English is a main requirement too, which is very understandable. Not only a lot of companies are from other countries, but also there are brazilian companies that deal with international affairs.

![Alt text](../images/skill_category_comunicacao.png)

Finally, when we see the most required programming languages, we see the predominance of SQL = which is directly related to the requirement of database knowledge seen above - and Python, the main data analysis language in the market. It is interesting, however, the presence of Java and Javascript in a relatively high demand.

![Alt text](../images/skill_category_linguagens.png)