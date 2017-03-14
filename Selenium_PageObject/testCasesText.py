
# you can separate web test cases by page name

def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Critical', 'User goes to main page, page should be loaded'],
    ['Critical', 'Main page, set the firstname textbox'],
    ['Critical', 'Main page, set the lastname textbox'],
    ['Critical', 'Main page, select if user is male or female'],
    ['Critical', 'Main page, select years of experience'],
    ['Critical', 'Main page, enter the date'],
    ['Critical', 'Main Page, select from profession options'],
    ['Critical', 'Main Page, select automation tools'],
    ['Critical', 'Main Page, select continents'],
    ['Critical', 'Main Page, select selenium commands'],
    ['Critical', 'Main Page, test file download'],
    ['Critical', 'Main Page, test file upload'],
]

