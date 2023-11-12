# FILEPATH: /d:/WebDevProjs/TCR_JavaScript/test_or_revert.ps1

# Run Jest tests
python main.py

# Check if tests passed
if ($LASTEXITCODE -ne 0) {
  # Tests failed, reset changes
  git reset --hard
} else {
  # Tests passed, prompt for commit message
  git add ./src
  git add ./test_or_revert.ps1
  $commitMessage = Read-Host "Tests passed. Enter commit message"

  if ($commitMessage -eq "") {
    # No commit message, reset changes
    git commit -m 'Tests passed.'
  }
  else {
     # Commit changes with message
    git commit -m $commitMessage
  }
}
