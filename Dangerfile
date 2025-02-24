# Check commit message format
danger.rule("Commit message format") do
    commit_message = git.commits.first.message
    title, description = commit_message.split("\n", 2)
  
    # Check title length
    fail("Commit title must be 50 characters or less") if title.length > 50
  
    # Check for empty line between title and description
    fail("Commit message must have an empty line between title and description") unless description.to_s.start_with?("\n")
  
    # Check description length
    if description
      description_lines = description.strip.split("\n")
      description_lines.each do |line|
        fail("Commit description lines must be 72 characters or less") if line.length > 72
      end
      fail("Commit description must have at least 5 characters") if description.strip.length < 5
    end
  
    # Check if commit follows Conventional Commits
    unless title.match(/^(feat|fix|chore|docs|refactor|test|style): .+/)
      fail("Commit title must follow the Conventional Commits specification: 'type: description'")
    end
  end