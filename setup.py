from setuptools import find_packages, setup

def get_requirements() -> list[str]:
    """
    This function will return list of requirements
    """
    requirement_list: list[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list
print(get_requirements())

setup(
    name="AI-TRAVEL-PLANNER",
    version="0.0.1",
    author="Ramya Kalisetti",
    author_email="kramyasudha2024@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)