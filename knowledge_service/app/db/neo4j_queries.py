QUERY_FIND_PROJECT_LIBS = """
MATCH (User:Person {id: $userId})
    -[:WORKED_ON]->(Project:Project)
    -[:USED_LIBRARY]->(Library:Software)
    -[:HAS_TAG]->(Tag:Category {name: $tag})
WHERE User.id = $userId
RETURN Library.name, Project.title, count(Library) AS UsageCount
ORDER BY UsageCount DESC
LIMIT 5
"""
