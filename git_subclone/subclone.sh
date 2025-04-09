# 1. Create an empty repository
git init repo_clone
cd repo_clone

# 2. Add the remote repository
git remote add origin https://github.com/user/repo.git  # Replace with your repo URL

# 3. Enable sparse-checkout
git config core.sparseCheckout true

# 4. Define the folder you want to check out (e.g., `subdir/`)
echo "subdir/" > .git/info/sparse-checkout

# 5. Pull only the specified folder
git pull origin main  # Replace "main" with the correct branch if needed
