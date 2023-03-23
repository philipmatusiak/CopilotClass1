# Commit to GitHub
import subprocess

# Define the path to your output.md file
output_path = 'C:\\Users\\philm\\Documents\\PythonOpenAIWithGithub\\output.md'

# Configure Git with your GitHub credentials
github_username = 'philipmatusiak'
github_email = 'philip@philipmatusiak.com'
subprocess.call(['git', 'config', '--global', 'user.name', github_username])
subprocess.call(['git', 'config', '--global', 'user.email', github_email])

# Initialize a new Git repository
subprocess.call(['git', 'init'])

# Add the output.md file to the Git staging area
subprocess.call(['git', 'add', 'output.md'])
subprocess.call(['git', 'add', 'GitUpload.py'])
# Commit the changes
subprocess.call(['git', 'commit', '-m', 'output.md'])
subprocess.call(['git', 'commit', '-m', 'GitUpload.py'])

# Set the remote URL for the GitHub repository
#remote_url = 'https://github.com/your-username/your-repository.git'
remote_url = 'https://github.com/philipmatusiak/CopilotClass1.git'
subprocess.call(['git', 'remote', 'add', 'origin', remote_url])
# Push the changes to the remote repository
subprocess.call(['git', 'push', '-u', 'origin', 'master'])

# Print Complete
print("Complete")
