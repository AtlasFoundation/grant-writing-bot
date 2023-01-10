USE grant_db;

CREATE TABLE organizations (
    org_id INT(11) NOT NULL AUTO_INCREMENT,
    org_name VARCHAR(255) NOT NULL,
    org_website VARCHAR(255) NOT NULL,
    org_email VARCHAR(255) NOT NULL,
    org_phone VARCHAR(255) NOT NULL,
    PRIMARY KEY (org_id)
);
