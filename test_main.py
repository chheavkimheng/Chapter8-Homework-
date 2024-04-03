import unittest
from main import generate_report

class TestGenerateReport(unittest.TestCase):
    def test_generate_report(self):
        expected_report = {
            'dev_activities': {'Hobby': 51942, 'Professional development or self-paced learning from online courses': 26957, 'Contribute to open-source projects': 18231}, 
            'most_used_language': {'JavaScript': 55711, 'HTML/CSS': 46396, 'Python': 43158}, 
            'most_wanted_language': {'JavaScript': 34986, 'Python': 34715, 'TypeScript': 32256}, 
            'most_used_framework': {'Node.js': 30626, 'React': 29137, 'jQuery': 15784}, 
            'most_wanted_framework': {'React': 24100, 'Node.js': 23027, 'Next.js': 14129}, 
            'most_used_tool': {'Visual Studio Code': 63793, 'Visual Studio': 24605, 'IntelliJ IDEA': 23209}, 
            'most_wanted_tool': {'Visual Studio Code': 50588, 'IntelliJ IDEA': 16887, 'Visual Studio': 15755}, 
            'most_personal_operating_system': {'Windows': 52086, 'MacOS': 28407, 'Ubuntu': 23791}, 
            'most_professional_operating_system': {'Windows': 40917, 'MacOS': 28786, 'Ubuntu': 23281}, 
            'popular_industry': {'Information Services, IT, Software Development, or other Technology': 18159, 'Financial Services': 4421, 'Other': 4011}
        }

        report = generate_report()
        self.assertEqual(report, expected_report)

if __name__ == "__main__":
    unittest.main()