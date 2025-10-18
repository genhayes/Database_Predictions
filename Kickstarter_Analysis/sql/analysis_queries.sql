-- Kickstarter Data Analysis SQL Queries
-- Examine database schema and analyze project success rates

-- 1. Get table schema and column information
.schema kickstarter_projects

-- 2. Display all column names
PRAGMA table_info(kickstarter_projects);

-- 3. Get basic statistics about the dataset
SELECT 
    COUNT(*) as total_projects,
    COUNT(DISTINCT main_category) as unique_categories,
    COUNT(DISTINCT country) as unique_countries,
    MIN(launched) as earliest_launch,
    MAX(launched) as latest_launch
FROM kickstarter_projects;

-- 4. Show all unique categories
SELECT DISTINCT main_category, COUNT(*) as project_count
FROM kickstarter_projects
GROUP BY main_category
ORDER BY project_count DESC;

-- 5. Analyze success rates by category
SELECT 
    main_category,
    COUNT(*) as total_projects,
    SUM(CASE WHEN state = 'successful' THEN 1 ELSE 0 END) as successful_projects,
    SUM(CASE WHEN state = 'failed' THEN 1 ELSE 0 END) as failed_projects,
    ROUND(
        100.0 * SUM(CASE WHEN state = 'successful' THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) as success_rate_percent
FROM kickstarter_projects
WHERE state IN ('successful', 'failed')
GROUP BY main_category
ORDER BY success_rate_percent DESC;

-- 6. Success rates by funding goal ranges
SELECT 
    CASE 
        WHEN goal < 1000 THEN 'Under $1K'
        WHEN goal < 5000 THEN '$1K - $5K'
        WHEN goal < 10000 THEN '$5K - $10K'
        WHEN goal < 50000 THEN '$10K - $50K'
        WHEN goal < 100000 THEN '$50K - $100K'
        ELSE 'Over $100K'
    END as goal_range,
    COUNT(*) as total_projects,
    ROUND(
        100.0 * SUM(CASE WHEN state = 'successful' THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) as success_rate_percent
FROM kickstarter_projects
WHERE state IN ('successful', 'failed')
GROUP BY goal_range
ORDER BY 
    CASE 
        WHEN goal < 1000 THEN 1
        WHEN goal < 5000 THEN 2
        WHEN goal < 10000 THEN 3
        WHEN goal < 50000 THEN 4
        WHEN goal < 100000 THEN 5
        ELSE 6
    END;

-- 7. Most successful categories with high project counts
SELECT 
    main_category,
    COUNT(*) as total_projects,
    ROUND(
        100.0 * SUM(CASE WHEN state = 'successful' THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) as success_rate_percent,
    AVG(goal) as avg_goal,
    AVG(pledged) as avg_pledged
FROM kickstarter_projects
WHERE state IN ('successful', 'failed')
GROUP BY main_category
HAVING COUNT(*) >= 100  -- Only categories with significant sample size
ORDER BY success_rate_percent DESC;

-- 8. Sample of successful projects for inspection
SELECT 
    name,
    main_category,
    goal,
    pledged,
    backers,
    country,
    launched,
    deadline
FROM kickstarter_projects
WHERE state = 'successful'
ORDER BY pledged DESC
LIMIT 10;