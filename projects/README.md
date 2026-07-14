# Project 2

# Problem Statement
The technology market changes rapidly, making it difficult for students, entry-level developers, and educational programs to know which programming skills are worth learning. This project analyzes real-world data to find out which programming languages offer the highest pay and the fastest growth for junior developers.



# Executive Summary
This project was built to find out where the technology industry is heading by looking at real-world survey data from thousands of software developers across the United States. The process started by cleaning the data and exploring the data generally and exploring it while focusing on factors that could affect the results, such as education and experience level.

The most important findings show that software development is rarely done using just one language; the highest-paying roles rely on combining specific foundational tools together. Furthermore, it was discovered that starting salaries change significantly depending on the language a junior developer specializes in, with certain modern backend tools growing in financial value much faster than older, traditional tools.

To conclude, anyone entering the tech market today can gain a massive advantage by being strategic about the skills they learn. It is recommended that schools and bootcamps update their classes to teach these high-value language combinations, and that job seekers focus their personal portfolios on the specific fast-growing languages highlighted in the project charts to secure the best starting pay.



# File Directory
Report.ipynb - Jupyter notebook with the code handling and cleaning data, as well as performing EDA

presentation_stack_overflow - presentation slides

Stack Overflow - folder with original data and new_data folder
        new_data - folder with cleaned data as csv and 4 charts 



# Data & Data Dictionary
The data for this project comes from the official Stack Overflow Annual Developer Survey for the years 2024 and 2025.
The cleaned data frame has the follwing columns: 
['MainBranch', 'Employment', 'RemoteWork', 'EdLevel', 'YearsCode', 'DevType', 'OrgSize', 'Country', 'Currency', 'CompTotal', 'LanguageHaveWorkedWith', 'WorkExp', 'Industry', 'ConvertedCompYearly']
results.csv: 
    MainBranch: description of respondents
    Employment: respondent's current employment status
    RemoteWork: work situation
    EdLevel: education level
    YearsCode: years of coding including education
    DevType: description of cuurent job
    OrgSize: number of people employed by repsondent's organization
    Country: country of residence of the respondent 
    Currency: currency used by respondent on a day-to-day basis
    CompTotal: current total annual compensation
    LanguagesHaveWorkedWith: languages the respondent has worked with
    WorkExp: professional work experience
    Industry: industry of the company the respondent works in
    ConvertedCompYearly: converted currencies to USD of CompTotal
    Year: 2024 or 2025 from original seperated files

extra_rows:
    same as results but with exploded languages column



# Important Visualizations
## Visualization 1 (2024 highest median languages): 
Identifies which single languages commanded the highest mid-point premium in the year 2024.
## Visualization 2 (2025 highest median languages): 
Identifies which single languages commanded the highest mid-point premium in the year 2025.
## Visualization 3 (Year-over-Year Growth Rate): 
Highlights which entry-level languages are accelerating in financial value the fastest moving into 2025.



# Conclusions & Recommendations
## Conclusion: 
Elimination of "Passenger Skills": When analyzing multi-language combinations, common languages (like JavaScript or HTML) appeared to command high salaries simply because they co-occurred with rare, high-paying skills. By isolating each language independently, it was discovered what the true standalone value of each language is.

Identification of Real Growth: By requiring a language to have at least 500 respondents in both 2024 and 2025, statistical anomalies from rare languages were successfully blocked out. It was discovered that the top 10 growth list reflects languages that are genuinely gaining market value.

Experience Outpaces Education: When comparing career paths, it was discovered that additional years of hands-on job experience increase median salaries much faster and higher than holding an advanced university degree.

## Recommendations: 
Focus on Growth Ecosystems: To maximize income potential, training and upskilling should be focused on the specific technologies identified in the top 10 growth chart rather than simply learning the most ubiquitous languages.

Skill-Specific Compensation: Companies should utilize these single-language median benchmarks to structure compensation packages for new hires, rather than relying on generic "software engineer" averages.

Prioritize Early Industry Entry: For individuals choosing between entering the workforce or pursuing an additional consecutive degree, the data suggests that securing professional, real-world experience yields a faster financial return.



# Areas for Further Research/Study
## Analyzing High-Value Pairings: 
Now that the top individual languages are known, it should be investigated how they behave when combined. For example, if two separate languages both command high medians, the next step is to analyze the salary impact when a developer knows both.

## Geographical Segmentation: 
Because compensation varies drastically by location, it should be explored whether these specific languages command a premium globally or if the data is heavily skewed by a few high-paying regions.

## Career Stage Cross-Tabulation: 
It should be determined whether these high-growth languages benefit entry-level developers, or if the salary increases are strictly concentrated among senior professionals with over a decade of experience.



# Sources
## Source 1: 
Stack Overflow Annual Developer Survey Datasets (2024 and 2025).

## Source 2: 
Matplotlib and Pandas Documentation.