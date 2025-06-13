-- Initialize the review database
CREATE DATABASE IF NOT EXISTS review;
USE review;

-- Grant privileges to django_user
GRANT ALL PRIVILEGES ON review.* TO 'django_user'@'%';
FLUSH PRIVILEGES;

-- Optional: Create a sample table to verify setup
-- You can remove this if not needed
CREATE TABLE IF NOT EXISTS test_connection (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    message VARCHAR(255) DEFAULT 'Database connected successfully'
);

