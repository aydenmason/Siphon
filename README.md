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
# Once IntelliJ IDEA is open:
# 1. Go to: Preferences -> Plugins
# 2. Search for "Minecraft Development"
# 3. Click "Install" to install the plugin
# 4. Restart IntelliJ IDEA to apply changes
# Siphon
