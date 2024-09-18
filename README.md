# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Verify Homebrew installation
brew doctor

# Install Java (OpenJDK)
brew install openjdk

# Verify Java installation
java -version

# Install Maven
brew install maven

# Verify Maven installation
mvn -version

# Install IntelliJ IDEA Community Edition
brew install --cask intellij-idea-ce

# Set up JAVA_HOME (add to .zshrc or .bash_profile)
echo 'export JAVA_HOME=$(/usr/libexec/java_home)' >> ~/.zshrc

# Apply the changes
source ~/.zshrc  # or ~/.bash_profile

# Launch IntelliJ IDEA
open -a "IntelliJ IDEA"

# Install Minecraft Development Extension
Once IntelliJ IDEA is open:
- #1. Go to: Preferences -> Plugins
- #2. Search for "Minecraft Development"
- #3. Click "Install" to install the plugin
- #4. Restart IntelliJ IDEA to apply changes


make changes to plugin if needed. 

export by clicking the maven button on far right. then double click package
notice the jar on the left side of your screen boxed in red. 

put that in plugin directory on your server. 



[video instructions if needed for maven]([https://www.example.com](https://www.youtube.com/watch?v=h9_UCAQ3j_w))


it will track users data for 15 minutes. do some transforms + computations. will run the user against them model predicting a verdict.

data pipeline goes like this. 

paper_server->playerlog.txt->transformer->ML->returns prediction verdict

paper_server->playerlog.txt->transformer->physical computation of verdict->compare to ML

this is known as SUPERVISED LEARNING. 

azure architecure.

prototype -> 
azure VM -> hosting server -> logging data -> transforming data-> computation verdict
transormed data -> ML model verdict 

blob storage
store minecraft model
log files 
"sus" playerIDs

go out to server owners offereing our services. business model TBD



